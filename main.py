from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []

for keys in question_data:
    question = Question(keys["question"], keys["correct_answer"])
    question_bank.append(question)

quiz1 = QuizBrain(question_bank)

while quiz1.still_has_question():
    quiz1.next_question()

print("You've completed the quiz!")
print(f"Your final score was {quiz1.score}/{len(quiz1.question_list)}, you got {((quiz1.score/12)*100):.2f}%")