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


def calc(n):
    """Функция возвращает результат 1+2+3+...+n"""
    return 1 if n == 1 else n + calc(n - 1)


n = int(input('Enter n: '))
print(f'1+2+...+n = {calc(n)}')
print(f'n(n+1)/2 = {n * (n + 1) / 2}')