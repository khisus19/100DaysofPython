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
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", False, "left", FONT)
   
    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", False, "center", FONT)
        
