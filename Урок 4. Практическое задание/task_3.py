"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""

from timeit import timeit
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


def revers_4(enter_num):
    enter_num = list(str(enter_num))
    enter_num.reverse()
    return ''.join(enter_num)


print('Замеры времени выполнения:\n')
print(timeit('revers_1(987654321)', globals=globals()))
print(timeit('revers_2(987654321)', globals=globals()))
print(timeit('revers_3(987654321)', globals=globals()))
print(timeit('revers_4(987654321)', globals=globals()))
print('Профилирование кода при помощи cProfile:\n')


def main():
    revers_1(987654321)
    revers_2(987654321)
    revers_3(987654321)
    revers_4(987654321)


cProfile.run('main()')

"""
3-я функция является самой быстрой за счет работы со слайзом
4-я функция будет медленне за счет преобразования в список и использование реверса с джойном для преобразования списка в строку
2-я функция является предпоследней по скорости за счет цикла
1-я функция проигрывает остальным за счет рекурсии, которая имеет 10 стэков.

К сожалению, алгоритма лучше слайза придумать не смог.
"""
