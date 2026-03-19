from turtle import Turtle

FONT = ("Courier", 24, "bold")
ALIGNMENT = "center"

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.update_score()


    def update_score(self):
        self.clear()
        self.goto(0, 250)
        self.write(f"Score: {self.score}", align= ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.update_score()
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!", align= ALIGNMENT, font=FONT)



