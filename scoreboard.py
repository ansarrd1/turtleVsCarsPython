from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.goto(-180, 250)
        self.hideturtle()
        self.level = 1
        self.updateScore()

    def updateScore(self):
        self.clear()
        self.write(f"Level: {self.level}", align='center', font=FONT)

    def increaseLevel(self):
        self.level += 1
        self.updateScore()

    def gameOver(self):
        self.goto(0, 0)
        self.write("Game Over.", align='center', font=FONT)
