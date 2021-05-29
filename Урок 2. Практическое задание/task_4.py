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


class OwnError (Exception):
    def __init__(self, txt):
        self.txt = txt


def req_calc_row(n):
    if n == 1:
        return 1
    else:
        return req_calc_row(n-1) + (-1/2)**(n-1)


while True:
    try:
        user_number = int(input(f"Введите n:"))
        if user_number <= 0:
            raise OwnError("Введено не натуральное число!\n")
        print(f' сумма {user_number} членов ряда: 1 -0.5 0.25 -0.125 ... равна {req_calc_row(user_number)}')
        break
    except ValueError:
        print('Введено не число!\n')
    except OwnError as err:
        print(err)
