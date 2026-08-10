# repository.py
import json
from quiz import Quiz
from config import SEED_QUIZ_PATH, CUSTOM_QUIZ_PATH, STATE_PATH


class QuizRepository:
    def __init__(self, seed_path=SEED_QUIZ_PATH, custom_path=CUSTOM_QUIZ_PATH, state_path=STATE_PATH):
        self.seed_path = seed_path
        self.custom_path = custom_path
        self.state_path = state_path

        self.best_score = 0.0
        self.quizzes = []

        self.load_state()

    def load_state(self):
        if self.state_path.exists():
            with open(self.state_path, "r", encoding="utf-8") as file:
                state_data = json.load(file)

            quizzes_data = state_data.get("quizzes", [])
            self.best_score = state_data.get("best_score", 0.0)

        else:
            quizzes_data = self._load_json(self.seed_path)
            self.best_score = 0.0

        self.quizzes = []

        for item in quizzes_data:
            quiz = Quiz(
                question=item["question"],
                choices=item["choices"],
                answer=item["answer"]
            )

            self.quizzes.append(quiz)


    def _load_json(self, filepath):
        """지정한 JSON 파일 존재시 읽어오는 메서드 / 없으면 [] 반환 """
        if filepath.exists():
            with open(filepath, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []


    def add_quiz(self, question, choices, answer):
        for existing_quiz in self.quizzes:
            if existing_quiz.question == question:
                return False

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        self.save_state(self.best_score)
        return True


    def get_all_quizes(self):
        return self.quizzes

    def save_state(self, best_score):
        self.best_score = best_score

        quizzes_data = [
            {
                "question" : q.question,
                "choices" : q.choices,
                "answer" : q.answer
            }
            for q in self.quizzes
        ]

        state_data= {
            "quizzes": quizzes_data, 
            "best_score": self.best_score
        }

        self.state_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.state_path, "w", encoding="utf-8") as f:
            json.dump(state_data, f, ensure_ascii=False, indent= 4)
        

    def get_best_score(self):
        return self.best_score