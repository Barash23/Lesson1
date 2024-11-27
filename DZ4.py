a = int(input("Введите целое положительное число:"))
b = a % 10
while a >= 1:
    a = a // 10
    if a % 10 > b:
        b = a % 10
    elif a > 9:
        pass
print("Максимальное цифра в числе ", b)