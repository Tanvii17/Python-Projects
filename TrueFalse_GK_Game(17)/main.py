from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for que in question_data:
    question_text = que["question"]
    question_answer = que["correct_answer"]
    new_question = Question(question_text,question_answer)
    question_bank.append(new_question)


Quiz = QuizBrain(question_bank)

while Quiz.still_has_questions():
    Quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is : {Quiz.score}/{len(question_bank)}")