'''
4. Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name,
is_police (булево). А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала,
остановилась, повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''
class Car:

    def __init__(self, name, speed, color, is_police):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f' {self.name} (цвет: {self.color}) поехала.'

    def stop(self):
        return f'\n {self.name} остановилась.'

    def turn(self, direction):
        return f'\n {self.name} поворачивает на {direction}.'

    def show_speed(self, n):
        if n == 0:
            return f'\n Скорость: {self.speed} км/ч.'
        else:
            if self.speed > n:
                return f'\n Превышение скорости, скорость : {self.speed} км/ч.'
            else:
                return f'\n Скорость {self.name} в норме, скорость : {self.speed} км/ч.'


    def police_check(self):
        if self.is_police != False:
            return f'\n {self.name} полицейская машина.'
        else:
            return f'\n {self.name} не полицейская машина.'


class TownCar(Car):
    pass

class SportCar(Car):
    pass

class WorkCar(Car):
    pass

class PoliceCar(Car):
    pass


town = TownCar('Smart', 70, 'Белый', False)
print('\n' + town.go(), town.show_speed(60), town.turn('Право'), town.turn('Лево'), town.stop(), town.police_check())

sport = SportCar('Bugatti', 250, 'Синий', False)
print('\n' + sport.go(), sport.show_speed(0), sport.turn('Право'), sport.stop(), sport.police_check())

work = WorkCar('KIA', 40, 'Серый', False)
print('\n' + work.go(), work.show_speed(40), work.turn('Право'),work.turn('Право'), work.stop(), work.police_check())

police = PoliceCar('Ford', 100, 'Белый', True)
print('\n' + police.go(), police.show_speed(0), police.turn('Лево'), police.stop(), police.police_check())