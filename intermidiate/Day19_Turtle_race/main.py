from turtle import Turtle, Screen
import random
tim = Turtle(shape="turtle")
sam = Turtle(shape="turtle")
anne = Turtle(shape="turtle")
naan = Turtle(shape="turtle")
bran = Turtle(shape="turtle")
tim.color('red')
anne.color('blue')
bran.color('green')
naan.color('purple')
sam.color('violet')
screen = Screen()






def base(turtle):
    turtle.penup()
    turtle.setheading(155)
    turtle.forward(400)
    turtle.setheading(270)

def set_off(turtle):
        if turtle == tim:
            base(tim)
            tim.setheading(0)
        elif turtle == sam:
            base(sam)
            sam.forward(50)
            sam.setheading(0)
        elif turtle == anne:
            base(anne)
            anne.forward(100)
            anne.setheading(0)
        elif turtle == naan:
            base(naan)
            naan.forward(150)
            naan.setheading(0)
        elif turtle == bran:
            base(bran)
            bran.forward(200)
            bran.setheading(0)
finish_line = 650
point_tim = 0
point_sam = 0
point_anne = 0
point_naan = 0
point_bran = 0

def move(t, p, ):
        rand_amount = random.randint(1, 50)
        t.forward(rand_amount)
        p += rand_amount
        return p


set_off(tim)
set_off(sam)
set_off(anne)
set_off(naan)
set_off(bran)

print("Welcome to the Turtle Race Game!\n")
winner_guess = input("Who do you think will win?\n").lower()
winner = " "
while  True:
    point_tim = move(tim, point_tim)
    point_sam = move(sam, point_sam)
    point_anne = move(anne, point_anne)
    point_naan = move(naan, point_naan)
    point_bran = move(bran, point_bran)
    if point_tim >= finish_line:
        winner = "red"
        break
    elif point_sam >= finish_line:
        winner = "violet"
        break
    elif point_anne >= finish_line:
        winner = "blue"
        break
    elif point_bran >= finish_line:
        winner = "green"
        break
    elif point_naan >= finish_line:
        winner = "purple"
        break

if winner == winner_guess:
    print("You win!")
else:
    print("You lose!")
    print(f"The winner is {winner}")


screen.exitonclick()