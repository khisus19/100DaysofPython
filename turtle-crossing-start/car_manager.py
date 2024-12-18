import random
import turtle as t


COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5
START_FREQUENCY = 6


class CarManager():
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE
        self.car_frequency = START_FREQUENCY

    def create_car(self):
        random_chance = random.randint(1, self.car_frequency)
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
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT
        if self.car_frequency > 3:
            self.car_frequency -= 1
        
