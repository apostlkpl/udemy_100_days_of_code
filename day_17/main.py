from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Create the question bank
question_bank = []
for question in question_data:
    question_bank.append(Question(question["text"], question["answer"]))

# Start the quiz
quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

# Final score
print("You \'ve completed the quiz.")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")
