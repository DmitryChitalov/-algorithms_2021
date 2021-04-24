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
Правой части в рекурсии быть не должно. Необходимо сравнить результат, который даст рекурсивная ф-ция
со значением, полученным в правой части (здесь нужно просто подставить n и подсчитать)

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def sum_n(n):
    return n if n == 1 else sum_n(n-1) + n


def compare_sum(n):
    print(f'Сравниваем сумму ряда чисел от 1 до {n} и {n}*({n}+1)/2')
    return 'Верно!' if sum_n(n) == n * (n + 1) / 2 else 'Неверно'


while True:
    number = input('Введите количество элементов (n > 0) \n>>> ')
    if number.isdigit() and int(number) > 0:
        break

number = int(number)
print(compare_sum(number))
