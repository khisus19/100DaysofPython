import turtle as t

class Snake:
    def __init__(self):
        self.segments_list = []

        starting_positions = [(0, 0), (-20, 0), (-40, 0)]

        for position in starting_positions:
            new_segment = t.Turtle("square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments_list.append(new_segment)

    def move(self):
        for seg_index in range(len(self.segments_list) - 1, 0, -1):
            new_x = self.segments_list[seg_index - 1].xcor()
            new_y = self.segments_list[seg_index - 1].ycor()
            self.segments_list[seg_index].goto(new_x, new_y)

        self.segments_list[0].forward(20)