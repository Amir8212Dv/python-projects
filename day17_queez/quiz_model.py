from question_model import Question
from data import question_data
import random


class Quiz:
    def __init__(self):
        self.questions = []
        self.score = 0
        self.create_questions()

    def create_questions(self):
        """Create's questions objects with question data"""

        random.shuffle(question_data)
        for i in range(len(question_data)):
            question = question_data[i]
            self.questions.append(Question(question["text"], question["answer"], i + 1))

    def start_quiz(self) -> int:
        """Start's to asking questions and returns the final result"""

        for i in range(len(self.questions)):
            result = self.questions[i].ask_question()
            self.score += int(result)
            print(f"Your current score is: {self.score}/{i + 1}\n")

        return f"{self.score}/{len(self.questions)}"
