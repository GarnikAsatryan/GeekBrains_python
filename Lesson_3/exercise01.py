# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя, предусмотреть обработку ситуации деления на ноль.

def my_func():
    a = float(input('Введите делимое число: '))
    b = float(input('Введите число делитель: '))
    try:
        return a / b
    except ZeroDivisionError:
        print('Ошибка! Делить на ноль нельзя')

result = my_func()
print(result)