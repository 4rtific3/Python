from turtle import Turtle
STARTING_COOR = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        self.head = self.snake_body[0]
        
    def create_snake(self):
        for i in STARTING_COOR:
            self.add_segment(i)
            
    def add_segment(self, STARTING_COOR):
        snake = Turtle(shape="square")
        snake.pu()
        snake.color("white")
        snake.goto(STARTING_COOR)
        self.snake_body.append(snake)
    
    def extend(self):
        self.add_segment(self.snake_body[-1].position())
            
    def move(self):
        for seg_num in range(len(self.snake_body)-1,0,-1):
            new_x = self.snake_body[seg_num-1].xcor()
            new_y = self.snake_body[seg_num-1].ycor()
            self.snake_body[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DIST)
    
    def reset(self):
        for segment in self.snake_body:
            segment.hideturtle()
        self.snake_body.clear()
        self.create_snake()
        self.head = self.snake_body[0]
    
    def up(self):
        if self.head.heading() != DOWN:
            self.head.seth(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.seth(DOWN)
        
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.seth(LEFT)
        
    def right(self):
        if self.head.heading() != LEFT:
            self.head.seth(RIGHT)