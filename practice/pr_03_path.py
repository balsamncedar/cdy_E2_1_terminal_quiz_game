# pr_03_path.py 
# 경로 확인 및 설정 
from pathlib import Path

# 1. 현재 이 파일이 있는 폴더의 절대 경로 동적으로 구함.
BASE_DIR = Path(__file__).resolve().parent

# 2. BASE_DIR 경로를 기준으로 state.json 파일 경로를 설정 
# DATA_FILE = BASE_DIR / "state.json"


# 변수를 함께 섞어서 프린트하는 법(문자열 포매팅)
# f" {변수명}"  : f-string 방식

print(f"현재 프로젝트 절대 경로 : {BASE_DIR}")
# print(f"데이터 파일 경로 : {DATA_FILE}")

# 그냥 일반으로 출력
print("현재 프로젝트 절대경로2 : ", BASE_DIR)