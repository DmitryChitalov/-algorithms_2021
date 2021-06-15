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
import random
'''
Возможные варианты решения
def recur_method(numb):
    if numb == 1:
        return numb
    else:
        return recur_method(numb-1) + numb

try:
    NUMB = int(input('Введите число: '))
    if recur_method(NUMB) == NUMB * (NUMB+1) / 2:
        print(f'Равенство равно')
except ValueError:
    print(f'Вы вместо числа ввели строчку')


и еще одно решение

def recur_method (numb):
    return numb if numb == 1 else numb + recur_method(numb-1)
'''


def func_recursion_seven(number, verification_number, the_sum=0, counter=1):
    the_sum = the_sum + counter
    print(f' number, verification_number, the_sum, counter ', number, verification_number, the_sum, counter)
    if the_sum != verification_number:
        func_recursion_seven(number, verification_number, the_sum, counter = counter + 1)
    return the_sum


if __name__ == '__main__':
    my_number = int (input (f'Введите натуральное число '))
    print(f'final ', func_recursion_seven (my_number, int((my_number * (my_number + 1)) / 2)))
