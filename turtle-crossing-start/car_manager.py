import random
import turtle as t


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    def __init__(self):
        self.all_cars = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = t.Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(1, 2)
            new_car.penup()
            lane = random.choice(range(-240, 241, 20))
            new_car.goto(310, lane)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)
        
