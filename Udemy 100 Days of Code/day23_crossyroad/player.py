from turtle import Turtle

STARTING_POS = (0, -280)
MOVE_DIST = 10
FINISH_LINE = 280

class Player(Turtle):
    
    def __init__(self):
        super().__init__()
        self.pu()
        self.seth(90)
        self.shape("turtle")
        self.reset_pos()
    
    def move(self):
        self.forward(MOVE_DIST)
    
    def is_at_finish(self):
        if self.ycor() > FINISH_LINE:
            return True
        else:
            return False
    
    def reset_pos(self):
        self.goto(STARTING_POS)