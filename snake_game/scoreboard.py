import turtle as t

ALIGMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(t.Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 290)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} Highscore: {self.highscore}", align=ALIGMENT, font=FONT)

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()