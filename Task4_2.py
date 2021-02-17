# Представлен список чисел. Необходимо вывести элементы исходного списка, значения которых больше предыдущего элемента.
# Подсказка: элементы, удовлетворяющие условию, оформить в виде списка. Для его формирования используйте генератор.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].

num_list = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
first_list = [num_list[num] for num in range(1, len(num_list)) if num_list[num] > num_list[num - 1]]
print(first_list)

