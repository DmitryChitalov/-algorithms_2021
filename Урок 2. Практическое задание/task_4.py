"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def func_num(n):
    if n == 1:
        return 1
    else:
        return func_num(n-1) / 2


def func_sum(n):
    if n == 1:
        return 1
    else:
        if n % 2 == 0:
            return func_sum(n - 1) - func_num(n)
        else:
            return func_sum(n - 1) + func_num(n)


if __name__ == '__main__':
    try:
        x = int(input('enter number'))
        print(func_sum(x))
    except ValueError:
        print('You entered not an integer.')



