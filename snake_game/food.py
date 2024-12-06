import random

import turtle as t

POSSIBLE_COORDENATES = range(-280, 280, 20)

class Food(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        xcor = random.choice(POSSIBLE_COORDENATES)
        ycor = random.choice(POSSIBLE_COORDENATES)
        self.goto(xcor, ycor)