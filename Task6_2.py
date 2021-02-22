# 2. Реализовать класс Road (дорога), в котором определить атрибуты:
# length (длина), width (ширина).
# Значения данных атрибутов должны передаваться при создании экземпляра класса.
# Атрибуты сделать защищенными.
# Определить метод расчета массы асфальта, необходимого для покрытия всего
# дорожного полотна. Использовать формулу: длина * ширина * масса асфальта
# для покрытия одного кв метра дороги асфальтом, толщиной в 1 см * чи сло см
# толщины полотна. Проверить работу метода.
# Например: 20м * 5000м * 25кг * 5см = 12500 т


class Road:
    def __init__(self, _length, _width):
        self._length = _length
        self._width = _width

    def mass(self):
        return self._length * self._width


class MassCount(Road):
    def __init__(self, _length, _width, volume):
        super().__init__(_length, _width)
        self.volume = volume


r = MassCount(25, 10000, 125)
print(r.mass())













# class Road:
#     def __init__(self, lenght, width):
#         self._lenght = lenght
#         self._width = width
#     def mass_full(self):
#         return f"{self._lenght} м * 25 кг * 5 см = {(self._lenght * self._width * 25 * 5) / 1000} т"
#
# road_1 = Road(5000, 20)
# print(road_1.mass_full())









