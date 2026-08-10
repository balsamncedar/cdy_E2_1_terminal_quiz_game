from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent


# 저장 위치 변경(루트에있어야함) 
SEED_QUIZ_PATH = BASE_DIR / "data" / "seed_quizzes.json"
CUSTOM_QUIZ_PATH = BASE_DIR / "data" / "custom_quizzes.json"
STATE_PATH = BASE_DIR / "state.json"