from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Comic Sans MS", 16, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            stored_high_score = data.read()
            self.high_score = int(stored_high_score)
        self.score = 0
        self.pu()
        self.hideturtle()
        self.color("white")
        self.goto(0, 260)
        self.update_scoreboard()
        
    
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
    
    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
    
    def reset(self): 
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()