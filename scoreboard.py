from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 16, 'normal')


class Scoreboard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.penup()
        self.pencolor("white")
        self.goto(x=0, y=270)
        self.print_score()

    def print_score(self):
        self.write(f"score: {self.score}", align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.clear()
        self.score += 1
        self.print_score()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)