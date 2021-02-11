# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
# наибольших двух аргументов.

def my_func(*args):
    a = [
        int(input('')),
         int(input('')),
         int(input(''))
    ]
    a.sort()
    b = a[2]
    c = a[1]
    print(b + c)
my_func()


# rec_fact = lambda a: 1 if not a else a * rect_fact(a-1)


# def my_func(x, y, z):
#     sequence = [x, y, z]
#     total = []
#     max_1 = max(sequence)
#     total.append(max_1)
#     sequence.remove(max_1)
#     max_2 = max(sequence)
#     total.append(max_2)
#     print(sum(total))
# my_func()
