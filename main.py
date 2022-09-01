import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
carManager = CarManager()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(player.move, 'Up')

game_is_on = True
while game_is_on:
    time.sleep(player.moveSpeed)
    screen.update()
    carManager.createCar()
    carManager.moveCars()
    for i in carManager.allCars:
        if player.distance(i) < 20:
            scoreboard.gameOver()
            game_is_on = False

    if player.ycor() == 250:
        scoreboard.increaseLevel()

screen.exitonclick()
