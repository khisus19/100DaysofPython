import turtle as t

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 275)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 14, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Arial", 14, "normal"))