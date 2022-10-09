from turtle import Turtle

FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.pu()
        self.goto(-220, 250)
        self.update_score()
    
    def level_up(self):
        self.level += 1
        self.update_score()
    
    def update_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)
    
    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)