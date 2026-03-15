from turtle import Turtle,Screen

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.speed("fastest")
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(1,5)
        self.setheading(90)
        self.goto(x,y)
    def up(self):
        self.setheading(90)
        self.forward(20)
    def down(self):
        self.setheading(270)
        self.forward(20)
