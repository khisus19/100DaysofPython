import turtle as t

class State:
    def __init__(self, name, x_pos, y_pos):
        self.name = name
        self.x_pos = x_pos
        self.y_pos = y_pos
        self.create_new_state()

    def create_new_state(self):
        state = t.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(self.x_pos, self.y_pos)
        state.write(self.name, "center")

        