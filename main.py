# main.py 
# [실행파일] 프로그램 시작점
from quiz_game import QuizGame
from repository import QuizRepository



def main():
    
    repository = QuizRepository()

    game = QuizGame(repository)

    game.run()

if __name__ == "__main__":
    main()

