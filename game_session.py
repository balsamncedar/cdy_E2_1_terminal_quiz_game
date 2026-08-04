import json
from pathlib import Path


class GameSession:
    def __init__(self, gameRepo):
        self.quizzes = gameRepo.quizzes
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


    # 세션 저장
    def save(self):
        pass
            


