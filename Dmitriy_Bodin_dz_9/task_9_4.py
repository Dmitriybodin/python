# Task 4

class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} is going!')

    def stop(self):
        print(f'{self.name} is stopping!')

    def turn(self, direction):
        print(f'{self.name} is turning to {direction}!')

    def show_speed(self):
        print('Current speed:', self.speed)


class TownCar(Car):
    def show_speed(self):
        print('Current speed:', self.speed)
        if self.speed > 60:
            print('Speeding!')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        print('Current speed:', self.speed)
        if self.speed > 40:
            print('Speeding!')


class PoliceCar(Car):
    pass


sport_car = SportCar(180, 'black', 'Sport car', False)
town_car = TownCar(70, 'blue', 'Town Car', False)
work_car = WorkCar(50, 'red', 'Work Car', False)
police_car = PoliceCar(120, 'white', 'Police Car', True)

sport_car.show_speed()
town_car.show_speed()
work_car.show_speed()
police_car.show_speed()
town_car.go()
town_car.stop()
town_car.turn('left')
