'''
4.Реализуйте базовый класс Car.
У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда).
Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
Добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля.
Для классов TownCar и WorkCar переопределите метод show_speed.
При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении скорости.
Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
Выполните вызов методов и также покажите результат.
'''
class Car:

    def __init__(self, name, speed, color, is_police=False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police

    def go(self):
        return f'Автомобиль {self.name} начал движение.'

    def stop(self):
        return f'\nАвтомобиль {self.name} остановился.'

    def turn(self, direction):
        return f'\nАвтомобиль {self.name} повернул на {direction}'

    def show_speed(self):
        return f'\nВаша скорость {self.speed}'


class TownCar(Car):
    def show_speed(self):

        if self.speed > 60:
            return f'\nВы превысили скорость! Вы движетесь со скоростью {self.speed} км/час'
        else:
            return f'Скорость движения автомобиля {self.name} км/час. Допустимый режим!'


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if self.speed > 40:
            return f'\nВы превысили скорость! Вы движетесь со скоростью {self.speed} км/час'
        else:
            return f'Скорость движения автомобиля {self.speed} км/час. Допустимый режим!'


class PoliceCar(Car):
    def show_speed(self):
        if self.speed > 60:
            return f'\nВы превысили скорость! Вы движетесь со скоростью {self.speed} км/час'
        else:
            return f'Скорость движения автомобиля {self.name} км/час. Допустимый режим!'


town = TownCar('Audi', 70, 'желтый', False)
print('1:\n' + town.go(), town.show_speed(), town.turn('лево'), town.turn('право'), town.stop())

sport = SportCar('AudiRS', 170, 'красный', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn('лево'), sport.stop())

work = WorkCar('ВАЗ', 30, 'белый', False)
print('3:\n' + work.go(), work.show_speed(), work.turn('право'), work.stop())

police = PoliceCar('Kia', 100, 'оранжевый', True)
print('4:\n' + police.go(), police.show_speed(), police.turn('лево'), police.stop())
