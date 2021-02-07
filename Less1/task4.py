a = int(input("Введите любое число:  "))
max = 0
while a > 0:
    x = a % 10
    if x >= max:
        max = x
    a = a // 10
print(max)


