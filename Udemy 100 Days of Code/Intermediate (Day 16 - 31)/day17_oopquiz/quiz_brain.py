class QuizBrain:
    def __init__(self, q_list):
        self.q_no = 0
        self.q_list = q_list
        self.score = 0
        
    def still_has_questions(self):
        return self.q_no < len(self.q_list)
    
    def next_question(self):
        current_q = self.q_list[self.q_no]
        self.q_no += 1
        user_answer = input(f"Q.{self.q_no}: {current_q.text} (True/False)? ").lower()
        self.check_answer(user_answer, current_q.answer)
    
    def check_answer(self, user_ans, correct_ans):
        if user_ans == correct_ans.lower():
            print("Correct!")
            self.score += 1
        else:
            print("That's not right.")
            print(f"The correct answer is {correct_ans}")
        print(f"Your current score is: {self.score}/{self.q_no}\n")