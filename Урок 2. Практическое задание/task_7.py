"""
7.	Напишите программу, доказывающую или проверяющую, что для множества
натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2,
где n - любое натуральное число.
Рекурсия вам нужна для решения левой части выражения.
Полученный результат нужно просто сравнить с результатом в правой.

Пример:
для n = 5
1+2+3+4+5 = 5(5+1)/2

Подсказка:
Правой части в рекурсии быть не должно!!! Необходимо сравнить результат, который даст рекурсивная ф-ция
со значением, полученным в правой части (здесь нужно просто подставить n и подсчитать)

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

class OwnError (Exception):
    def __init__(self, txt):
        self.txt = txt


def req_summ_n(n):
    if n == 1:
        return 1
    else:
        return req_summ_n(n-1) + n


while True:
    try:
        user_number = int(input(f"Введите n:"))
        if user_number <= 0:
            raise OwnError("Введено не натуральное число!\n")
        res1 = req_summ_n(user_number)
        res2 = user_number * (user_number + 1) / 2
        print(f'Сумма {user_number} членов ряда: 1 2 3 4 ... n равна {res1}')
        print(f'Значение выражения {user_number}({user_number}+1)/2 равно {res2}')
        print(f'Проверка на равенство - {res1 == res2}')
        break
    except ValueError:
        print('Введено не число!\n')
    except OwnError as err:
        print(err)
