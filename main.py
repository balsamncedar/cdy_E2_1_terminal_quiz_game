# main.py 
# [실행파일] 프로그램 시작점, 메뉴 루프 및 사용자 입력 수집 


# UI 관련 너비 매직넘버 방지용 변수 전역 선언 WIDTH (40으로 고정, 혹시 다른데서도 사용할까봐 전역처리 )
WIDTH = 40

def display_menu():
    print("="*WIDTH)
    print("          🎯 나만의 퀴즈 게임 🎯           ")
    print("="*WIDTH)
    print("    1. 퀴즈 풀기  ")
    print("    2. 퀴즈 추가  ")
    print("    3. 퀴즈 목록  ")
    print("    4. 점수 확인  ")
    print("    5. 종료  ")
    print("="*WIDTH)
    # print("선택 :        ", end="")


def main():
    display_menu()
    choice= input("1 ~ 5 중 메뉴선택(이외 입력시 다시 선택) : ").strip()

    if choice == "1":
        print("퀴즈 풀기 선택")
    elif choice == "2":
        print("퀴즈 추가 선택")
    elif choice == "3":
        print("퀴즈 추가 선택")
    elif choice == "4":
        print("점수 확인 선택")
    elif choice == "5":
        print("프로그램 종료 선택 ")
    else:
        print("⚠️  잘못된 입력입니다. 1 ~ 5 번 중 선택해주세요. ")

if __name__ == "__main__":
    main()

