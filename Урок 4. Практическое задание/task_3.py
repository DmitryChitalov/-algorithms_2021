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


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


vol = 1236450
print(timeit('revers_1(vol)', globals=globals()))  # 1.9106982
print(timeit('revers_2(vol)', globals=globals()))  # 1.3312625
print(timeit('revers_3(vol)', globals=globals()))  # 0.37501439999999997
print(timeit('revers_4(vol)', globals=globals()))  # 0.6993331
run('revers_1(vol)')
run('revers_2(vol)')
run('revers_3(vol)')
run('revers_4(vol)')
"""
Как и ожидалось рекурсия отработала дольше других т.к имеет самую высокую сложность,
так же в данном исполнении рекурсия и цикл дают не правильный результат с цифрами
оканчивающимися нулём, а также выдают результат Float (546321.0).
Функции со срезом и reversed + join выводят корректный результат (0546321) и отрабатывают в разы быстрее
однако в четвертом примере помимо reversed ещё тратится время на создание списка (join),
поэтому функция со срезом будет самой эффективной в скорости исполнения
"""
