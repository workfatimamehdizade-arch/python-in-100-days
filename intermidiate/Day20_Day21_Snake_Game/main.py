from turtle import Screen
from food import Food
from snake import Snake
import time
from scoreboard import  Scoreboard
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()
screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    #DETECT COLLISION WITH FOOD
    if snake.head.distance(food) < 15:
        food.refresh()
        scoreboard.increase_score()
        snake.extend_snake()

    #DETECT COLLISION WITH WALL
    if snake.head.xcor() >280 or snake.head.xcor()< -280 or snake.head.ycor() > 280 or snake.head.ycor() <- 280:
        snake.reset()
        scoreboard.reset()

    #DETECT COLLISION WITH WALL
    #IF COLLIDE WITH ANY PART OF SNAKE BUT HEAD
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            snake.reset()
            scoreboard.reset()

screen.exitonclick()