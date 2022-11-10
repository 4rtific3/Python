from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.pu()
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.goto(position)

    def p1_up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)
    
    def p1_down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)
        
    def p2_up(self):
        new_ycor = self.ycor() + 20
        self.goto(self.xcor(), new_ycor)
    
    def p2_down(self):
        new_ycor = self.ycor() - 20
        self.goto(self.xcor(), new_ycor)