from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent

# 기본 퀴즈는 읽기 전용 시드로, 실제 게임 상태는 프로젝트 루트에 저장한다.
SEED_QUIZ_PATH = BASE_DIR / "data" / "seed_quizzes.json"
STATE_PATH = BASE_DIR / "state.json"
