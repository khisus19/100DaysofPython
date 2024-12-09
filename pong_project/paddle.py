import turtle as t

PADDLE_YCORDS = [30, 10, 0, -10, -30]
RIGHT_SIDE_PADDLE = 350

class Paddle(t.Turtle):
    def __init__(self, side):
        super().__init__()
        self.side = side
        self.paddle = {}
        self.create_paddle()

    def create_paddle(self):    
        paddle = t.Turtle("square")
        paddle.color("white")
        paddle.shapesize(5, 1)
        paddle.penup()
        paddle.setpos(self.side, 0)
        self.paddle = paddle

    def move_up(self):
        self.paddle.sety(self.paddle.ycor() + 20)

    
    def move_down(self):
        self.paddle.sety(self.paddle.ycor() - 20)
    
    