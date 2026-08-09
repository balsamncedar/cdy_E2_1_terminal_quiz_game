import json
from pathlib import Path


class GameSession:
    def __init__(self, quizzes):
        self.quizzes = quizzes
        self.correct_count = 0
        self.score = 0.0

    # main.py 에 남아있는거 가져와서 향후 추가
    def start(self, render_quiz):
        WIDTH = 40
        #  갯수 확인 추가해야함 
        total_quiz_count = len(self.quizzes)

        # 기본 data 넣어주면 걸릴일 없긴함. 처리해야할듯.
        if not self.quizzes:
            print("현재 풀 수 있는 퀴즈가 없습니다. 퀴즈를 추가해주세요!")
            return

        print(f"퀴즈를 시작합니다! (총 {total_quiz_count} 문제)")
        print("-"* WIDTH)

        for quiz in self.quizzes:
            render_quiz(quiz)
            self.run_single_quiz(quiz)

        self.calculate_score(total_quiz_count)
        return self.score
        

    def run_single_quiz(self, quiz):
        user_input = input("정답을 입력하세요: ").strip()

        if quiz.check_answer(user_input) :
            self.correct_count += 1 

    def calculate_score(self, total_quiz_count):
        self.score = (self.correct_count / total_quiz_count) * 100
        self.score = round(self.score, 1)
                  
        return self.score