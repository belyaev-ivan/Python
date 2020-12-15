class Car:
    def __init__(self, speed, color, name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'Автомобиль {self.name} поехал ')
        self.show_speed()

    def stop(self):
        print(f'Автомобиль {self.name} остановился ')

    def turn(self, direction):
        if direction == 'left':
            print(f'Автомобиль {self.name} повернул налево' )
        elif direction == 'right':
            print(f'Автомобиль {self.name} повернул направо ')
        elif direction == 'return':
            print(f'Автомобиль {self.name} развернулся ')
    def show_speed(self):
        print(f'Скорость автомобиля равна {self.speed} км/ч')

class TownCar(Car):

    def show_speed(self):
        if self.speed >= 60:
            print('Вы нарушаете скоростной режим!!!')
            print(f'Скорость автомобиля равна {self.speed} км/ч')
        else:
            print(f'Скорость автомобиля равна {self.speed} км/ч')

class SportCar(Car):

    def __init__(self, speed, color, name, is_police = False):
        super().__init__(speed, color, name, is_police)
        self.SportCar()

    def SportCar(self):
        if self.speed <= 100:
            print('Вы ошиблись, спортивный автомобиль не может ехать так медленно!')



class WorkCar(Car):

    def show_speed(self):
        if self.speed >= 40:
            print('Вы нарушаете скоростной режим!!!')
            print(f'Скорость автомобиля равна {self.speed} км/ч')
        else:
            print(f'Скорость автомобиля равна {self.speed} км/ч')

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police = True):
        super().__init__(speed, color, name, is_police)


a = SportCar(120, 'red', 'BMV')
print(a.is_police)
print(a.color)
print(a.name)
a.go()
a.turn('left')
a.turn('right')
a.turn('return')

b = PoliceCar(80, 'blue', 'Audi')
print(b.is_police)
print(b.color)
print(b.name)
b.go()
b.turn('left')
b.turn('right')
b.turn('return')