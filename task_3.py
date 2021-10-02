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


import timeit
import cProfile


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


def my_revers(enter_num):
    n_list = list(str(enter_num))
    n_list.reverse()
    enter_num = "".join(n_list)
    return enter_num


def all_func():
    revers_1(1234567890)
    revers_2(1234567890)
    revers_3(1234567890)
    my_revers(1234567890)


# Как мы уже знаем, когда используется рекурсия код становится болеее лаконичным, но скорость выполения снижается.
# В цикле мы итерируемся по всей длине, что не является лучшим вариантом.
# В последнем случае мы используем срез, что значительно ускоряет программу O(1).
# В моей вариации цифры переводятся в строку, а затем разбивается по одной цифре в списке, а потом делается reverse
# и соединяется. Довольно быстро, но до среза еще далеко.

if __name__ == '__main__':
    a1 = timeit.timeit('revers_1(1234567890)', globals=globals(), number=1000000)
    a2 = timeit.timeit('revers_2(1234567890)', globals=globals(), number=1000000)
    a3 = timeit.timeit('revers_3(1234567890)', globals=globals(), number=1000000)
    a4 = timeit.timeit('my_revers(1234567890)', globals=globals(), number=1000000)
    print(a1, a2, a3, a4)  # 5.4091883 3.8110578999999998 0.7941918999999995 1.4159908999999988
    cProfile.run('all_func()')
