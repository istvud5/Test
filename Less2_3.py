#3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц n/
# (зима, весна, лето, осень). Напишите решения через list и через dict.

a = int(input("ВВедите порядковый номер месяца года "))
# Создаю список
month_list = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябррь',
              'ноябрь', 'декабрь']
# Нахожу месяц
print(month_list[a - 1])
if a <= 2 <= 0:
    print("ЗИМА")
elif 3 <= a <= 5:
    print("Весна")
elif 6 <= a <= 8:
    print("Лето")
elif 9 <= a <= 11:
    print("Осень")
else:
    print("ЗИМА")





#Пример Евгения
# while True:
#     user_month = input('Введите номер месяца от 1 до 12: ')
#     if user_month.isdigit() and 0 <= int(user_month) <= 12:
#     # if 0 <= int(user_month) <= 12 and user_month.isdigit():
#         season_1 = ['зима', 'весна', 'лето', 'осень', 'зима']
#         season_2 = {0: 'зима', 1: 'весна', 2: 'лето', 3: 'осень', 4: 'зима'}
#         print(f'Список сезонов - {season_1[int(user_month) // 3]}\nСловарь сезонов - {season_2[int(user_month) // 3]}')
#         break
#     else:
#         print('Ошибка')


