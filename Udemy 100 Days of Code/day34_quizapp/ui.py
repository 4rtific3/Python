from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class QuizInterface:
    
    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain
        
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        
        self.canvas = Canvas(width=300, height=250, highlightthickness=0)
        self.question_text = self.canvas.create_text(150, 125, text="question", font=FONT, width=275)
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)
        
        self.score_label = Label(text=f"Score: {self.quiz_brain.score}", fg="white", bg=THEME_COLOR)
        self.score_label.grid(column=1, row=0)
        
        true_img = PhotoImage(file="images/true.png")
        self.true_button = Button(image=true_img, highlightthickness=0, command=self.guess_true)
        self.true_button.grid(column=0, row=2)
        
        false_img = PhotoImage(file="images/false.png")
        self.false_button = Button(image=false_img, highlightthickness=0, command=self.guess_false)
        self.false_button.grid(column=1, row=2)
        
        self.get_next_question()
        
        self.window.mainloop()
    
    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have reached the end of the quiz")
            self.true_button.config(state="disabled")
            self.false_button.config(state="disabled")
    
    def guess_true(self):
        is_correct = self.quiz_brain.check_answer("true")
        self.give_feedback(is_correct)
    
    def guess_false(self):
        is_correct = self.quiz_brain.check_answer("false")
        self.give_feedback(is_correct)
    
    def give_feedback(self, is_correct):
        if is_correct:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
        self.score_label["text"] = f"Score: {self.quiz_brain.score}"