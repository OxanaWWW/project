#1****************************8
from time import sleep


class Trafficlight:
    colors = ('red', 'yellow', 'green')
    delay = (7, 2, 5)
     # 7, 2, 5 - time glow by sec

    def __init__(self):
        self.__color = 'green'

    def running(self):
        while True:
            for i in self.colors:
                self.__colors = i
                print(self.__colors)
                sleep(self.delay[self.colors.index(self.__colors)])


traffic_licht = Trafficlight()
traffic_licht.running()

#2************************

class Road:
    def __init__(self, lenght, width):
        self._lenght = lenght
        self._width = width

    def get_weight(self, spec_grav, thick):
        # spec_grav - massa asphalt thickness by 1 m/2
        # thick - thicness
        return self._lenght * self._width * spec_grav * thick / 1000


r = Road(5000, 20)
print(r.get_weight(25, 5))

#3**********************

class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self. position = position
        self._income = {'wage': wage, 'bonus': bonus}


class Position(Worker):

    def get_full_name(self):
        return '{0} {1}'. format(self. name, self.surname)

    def get_total_income(self):
        return  self._income['wage'] + self._income['bonus']

    # for example
employee = Position('Tom','Ridd', 'developer', 4000, 5000)
print(employee.name)
print(employee.surname)
print(employee._income)
print(employee.get_full_name())
print(employee.get_total_income())


#4********************

class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print('Go')

    def stop(self):
        print('stop')

    def turn(self, direction):
        print(f'car turned to {direction}')

    def show_speed(self):
        print(f'current speed is {self.speed}')


class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        #Car.show_speed(self)
        if self.speed > 60:
            print('reduce speed')


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print('reduce speed')


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


town = TownCar(90, 'green', 'Town')
sport = SportCar(120, 'red', 'Sport')
work = WorkCar(41, 'yellow', 'Work')
police = PoliceCar(100, 'blue', 'Police')

town.show_speed()
work.show_speed()

work.speed = 30
work.show_speed()

police.turn('left')

#5*************************

class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('start drawing')


class Pen(Stationery):
    def draw(self):
        print(f'drawing with pen {self.title}')


class Pencil(Stationery):
    def draw(self):
        print(f'start drawing with pencil {self.title}')


class Handle(Stationery):
    def draw(self):
        print(f'drawing with handle {self.title}')


pen = Pen('A')
pencil = Pencil('B')
handle = Handle('C')
for s in (pen, pencil, handle):
    s.draw()