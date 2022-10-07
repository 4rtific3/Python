from turtle import Turtle

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.pu()
        self.hideturtle()
        self.color("white")
        self.update_scores()
        
    def p1_point(self):
        self.p1_score += 1
        self.update_scores()
    
    def p2_point(self):
        self.p2_score += 1
        self.update_scores()
        
    def update_scores(self):
        self.clear()
        self.goto(-100, 180)
        self.write(self.p1_score, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 180)
        self.write(self.p2_score, align="center", font=("Courier", 80, "normal"))