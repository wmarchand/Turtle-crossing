from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("black")
        self.score = 1
        self.update_scoreboard()


    def update_scoreboard(self):
        self.goto(-250,230)
        self.write(f"Level: {self.score}", font=FONT)


    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
