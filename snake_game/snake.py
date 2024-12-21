import turtle as t

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.segments_list = []
        self.create_snake()
        self.head = self.segments_list[0]
        
    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_segment = t.Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments_list.append(new_segment)

    def extend(self):
        self.add_segment(self.segments_list[-1].position())

    def move(self):
        for seg_index in range(len(self.segments_list) - 1, 0, -1):
            new_x = self.segments_list[seg_index - 1].xcor()
            new_y = self.segments_list[seg_index - 1].ycor()
            self.segments_list[seg_index].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def reset_snake(self):
        for segment in self.segments_list:
            segment.goto(1000, 1000)
        self.segments_list.clear()
        self.create_snake()
        self.head = self.segments_list[0]


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)