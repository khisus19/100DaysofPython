import turtle as t

class Ball(t.Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.setheading(130)
        self.penup()

    def move(self):
        if self.xcor() < 380 or self.xcor() > -380:
            self.forward(10)

    def bounce(self):
        new_angle = 360 - self.heading()
        self.setheading(new_angle)