import time
from turtle import Screen
from player import Player
from car_manager import CarManager

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

from scoreboard import Scoreboard
car_manager = CarManager()
player = Player()
screen.listen()
score_board = Scoreboard()
screen.onkey(player.move_up, "Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.create_car()
    car_manager.move_cars()

    # DETECT COLLISION WITH CARS
    for car in car_manager.all_cars:
        if player.distance(car) < 25 and player.xcor() < 300:
            game_is_on = False
            score_board.game_over()
    # DETECT COLLISION WITH WALL
    if player.is_at_finish():
        player.go_to_starting_position()
        car_manager.level_up()
        score_board.increase_score()

screen.exitonclick()