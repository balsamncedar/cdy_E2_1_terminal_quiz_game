# quiz.py
# 개별 퀴즈 모델 (Quiz 클래스)
class Quiz:
    def __init__(self, question, choices, answer):
        # 1. 질문이 문자열인지 검증
        if not isinstance(question, str):
            raise TypeError("질문은 문자열(str)이어야 합니다. ")

        # 2. 선택지 리스트 형식 및 4개 인지 확인 (일단 4지선다만)
        if not isinstance(choices, list) or len(choices) != 4:
            raise TypeError("선택지(choices)는 반드시 4개의 아이템을 가진 리스트여야합니다. ")

        # 3. 정답 형식 검증 ( 일단 지금은 비어있는것 정도만. 숫자일지문자열일지는 추후)
        if not str(answer).strip():
            raise ValueError("정답은 비어있을 수 없습니다. ")

        # 검증 통과 후 저장
        self.question  = question
        self.choices = choices
        self.answer = answer

    # 정답 확인
    def check_answer(self, user_input):
        user_answer = str(user_input).strip()
        correct_answer = str(self.answer).strip()

        correct = user_answer == correct_answer
        result_msg = "👌 정답!" if correct else "❌ 땡!"
        print(result_msg)

        return correct

    # 퀴즈 출력  
    def print_quiz(self):
        print(f"Q. {self.question}")
        for choice in self.choices:
            print(choice)
        print(f"정답 : {self.answer}.{self.choices[int(self.answer) - 1][1:]}")

    # 개발 확인용
    def __str__(self):
        return f"<Quiz 객체> : {self.question}"


# === 테스트 실행부 ===
if __name__ == "__main__":
    # 인스턴스 찍기 (개별 퀴즈 만들기)
    quiz_1 = Quiz(
        question = "루이스 해밀턴(Lewis Hamilton)이 오랜 기간 몸담았던 메르세데스를 떠나, 2025시즌부터 새롭게 둥지를 튼 팀은 어디일까요?", 
        choices = ["① 레드불 레이싱 (Red Bull Racing)", "② 스쿠데리아 페라리 (Scuderia Ferrari)", "③ 맥라렌 (McLaren)", "④ 애스턴 마틴 (Aston Martin)"],
        answer = "2"
    )

    # 퀴즈 출력
    # 0. print() 사용시
    # __str__ 없을 경우 :  주솟값 찍힘. (Default String Representation)  / 예시) <__main__.Quiz object at 0x0000023F966CCB10>
    # __str__ 정의 : 개발자 확인용으로 진행. (read-only 만 권장 / 추후 삭제 검토 )
    print(f"\n========= print() 함수 활용시 ======================")
    print(quiz_1)


    # 1.
    # print(f"==== print_quiz() 함수 사용 퀴즈 출력 ======")
    # print_quiz(quiz_1)

    # 2.
    print(f"\n==== print_quiz() 메서드 사용 퀴즈 출력 ======")
    quiz_1.print_quiz()

    
    print(f"\n======== 정답확인 ==========")
    print(quiz_1.check_answer(2))
    print(quiz_1.check_answer(3))