#  Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами n/
#  0 и 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте.n/
#  Для заполнения списка элементов необходимо использовать функцию input().

my_list = input("ВВедите элементы массива ").split()
print(f'Original {my_list}')
i = 0
while i + 1 < len(my_list):
    if i % 2 == 0:
        my_list.insert(i, my_list.pop(i + 1))
    i += 1
print(f'Change {my_list}')


a = input('Input digits with BSP ').split()
for i in range(1, len(a), 2):
    a.insert(i - 1, a.pop(i))
print(a)






# list.insert(i, x)


# my_list = list(input("Введите числа без пробелов - "))
#
# for i in range(1, len(my_list), 2):
#     my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]
# print(my_list)






