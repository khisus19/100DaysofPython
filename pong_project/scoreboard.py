import turtle as t

ALIGMENT = "center"
FONT = ("Arial", 50, "normal")

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.p1_score = 0
        self.p2_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 220)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.p1_score} : {self.p2_score}", align=ALIGMENT, font=FONT)

    def increase_score(self, player):
        if player == "p1":
            self.clear()
            self.p1_score += 1
        else:
            self.clear()
            self.p2_score += 1
