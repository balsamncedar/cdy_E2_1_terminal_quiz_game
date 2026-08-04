
# quiz_game.py
from game_session import GameSession

class QuizGame:
    def __init__(self, repository):
        self.repository = repository
        self.WIDTH = 40

    def display_menu(self):
        print("="* self.WIDTH )
        print("          🎯 나만의 퀴즈 게임 🎯           ")
        print("="* self.WIDTH )
        print("    1. 퀴즈 풀기  ")
        print("    2. 퀴즈 추가  ")
        print("    3. 퀴즈 목록  ")
        print("    4. 점수 확인  ")
        print("    5. 종료  ")
        print("="* self.WIDTH )
        # print("선택 :        ", end="")


         
    def run(self):
        try:
            while True:
                self.display_menu()
                choice= input("1 ~ 5 중 메뉴선택(이외 입력시 다시 선택) : ").strip()
    
                if choice == "1":
                    print("퀴즈 풀기 선택")
                elif choice == "2":
                    print("퀴즈 추가 선택")
                    break;
                elif choice == "3":
                    print("퀴즈 추가 선택")
                    break;
                elif choice == "4":
                    print("점수 확인 선택")
                    break;
                elif choice == "5":
                    print("프로그램 종료 선택 ")
                    break;
                else:
                    print("⚠️  잘못된 입력입니다. 1 ~ 5 번 중 선택해주세요. ")

        except KeyboardInterrupt:
            print("\nCtrl + C 입력, 메인 메뉴 프로그램 종료. ")

    def play_quiz(self):
        session = GameSession(self.repository)
        final_score = session.start()

        if final_score is None:
            return 

        if final_score > self.repository.best_score:
            print(f"🎉 신기록 달성! 기존 최고점({self.repository.best_score}점 )")


    def add_quiz(self):
        print(" 📌 새로운 퀴즈를 추가합니다. ")
        question = input("문제를 입력하세요: ").strip()
        print(f"{question}")
        if not question : 
            print("⚠️ 질문은 필수값입니다. 메인 메뉴로 돌아갑니다.")
            return

        choices = []
        print("👉 4개의 보기(선택지)를 차례대로 입력해주세요.")
        for i in range(1,5):
            choice = input(f"선택지{i}: {choices[i - 1]}")
            if not choice:
                print("⚠️ 보기는 필수값입니다. 취소합니다.")
                return
            choices.append(choice)

        answer = input("🎯 정답 번호를 입력하세요 (1 ~ 4 중 하나): ").strip()
        if answer not in ["1", "2", "3", "4"]:
            print("⚠️ 정답은 1부터 4 사이의 숫자여야 합니다. 취소합니다.")
            return

        success = self.repository.add_custom_quiz(question, choices, answer)

        if success:
            print(" ✅ 퀴즈가 추가되었습니다! ")
        else :
            print("❌ 퀴즈 추가에 실패했습니다.")
        
        