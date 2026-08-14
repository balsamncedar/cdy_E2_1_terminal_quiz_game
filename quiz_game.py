# quiz_game.py
from game_session import GameSession


class QuizGame:
    def __init__(self, repository):
        self.repository = repository
        self.width = 40

    def display_menu(self):
        print("=" * self.width)
        print("          [ 나만의 퀴즈 게임 ]           ")
        print("=" * self.width)
        print("    1. 퀴즈 풀기  ")
        print("    2. 퀴즈 추가  ")
        print("    3. 퀴즈 목록  ")
        print("    4. 점수 확인  ")
        print("    5. 종료  ")
        print("=" * self.width)

    def run(self):
        try:
            while True:
                self.display_menu()
                choice = input("1 ~ 5 중 메뉴선택(이외 입력시 다시 선택) : ").strip()

                if choice == "1":
                    print("퀴즈 풀기 선택")
                    self.play_quiz()
                elif choice == "2":
                    print("퀴즈 추가 선택")
                    self.add_quiz()
                elif choice == "3":
                    print("퀴즈 목록 ")
                    self.display_quiz_list()
                elif choice == "4":
                    print("점수 확인 선택")
                    self.check_score()
                elif choice == "5":
                    self.repository.save_state()
                    print("게임을 종료합니다.")
                    break
                else:
                    print("[주의] 잘못된 입력입니다. 1 ~ 5 번 중 선택해주세요. ")

        except (KeyboardInterrupt, EOFError):
            print("\n[안내] 입력이 중단되어 게임을 안전하게 종료합니다.")
            self.repository.save_state()

    def play_quiz(self):
        session = GameSession(self.repository.quizzes)
        final_score = session.start(self.display_quiz)

        if final_score is None:
            return

        print("=" * self.width)
        print(f"결과: {len(session.quizzes)}문제 중 {session.correct_count}문제 정답! ({session.score}점)")

        previous_best = self.repository.best_score
        if previous_best is None or final_score > previous_best:
            self.repository.best_score = final_score
            self.repository.save_state()
            if previous_best is None:
                print(f"첫 기록이 저장되었습니다: {final_score}점")
            else:
                print(f"신기록 달성! 기존 최고점({previous_best}점) -> 새 최고점({final_score}점)")

    def add_quiz(self):
        print(" 새로운 퀴즈를 추가합니다. ")
        while True:
            question = input("문제를 입력하세요: ").strip()
            if not question:
                print("[주의] 질문은 필수값입니다. 다시 입력해주세요.")
                continue
            break

        
        choices = []
        print("4개의 보기(선택지)를 차례대로 입력해주세요.")
        for i in range(1, 5):
            while True:
                choice = input(f"선택지{i}: ").strip()
                if not choice:
                    print("[주의] 보기는 필수값입니다. 다시 입력해주세요.")
                    continue
                choices.append(choice)
                break  

        while True:
            correct_choice_text = input("정답 번호를 입력하세요 (1 ~ 4 중 하나): ").strip()

            if not correct_choice_text:
                print("정답 번호는 필수입니다.")
                continue
            
            try:
                correct_choice_number = int(correct_choice_text)
            except ValueError:
                print("숫자를 입력해주세요")
                continue

            if correct_choice_number < 1 or correct_choice_number > 4 :
                print("1부터 4사이의 숫자를 입력해주세요.")
                continue

            break

        success = self.repository.add_quiz(question, choices, correct_choice_number)

        if success:
            print("퀴즈가 추가되었습니다! ")
        else:
            print("동일한 질문이 있거나 저장에 실패하여 퀴즈를 추가하지 못했습니다.")

    def display_quiz_list(self):
        print("\n [등록된 퀴즈 목록]")
        quizzes = self.repository.quizzes

        if not quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for i, quiz in enumerate(quizzes, start=1):
            print(f"{i}. {quiz.question}")


    def display_quiz(self, quiz):
        for line in quiz.to_lines():
                print(line)

    def check_score(self):
        best_score = self.repository.get_best_score()
        if best_score is None:
            print("아직 퀴즈를 푼 기록이 없습니다.")
        else:
            print(f"현재 최고 점수: {best_score}점")
