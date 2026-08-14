# repository.py
import json
from pathlib import Path

from quiz import Quiz
from config import SEED_QUIZ_PATH, STATE_PATH


class QuizRepository:
    def __init__(self, seed_path=SEED_QUIZ_PATH, state_path=STATE_PATH):
        self.seed_path = Path(seed_path)
        self.state_path = Path(state_path)
        self.best_score = None
        self.quizzes = []
        self.load_state()

    def load_state(self):
        try:
            if not self.state_path.exists():
                self._restore_defaults("state.json이 없어 기본 퀴즈를 불러옵니다.")
                return

            state_data = self._read_json(self.state_path)
            if not isinstance(state_data, dict):
                raise ValueError("최상위 데이터는 객체여야 합니다.")
            quizzes_data = state_data.get("quizzes")
            best_score = state_data.get("best_score")
            if not isinstance(quizzes_data, list):
                raise ValueError("quizzes는 목록이어야 합니다.")
            if best_score is not None and (
                isinstance(best_score, bool)
                or not isinstance(best_score, (int, float))
                or not 0 <= best_score <= 100
            ):
                raise ValueError("best_score는 0~100의 숫자 또는 null이어야 합니다.")

            self.quizzes = [self._quiz_from_dict(item) for item in quizzes_data]
            self.best_score = best_score
        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            self._restore_defaults(f"state.json을 읽을 수 없습니다: {error}")

    def _restore_defaults(self, message):
        print(f"[안내] {message}")
        try:
            seed_data = self._read_json(self.seed_path)
            if not isinstance(seed_data, list):
                raise ValueError("기본 퀴즈 데이터는 목록이어야 합니다.")
            self.quizzes = [self._quiz_from_dict(item) for item in seed_data]
        except (OSError, json.JSONDecodeError, KeyError, TypeError, ValueError) as error:
            print(f"[안내] 기본 퀴즈도 불러오지 못해 빈 목록으로 시작합니다: {error}")
            self.quizzes = []
        self.best_score = None
        self.save_state()

    @staticmethod
    def _read_json(filepath):
        with filepath.open("r", encoding="utf-8") as file:
            return json.load(file)

    @staticmethod
    def _quiz_from_dict(item):
        if not isinstance(item, dict):
            raise ValueError("퀴즈 항목은 객체여야 합니다.")
        return Quiz(item["question"], item["choices"], item["answer"])


    def add_quiz(self, question, choices, answer):
        for existing_quiz in self.quizzes:
            if existing_quiz.question == question:
                return False

        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        if self.save_state():
            return True
        self.quizzes.pop()
        return False

    def save_state(self):
        state_data = {
            "quizzes": [quiz.to_dict() for quiz in self.quizzes],
            "best_score": self.best_score,
        }
        try:
            self.state_path.parent.mkdir(parents=True, exist_ok=True)
            with self.state_path.open("w", encoding="utf-8") as file:
                json.dump(state_data, file, ensure_ascii=False, indent=4)
            return True
        except OSError as error:
            print(f"[안내] state.json을 저장하지 못했습니다: {error}")
            return False

    def get_best_score(self):
        return self.best_score
