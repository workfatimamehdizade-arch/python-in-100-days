import turtle
from turtle import Turtle, Screen
import random
rgb_colors = [(235, 234, 231), (234, 229, 232), (236, 35, 108), (221, 231, 237), (145, 28, 66), (230, 237, 232), (239, 75, 35), (7, 148, 95), (220, 171, 45), (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91), (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35)]
tim = Turtle()
tim.penup()
turtle.colormode(255)
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 21

def row():
    for dot_count in range(1, number_of_dots):
        tim.dot(35, random.choice(rgb_colors))
        tim.forward(100)
        if dot_count % 5 == 0:
            tim.setheading(90)
            tim.forward(100)
            tim.setheading(180)
            tim.forward(500)
            tim.setheading(0)

row()


screen = Screen()
Screen().exitonclick()
