class Question:
    def __init__(self, question_text: str, answer: str, question_number: str):
        self.question_text = question_text
        self.answer = answer.lower()
        self.question_number = question_number

    def ask_question(self) -> bool:
        user_answer = input(f"Q{self.question_number}: {self.question_text} (True/False): ").lower()
        if user_answer == self.answer:
            print("You got it right!")
            return True
        else:
            print(f"The correct answer was: {self.answer.title()}")
            return False
