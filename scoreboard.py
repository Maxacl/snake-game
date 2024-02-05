from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 15, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.color("white")
        self.setposition(x=0, y=275)

    def update_score(self, score=0):
        self.score += 1
        points = self.score
        return self.write(f"SCORE: {points} ", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def starting_score(self, score=0):
        return self.write(f"SCORE: {self.score} ", align=ALIGNMENT, font=FONT)

