"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""
from timeit import timeit
from cProfile import run


def reverse_1(enter_num, revers_num=0):
    # O(n^2)
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return reverse_1(enter_num, revers_num)


def reverse_2(enter_num, revers_num=0):
    # O(n)
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def reverse_3(enter_num):
    # O(n)
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def my_reverse(enter_num):
    # O(n)
    listed_num = list(str(enter_num))
    listed_num.reverse()
    revers_num = "".join(listed_num)
    return revers_num


def main():
    print("Рекурсия:\n", timeit('reverse_1(my_number)', globals=globals(), number=10000))
    print("Цикл while:\n", timeit('reverse_2(my_number)', globals=globals(), number=10000))
    print("Срез:\n", timeit('reverse_3(my_number)', globals=globals(), number=10000))
    print("reverse():\n", timeit('my_reverse(my_number)', globals=globals(), number=10000))


my_number = 123456789

run('main()')


'''
1 - срез: заточен на скорость исполнения.
2 - reverse(): используются встроенные функции, заточенные на решение конкретных задач.
3 - цикл: проверка условия при каждой итерации.
4 - рекурсия: медленная и безжалостная.
'''