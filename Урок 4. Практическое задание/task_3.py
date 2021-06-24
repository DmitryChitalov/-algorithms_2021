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


from cProfile import run
from timeit import timeit
import random

my_num = random.randint(1000000, 100000000)

print(my_num)


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
    my_list = [i for i in reversed(str(enter_num))]
    return ''.join(my_list)


print(timeit('revers_1(my_num)', globals=globals(), number=10000))          # 0.06443115099999999
print(timeit('revers_2(my_num)', globals=globals(), number=10000))          # 0.04471473599999998
print(timeit('revers_3(my_num)', globals=globals(), number=10000))          # 0.01204923400000002
print(timeit('revers_4(my_num)', globals=globals(), number=10000))          # 0.03201660600000003

# Первая функция рекурсивная, соответственно имеет сложность O(n!), из-за этого наибольшее время выполнения.
# Остальные функции имеют сложность O(n), но с разным количеством операций, отсюда расхождения во
# времени выполнения.


run('revers_1(my_num)')
run('revers_2(my_num)')
run('revers_3(my_num)')
run('revers_4(my_num)')


# Время выполнения всех функций равно 0, так как выполняеться только один раз. Первая функция совершает 12 вызовов
# функций. Вторая и третья по 4. Четвертая - 6.