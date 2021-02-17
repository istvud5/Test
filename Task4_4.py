# Представлен список чисел. Определите элементы списка, не имеющие повторений.
# Сформируйте итоговый массив чисел, соответствующих требованию.
# Элементы выведите в порядке их следования в исходном списке.\
#     Для выполнения задания обязательно используйте генератор.
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
#Результат: [23, 1, 3, 10, 4, 11]

from random import randint  # вызываем случайный набор
my_list = [randint(1, 25) for i in range(30)]
print(my_list)
for i in range(len(my_list)):
   flag = 1
   for j in range(len(my_list)):
      if my_list[i] == my_list[j] and i != j:
         flag = 0
         break
   if flag:
      print(my_list[i], end=' ')

# a = [int(s) for s in input().split()]
# for i in range(len(a)):
#     for j in range(len(a)):
#         if i != j and a[i] == a[j]:
#             break
#     else:
#         print(a[i], end=' ')

# print(a := [randint(0, 9) for j in range(20)], '\n', [i for i in a if a.count(i) == 1], sep="")

# my_list = [randint(1, 25) for i in range(30)]  # создание случайного списка цифр от 1 до 25 в количестве 30
# new_list = [el for el in my_list if my_list.count(el) == 1]  # проверка вхождения каждого элемента в список
# print('Исходный список: ', my_list)
# print('Новый список без повторений', new_list)
# # print(f'Начальный спиок\n{my_list}\nСписок без повторений\n{new_list}')