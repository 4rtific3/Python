from data import question_data as q_data
from question_model import Question
from quiz_brain import QuizBrain

q_bank = []

for i in q_data:
    question = Question(i["question"], i["correct_answer"])
    q_bank.append(question)

quiz = QuizBrain(q_bank)

while quiz.still_has_questions():
    answer = quiz.next_question()

print("You've completed the quiz!")
print(f"Your final score is: {quiz.score}/{quiz.q_no}")