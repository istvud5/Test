# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие атрибуты:
# speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда).
# Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите метод
# show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar)
# должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Cars:
    name = None
    speed = None
    color = None
    is_police = False

    def __init__(self, name, speed, color, is_police = False):
        self.name = name
        self.speed = speed
        self.color = color
        self.is_police = is_police
    def go(self):
        return "The car went"
    def stop(self):
        return "The car has stopped"
    def turn(self, direction):
        return "The car turned to " + direction

class TownCar(Cars):
    family = None
    def __init__(self, name, speed, color, family = True):
        super().__init__(name, speed, color)
        self.family = family

class SportCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color)

class WorkCar(Cars):
    def __init__(self, name, speed, color, is_police):
        super().__init__(name, speed, color, is_police)

class PoliceCar(Cars):
    def __init__(self, name, speed, color):
        super().__init__(name, speed, color, True)

ford = TownCar('Ford', 60, 'black')
print(ford.name, ford.color, ford.speed, ford.is_police)
print(ford.go(), ford.turn('City'), ford.stop())
sport = SportCar('Ford', 180, 'red')
work1 = WorkCar('Ford', 90, 'white', True)
work2 = WorkCar('Audi', 90, 'white', False)
police = PoliceCar('Ford', 180, 'red')




# class Car:
#     """Автомобиииль !!!"""
#
#     def __init__(self, name, color, speed, is_police=False):
#         self.name = name
#         self.color = color
#         self.speed = speed
#         self.is_police = is_police
#         print(f"Новая машина: {self.name} (Цвет {self.color}) машина полицейская - {self.is_police}")
#
#     def go(self):
#         print(f"{self.name}: Машина поехала")
#
#     def stop(self):
#         print(f"{self.name}: Машина остановилась")
#
#     def turn(self, direction):
#         print(f"{self.name}: Машина повернула {'налево' if direction == 0 else 'направо'}")
#
#     def show_speed(self):
#         print(f"{self.name}: Скорость автомобиля - {self.speed}")
#
# class WorkCar(Car):
#
#     def show_speed(self):
#         return f"{self.name}: Скорость автомобиля - {self.speed} - ПРЕВЫШЕНИЕ СКОРОСТИ!!!" \
#             if self.speed > 40 else f"{self.name}: Скорость автомобиля - {self.speed}" # super().show_speed()
#
#
# class SportCar(Car):
#     """Спортивный автомобиль"""
#
# class PoliceCar(Car):
#     def __init__(self, name, color, speed, is_police=True):
#         super().__init__(name, color, speed, is_police)
#
# police_car = PoliceCar('ДПС', 'Белый', 80)
# police_car.go()
