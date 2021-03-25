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


"""
Не совсем понял посказку. Надеюсь такое решение тоже подходит
"""


def left_side(number_for_left_side):    # Рекурсивный подсчет суммы элементов
    if number_for_left_side == 0:
        return 0
    else:
        return number_for_left_side + left_side(number_for_left_side - 1)


def right_side(number_for_right_side):  # Подсчет суммы элементов по формуле
    return number_for_right_side*(number_for_right_side + 1)/2


def check_statement(number_to_check):   # Функция проверки утверждения
    if left_side(number_to_check) == right_side(number_to_check):
        print("Statement is true")
    else:
        print("Statement is false")


check_statement(154)
