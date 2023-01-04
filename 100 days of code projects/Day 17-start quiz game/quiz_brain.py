class QuizBrain:
    def __init__(self, question_list):
        self.number= 0
        self.question_list=question_list
        self.score = 0

    
    def still_has_questions(self):
        num_of_questions = len(self.question_list)
        return self.number< num_of_questions

 
    def next_question(self):
        current_question=self.question_list[self.number]
        user_answer = input(f"Q.{self.number+1}: {current_question.question} (True/False)?: ")
        self.number+=1
        self.check_answer(user_answer, current_question.answer)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("Correct!")
            self.score+=1
            
            
        else:
            print("That's wrong.")
            print(f"The correct answer is : {correct_answer}")
        print(f"Your current score is {self.score}/{self.number}\n")