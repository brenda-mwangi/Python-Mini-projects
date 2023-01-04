from data import question_data as data
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        
question = data[0]["text"]
answer = data[0]['answer']

quiz1 = Question(question,answer)        
print(quiz1.question)
