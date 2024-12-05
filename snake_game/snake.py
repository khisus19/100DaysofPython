import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20

class Snake:
    def __init__(self):
        self.segments_list = []
        self.create_snake()
        self.head = self.segments_list[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
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

        self.head.forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)