# . Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

def summary():
    try:
        with open('file_5.txt', 'w+') as file_obj:
            line = input('Введите цифры через пробел \n')
            file_obj.writelines(line)
            my_numb = line.split()

            print(sum(map(int, my_numb)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()



# from random import randint
# with open('5.txt', mode='w+', encoding='utf-8') as f:
#     f.write(" ".join([str(randint(1, 1000)) for _ in range(100000)]))
#     f.seek(0)
#     print(sum(map(int, f.readline().split())))
