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

def function(num: int, count: int = 0):
    if num >= 1:
        count += num
        return function(num - 1, count)
    else:
        return count

n = 5
num = function(n)

if num == n * (n + 1) / 2:
    print(f'Для num = {n}, утвержденеи верно')
else:
    print(f'Для num = {n}, утвержденеи не верно')


