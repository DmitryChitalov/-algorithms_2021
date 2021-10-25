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

import cProfile
from timeit import timeit

enter_number = 159753


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


def revers_4(enter_num):    # придуманный вариант пользователя
    new_list = []
    num_position = 1
    for i in str(enter_num):
        new_list.insert(-num_position, i)
        num_position = num_position + 1
    return new_list


def main():    # можно было и отдельный вызов для каждой функции
    revers_1(enter_number)
    revers_2(enter_number)
    revers_3(enter_number)
    revers_4(enter_number)


# проверка по timeit
print(f'{"Время выполнения revers_1:"} {timeit("revers_1(enter_number)", globals=globals())} {"сек."} '
      f'{ "Результат:" } {revers_1(enter_number)}')
print(f'{"Время выполнения revers_2:"} {timeit("revers_2(enter_number)", globals=globals())} {"сек."} '
      f'{ "Результат:" } {revers_2(enter_number)}')
print(f'{"Время выполнения revers_3:"} {timeit("revers_3(enter_number)", globals=globals())} {"сек."} '
      f'{ "Результат:" } {revers_3(enter_number)}')
print(f'{"Время выполнения revers_4:"} {timeit("revers_4(enter_number)", globals=globals())} {"сек."} '
      f'{ "Результат:" } {"".join(revers_4(enter_number))}', '\n')

# проверка по cProfile
cProfile.run('main()')

"""первая функция (revers_1) самая медленная - (рекурсивная судя по коду и показаниям cProfile с timeit).
самой быстрой является revers_3, 
второе место у revers_4 (созданная пользователем), но имеется запуск метода insert 
по количеству символов в переменной.
cProfile показал лишь рекурсию первой фунции и запуски метода insert (по количеству символов),
других проблем кода не обозначено"""
