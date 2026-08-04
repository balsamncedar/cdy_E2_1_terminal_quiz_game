import json
from pathlib import Path


class GameSession:
    def __init__(self, gameRepo):
        self.quizzes = gameRepo.quizzes
        self.correct_count = 0
        self.score = 0

    # main.py 에 남아있는거 가져와서 향후 추가
    def start(self):
        if not self.quizzes:
            print("현재 풀 수 있는 퀴즈가 없습니다. 퀴즈를 추가해주세요!")
            return

        WIDTH = 40
        #  갯수 확인 추가해야함 
        total_quiz_count = len(self.quizzes)
        print(f"📝 퀴즈를 시작합니다! (총 {total_quiz_count} 문제)")
        print("-"* WIDTH)

        for i, quiz in enumerate(self.quizzezs, 1):
            print(f"[문제 {i}]")
            quiz.display_quiz()

            user_input = input("정답 입력: ").strip()
            if quiz.check_answer(user_input):
                self.correct_count += 1

        self.score = (self.correct_count / total_quiz_count) * 100

        self.score = round(self.score, 1)


   
        print("="* WIDTH)
        print(f"결과: {total_quiz_count} 중 {self.correct_count} 정답! ({self.score})점")

        return self.score


