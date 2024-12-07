import turtle as t

SCREEN_SIZE = 300
WALL_LIMITS = SCREEN_SIZE - 20

class Walls(t.Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(- WALL_LIMITS, 270)
        self.pendown()
        self.goto(WALL_LIMITS, 270)
        self.goto(WALL_LIMITS, -WALL_LIMITS)
        self.goto(-WALL_LIMITS, -WALL_LIMITS)
        self.goto(-WALL_LIMITS, 270)