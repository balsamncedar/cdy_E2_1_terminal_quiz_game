# main.py 
# [실행파일] 프로그램 시작점
import sys

from quiz_game import QuizGame
from repository import QuizRepository


try:
    if sys.platform.startswith("win"):
        sys.stdin.reconfigure(encoding="utf-8")
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
except (AttributeError, ValueError):
    pass


def main():
    repository = QuizRepository()
    game = QuizGame(repository)
    game.run()


if __name__ == "__main__":
    main()

