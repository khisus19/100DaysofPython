import turtle as t

class Paddle(t.Turtle):
    def __init__(self, side):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.setpos(side, 0)

    def move_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    
    def move_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
    
    