seconds = int(input("Введите секунды:  "))
hours = seconds // 3600
seconds = seconds % 3600
minutes = seconds // 60
seconds = seconds % 60
print("чч:мм:сс   " f'{hours}:{minutes}:{seconds}')







