# repository.py
import json
from pathlib import Path
from quiz import Quiz

class QuizRepository:
    def __init__(self, seed_path="data/seed_quizzes.json", custom_path="data/custom_quizzes.json"):
        self.seed_path = Path(seed_path)
        self.custom_path = Path(custom_path)
        self.quizzes = []
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

        
    