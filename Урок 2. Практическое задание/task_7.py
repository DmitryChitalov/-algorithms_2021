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
В ф-цию принимаются два элемент - это левая и правая части

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

#
# def check_equality(sequence, expression=0, result=0):
#     if not sequence:
#         expression = expression * (expression + 1) / 2
#         return result == expression
#     result += sequence
#     expression += 1
#     return check_equality(sequence - 1, expression, result)


def check_equality(sequence, expression=0):
    if not sequence:
        return 0
    result = sequence + check_equality(sequence - 1, expression)
    expression = int(sequence * (sequence + 1) / 2)
    sequence = result
    return sequence == expression


print(check_equality(4))