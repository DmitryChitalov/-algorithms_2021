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


# O(n!) очень похоже
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


# O(n)
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


# O(n)
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


# O(N)
def revers_4(enter_num):
    listed_num = list(str(enter_num))
    # приводим к списку, т.к. функция применяется только к списку
    listed_num.reverse()                    # O(N)
    revers_num = "".join(listed_num)
    return revers_num


def main():
    print("Рекурсия:", timeit('revers_1(number)', globals=globals(), number=20000))
    print("While:", timeit('revers_2(number)', globals=globals(), number=20000))
    print("Срез:", timeit('revers_3(number)', globals=globals(), number=20000))
    print("my_func_reverse:", timeit('revers_4(number)', globals=globals(), number=20000))


number = 564892365
run('main()')
"""
Рекурсия: 0.0549181
While: 0.023538300000000012
Срез: 0.007375199999999998
my_func_reverse: 0.016952400000000006

Выводы: Рекурсия очень медленно за счёт сложности (4 место), 
While медленно за счет итераций и сложности O(n) (3 место), 
reverse 2 место за счет сложности O(1), но проигрывает за счёт примнения двух
методов reverse and join, 
срез быстрее всего. 
"""