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
    def display_quiz(self):
        print(f"Q. {self.question}")
        for choice in self.choices:
            print(choice)
        # print(f"정답 : {self.answer}.{self.choices[int(self.answer) - 1][1:]}")



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
    
    base_quizzes = [

        Quiz(
            question = "루이스 해밀턴(Lewis Hamilton)이 오랜 기간 몸담았던 메르세데스를 떠나, 2025시즌부터 새롭게 둥지를 튼 팀은 어디일까요?", 
            choices = ["① 레드불 레이싱 (Red Bull Racing)", "② 스쿠데리아 페라리 (Scuderia Ferrari)", "③ 맥라렌 (McLaren)", "④ 애스턴 마틴 (Aston Martin)"],
            answer = "2"
        ),

        Quiz(
                question = "2024년 사우디아라비아 그랑프리에서 맹장염으로 출전하지 못한 카를로스 사인츠를 대신해 페라리 머신을 몰고 전격 데뷔하여 포인트(7위)를 획득한 영건 드라이버는 누구일까요?", 
                choices = ["① 안드레아 키미 안토넬리 (Andrea Kimi Antonelli)", "② 올리버 베어맨 (Oliver Bearman)", "③ 프랑코 콜라핀토 (Franco Colapinto)", "④ 리암 로슨 (Liam Lawson)"],
                answer = "2"
        ),

        Quiz(
                question = "독일의 프리미엄 자동차 브랜드 아우디(Audi)가 독자 파워유닛 개발 및 F1 진입을 위해 인수를 진행하고 전면적인 워크스 팀 체제로 참가를 준비해 온 기존 팀은 어디일까요?", 
                choices = ["① 윌리엄스 (Williams)", "② 하스 (Haas)", "③ 자우버 (Sauber)", "④ 알파타우리 (현 VCARB)"],
                answer = "3"
        ),

        Quiz(
                question = "막스 페르스타펜(Max Verstappen)이 세운 F1 역사상 단일 시즌 최다 연승 기록은 몇 연승일까요?", 
                choices = ["① 8연승", "② 10연승", "③ 12연승", "④ 15연승"],
                answer = "2"
        ),

        Quiz(
                question = "화려한 네온사인과 라스베이거스 스트립(The Strip) 대도를 질주하며 F1 캘린더에 새롭게 합류한 메이저 나이트 레이스의 공식 명칭은 무엇일까요?", 
                choices = ["① 라스베이거스 그랑프리 (Las Vegas Grand Prix)", "② 네바다 스트리트 그랑프리 (Nevada Street GP)", "③ 마이애미 그랑프리 (Miami Grand Prix)", "④ 아메리카 그랑프리 (Americas GP)"],
                answer = "1"
        ),
    ]


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
    quiz_1.display_quiz()

    
    print(f"\n======== 정답확인 ==========")
    print(quiz_1.check_answer(2))
    print(quiz_1.check_answer(3))


    # print(f"===== 전체 기본 퀴즈 데이터셋 출력 ==")
    # for i in range(5):
    #     quiz_{i+1}.display_quiz()


    print("\n========= 전체 베이스 퀴즈 출력 ======")
    for i, quiz in enumerate(base_quizzes, 1):
        print(f"======= [퀴즈 {i}] 출력 ======")
        quiz.display_quiz()
        print()