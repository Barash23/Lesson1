a = int(input("Введите значение выручки:"))
b = int(input("Введите значение издержек:"))
if a > b:
    print("Вы работаете с прибылью")
    c = a / b * 100 # узнаем рентаб
    e = int(input("Введите количество сотрудников компании:"))
    f = c / e # на 1 сотрудника
    print("Прибыль фирмы на одного сотрудника составляет:" , f , "%")
else:
    print("Вы работаете с убытком, ливай с конторы")
# Я ЕБАЛ , ГДЕ ОШИБКА , СУКА!