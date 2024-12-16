import turtle as t


class Car(t.Turtle):
    def __init__(self, color, ycor):
        super().__init__()
        self.shape("square")
        self.color(color)
        self.shapesize(1, 2)
        self.penup()
        self.goto(310, ycor)
        self.move()

    def move(self):
        new_x = self.xcor() - 5
        self.goto(new_x, self.ycor())
    
