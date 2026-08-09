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
            try:
                with open(self.state_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    self.best_score = data.get("best_score", 0.0)
            except json.JSONDecodeError:
                self.best_score = 0.0
        self.load_quizzes()

    def _load_json(self, filepath):
        """지정한 JSON 파일 존재시 읽어오는 메서드 / 없으면 [] 반환 """
        if filepath.exists():
            with open(filepath, "r", encoding="utf-8") as f:
                try:
                    return json.load(f)
                except json.JSONDecodeError:
                    return []
        return []

    def load_quizzes(self):
        """시드데이터와 커스텀데이터 합쳐서 둘 다 담긴 하나의 퀴즈 리스트로 병합"""
        seed_data = self._load_json(self.seed_path)
        custom_data = self._load_json(self.custom_path)

        self.quizzes = []
        for item in seed_data + custom_data:
            quiz = Quiz(
                question = item["question"],
                choices = item["choices"],
                answer = item["answer"]
            )

            self.quizzes.append(quiz)


    def add_custom_quiz(self, question, choices, answer):
        "새로운 커스텀 퀴즈 추가 및 custom_quizzes.json 에 영구 저장"

        # 0. 퀴즈 중복 여부 확인
        for existing_quiz in self.quizzes :
            if existing_quiz.question == question:
                print("⚠️ 이미 동일한 질문의 퀴즈가 존재합니다. ")
                return False # 함수 강제종료해서 추가 방어
            

        # 1. 새로운 퀴즈 객체 생성 
        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)

        # 2. 기존 커스텀 데이터 불러오기
        custom_data = self._load_json(self.custom_path)

        # 3. 새로운 데이터 추가
        custom_data.append({
            "question": question,
            "choices" : choices,
            "answer": answer
        })

        # 4. 파일에 저장
        self.custom_path.parent.mkdir(parents=True, exist_ok=True)
        with open(self.custom_path, "w", encoding="utf-8") as f:
            json.dump(custom_data, f, ensure_ascii=False, indent=4)

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