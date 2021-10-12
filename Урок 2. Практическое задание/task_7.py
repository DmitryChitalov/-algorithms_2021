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
# Два способа


def check_equality_1(sequence, expression=0, result=0):
    if not sequence:
        expression = expression * (expression + 1) / 2
        return result == expression
    result += sequence
    expression += 1
    return check_equality_1(sequence - 1, expression, result)


print(check_equality_1(45))

#######################################################################################


def check_equality_2(sequence):
    if not sequence:
        return 0
    return sequence + check_equality_2(sequence - 1)


number = int(input('Введите число: '))
result = check_equality_2(number)
number = number * (number + 1) / 2
print(result == number)