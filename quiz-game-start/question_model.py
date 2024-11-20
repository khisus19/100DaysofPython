class Question:
	def __init__(self, text, answer):
		self.text = text
		self.answer = answer

my_first_q = Question("Are you a python programmer", "True")

print(my_first_q.text)
print(my_first_q.answer)