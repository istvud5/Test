# 1. Создать класс TrafficLight (светофор) и определить у него один
# атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый. Продолжительность первого состояния
# (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке
# (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

# import time
# class TrafficLight:
#     _color = None
#     _colors = ['red', 'yellow', 'green']
#
#     def __init__(self):
#         self._color = self._colors[0]
#
#     def running(self):
#         i = 0
#         while i < 5:
#             for el in TrafficLight._colors:
#                 print(el)
#                 i += 1
#                 time.sleep(1)
#
# traffic = TrafficLight()
# traffic.running()


# from time import sleep
#
#
# class TrafficLight:
#     __color = ['Красный', 'Желтый', 'Зеленый']
#
#     def running(self):
#         i = 0
#         while i < 3:
#             print(f'Светофор переключается \n '
#                   f'{TrafficLight.__color[i]}')
#             if i == 0:
#                 sleep(7)
#             elif i == 1:
#                 sleep(5)
#             elif i == 2:
#                 sleep(3)
#             i += 1


# TrafficLight = TrafficLight()
# TrafficLight.running()
# afficLight.running()

# from time import sleep
# class TrafficLight:
#     __color = "Черный"
#     def running(self):
#         while True:
#             print('Красный')
#             sleep(3)
#             print('Желтый')
#             sleep(2)
#             print('Зеленый')
#             sleep(1)
#             print('Желтый')
#             sleep(2)
# trafficlight = TrafficLight()
# trafficlight.running()

# import time
# import itertools
#
# class TrafficLight:
#     __color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [7, 32]], ["yellow", [2, 33]]]
#
#     def running(self):
#         for light in itertools.cycle(self.__color):
#             print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
#             time.sleep(light[1][0])
#
#
# trafficlight = TrafficLight()
# trafficlight.running()


#print('привет\rпока')







