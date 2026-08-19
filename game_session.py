class GameSession:
    def __init__(self, quizzes):
        self.quizzes = quizzes
        self.correct_count = 0
        self.score = 0.0

    def start(self, render_quiz):
        width = 40
        total_quiz_count = len(self.quizzes)

        if not self.quizzes:
            print("현재 풀 수 있는 퀴즈가 없습니다. 퀴즈를 추가해주세요!")
            return

        print(f"퀴즈를 시작합니다! (총 {total_quiz_count} 문제)")
        print("-" * width)

        for quiz in self.quizzes:
            render_quiz(quiz)
            self.run_single_quiz(quiz)

        self.calculate_score(total_quiz_count)
        return self.score
        

    def run_single_quiz(self, quiz):
        while True:
            choice_text = input("정답을 입력하세요 (1-4): ").strip()

            if not choice_text:
                print("정답은 필수로 입력하셔야합니다.")
                continue

            try:
                choice_number = int(choice_text)
            except ValueError:
                print("숫자를 입력해주세요.")
                continue

            if not 1 <= choice_number <= 4:
                print("1부터 4 사이의 숫자를 입력해주세요.")
                continue
            break       

        if quiz.check_answer(choice_number):
            self.correct_count += 1
            print("정답입니다!")
        else:
            print(f"오답입니다! 정답은 {quiz.answer}번입니다.")

    def calculate_score(self, total_quiz_count):
        self.score = (self.correct_count / total_quiz_count) * 100
        self.score = round(self.score, 1)
                  
        return self.score
