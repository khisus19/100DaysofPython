import turtle as t

FONT = ("Courier", 24, "normal")


class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.color("black")
        self.penup()
        self.goto(-280, 265)
        self.hideturtle()
        self.write(f"Level: {self.level}", False, "left", FONT)

    def level_up(self):
        self.leve += 1
    pass
