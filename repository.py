# repository.py
import json
from pathlib import Path
import os

from quiz import Quiz
from config import STATE_PATH


class QuizRepository:
    def __init__(self,  state_path=STATE_PATH):
        # self.seed_path = Path(seed_path)
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
            # seed_data = self._read_json(self.seed_path)
            seed_data = [
                {
                    "question" : "루이스 해밀턴(Lewis Hamilton)이 오랜 기간 몸담았던 메르세데스를 떠나, 2025시즌부터 새롭게 둥지를 튼 팀은 어디일까요?", 
                    "choices" : ["레드불 레이싱 (Red Bull Racing)", "스쿠데리아 페라리 (Scuderia Ferrari)", "맥라렌 (McLaren)", "애스턴 마틴 (Aston Martin)"],
                    "answer" : 2
                },

                {
                        "question" : "2024년 사우디아라비아 그랑프리에서 맹장염으로 출전하지 못한 카를로스 사인츠를 대신해 페라리 머신을 몰고 전격 데뷔하여 포인트(7위)를 획득한 영건 드라이버는 누구일까요?", 
                        "choices" : ["안드레아 키미 안토넬리 (Andrea Kimi Antonelli)", "올리버 베어맨 (Oliver Bearman)", "프랑코 콜라핀토 (Franco Colapinto)", "리암 로슨 (Liam Lawson)"],
                        "answer" : 2
                },  

                {
                        "question" : "독일의 프리미엄 자동차 브랜드 아우디(Audi)가 독자 파워유닛 개발 및 F1 진입을 위해 인수를 진행하고 전면적인 워크스 팀 체제로 참가를 준비해 온 기존 팀은 어디일까요?", 
                        "choices" : ["윌리엄스 (Williams)", "하스 (Haas)", "자우버 (Sauber)", "알파타우리 (현 VCARB)"],
                        "answer" : 3
                },

                {
                        "question" : "막스 페르스타펜(Max Verstappen)이 세운 F1 역사상 단일 시즌 최다 연승 기록은 몇 연승일까요?", 
                        "choices" : ["8연승", "10연승", "12연승", "15연승"],
                        "answer" : 2
                },

                {
                        "question" : "화려한 네온사인과 라스베이거스 스트립(The Strip) 대도를 질주하며 F1 캘린더에 새롭게 합류한 메이저 나이트 레이스의 공식 명칭은 무엇일까요?", 
                        "choices" : ["라스베이거스 그랑프리 (Las Vegas Grand Prix)", "네바다 스트리트 그랑프리 (Nevada Street GP)", "마이애미 그랑프리 (Miami Grand Prix)", "아메리카 그랑프리 (Americas GP)"],
                        "answer" : 1
                }       
            ]

            if not isinstance(seed_data, list):
                print("just check if it's working -- ")
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

        temp_path = self.state_path.with_suffix(".tmp")

        try:
            self.state_path.parent.mkdir(parents=True, exist_ok=True)

            with temp_path.open("w", encoding="utf-8") as file:
                json.dump(state_data, file, ensure_ascii=False, indent=4)

            os.replace(temp_path, self.state_path)
            return True
        
        except OSError as error:
            print(f"[안내] state.json을 저장하지 못했습니다: {error}")

            try : 
                if temp_path.exist():
                    temp_path.unlink()
            except:
                pass

            return False

    def get_best_score(self):
        return self.best_score
