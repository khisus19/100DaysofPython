from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []

for each_question in question_data:
	my_q = Question(each_question["text"], each_question["answer"])
	question_bank.append(my_q)

quiz = QuizBrain(question_bank)
quiz.next_question()