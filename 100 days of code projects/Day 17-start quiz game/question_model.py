from data import question_data as data
class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer
        
question_bank = []
for question in data:
    question_text=question['text']
    question_answer=question['answer']
    new_quest = Question(question_text,question_answer)
    question_bank.append(new_quest)

print(question_bank)
