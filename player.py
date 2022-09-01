from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.color('black')
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.moveSpeed = 0.1

    def move(self):
        self.forward(MOVE_DISTANCE)
        if self.isFinishLine():
            self.goBack()

    def goBack(self):
        self.goto(STARTING_POSITION)
        self.moveSpeed *= 0.8

    def isFinishLine(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
