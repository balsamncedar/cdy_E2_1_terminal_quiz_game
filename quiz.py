class Quiz:
    def __init__(self, question, choices, answer):
        if not isinstance(question, str) or not question.strip():
            raise ValueError("질문은 비어 있지 않은 문자열이어야 합니다.")
        if not isinstance(choices, list) or len(choices) != 4:
            raise ValueError("선택지는 반드시 4개여야 합니다.")
        if not all(isinstance(choice, str) and choice.strip() for choice in choices):
            raise ValueError("모든 선택지는 비어 있지 않은 문자열이어야 합니다.")
        if not isinstance(answer, int):
            raise TypeError("정답은 정수(int)여야 합니다.")
        if not 1 <= answer <= 4:
            raise ValueError("정답은 1부터 4 사이여야 합니다.")

        self.question = question.strip()
        self.choices = [choice.strip() for choice in choices]
        self.answer = answer

    # 정답 확인
    def check_answer(self, choice_number):
        return self.answer == choice_number

    def to_lines(self):
        lines = [f"Q. {self.question}"]
        for idx, choice in enumerate(self.choices, start=1):
            lines.append(f"{idx}. {choice}")
        return lines

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
        }
