#1. Создать список и заполнить его элементами различных типов данных. Реализовать скрипт проверки типа данных n/
# каждого элемента. Использовать функцию type() для проверки типа. Элементы списка можно не запрашивать у n/
# пользователя, а указать явно, в программе.
a = [55, 5.5, "This text", False, True, (2 + 1j)]
print(len(a))
b = int(len(a))
c = 0
while c <= b:
    print(type(a[c]))
    c += 1

#Решение Евгения
# my_list = [(-1 + 0j), 1, 2.2, True, None, 'String', [3, 4],
#            (5, 6, 6.5), {7: 'seven', 8: 'eight'}, {9, 10},
#            frozenset(), range(11), (b'twelve'), bytearray(b'thirteen'),
#            zip(*[(14, 15), (16, 17), ('a', 'b')]), TypeError]
#
# for i, item in enumerate(my_list, 1):
#   print(f"{i}) {item} - {type(item)}")