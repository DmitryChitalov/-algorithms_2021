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


def inter_num():
    return int(input('Введите целое число: '))


def revers_1(enter_num, revers_num=0):  # O(N!) Рекурсия
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):  # Цикл O(N), но больше промежуточных рассчетов
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):  # O(N) Описание под текстом кода
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):  # O(N) reversed() Обратный итератор списка + .join объединение списка
    revers_num = ''.join(reversed(str(enter_num)))
    return revers_num


def revers_5(enter_num):  # O(N) Конкатенация не самая быстрая операция
    enter_num = str(enter_num)
    revers_num = ''
    for i in enter_num:
        revers_num = i + revers_num
    return revers_num


def revers_6(enter_num, temp_digit=''):  # O(N!) Тоже рекурсия, как и revers_1(),
    # имеет меньшее число вызовов самой себя, но работае медленее.
    temp = enter_num
    temp_digit += str(temp % 10)
    temp = temp // 10
    if temp == 0:
        return temp_digit
    else:
        return revers_6(temp, temp_digit)


def main(num):
    for i in range(number):
        revers_1(num)
    for i in range(number):
        revers_2(num)
    for i in range(number):
        revers_3(num)
    for i in range(number):
        revers_4(num)
    for i in range(number):
        revers_5(num)
    for i in range(number):
        revers_6(num)


my_number = inter_num()
# my_number = 12345
number = 1000000

run('main(my_number)')

print(f'revers_1: {timeit("revers_1(my_number)", globals=globals(), number=number)}')
print(f'revers_2: {timeit("revers_2(my_number)", globals=globals(), number=number)}')
print(f'revers_3: {timeit("revers_3(my_number)", globals=globals(), number=number)}')
print(f'revers_4: {timeit("revers_4(my_number)", globals=globals(), number=number)}')
print(f'revers_5: {timeit("revers_5(my_number)", globals=globals(), number=number)}')
print(f'revers_6: {timeit("revers_6(my_number)", globals=globals(), number=number)}')


'''
Самая эффективная функция - это функция revers_3() с помощью оператора slice([]), имеет сложность O(N), 
без дополнительных промежуточных действий.
'''