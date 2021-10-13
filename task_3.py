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
import timeit
from cProfile import run
# самая эффективная ф-ия оказалась срезом,
# на втором месте цикл, на третьем рекурсия


# рекурсия
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


# цикл
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        # присвоения и арифметические действия дают O(log n)
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


# срез
def revers_3(enter_num):
    # O(N) сложность линейная
    enter_num = str(enter_num)  # O(N)
    revers_num = enter_num[::-1]  # O(N)
    return revers_num


enter_num = int(input('Enter number: '))

print(revers_1(enter_num, revers_num=0))
print(revers_2(enter_num, revers_num=0))
print(revers_3(enter_num))


print('Ркекурсия', timeit.timeit(f'revers_1({enter_num})', globals=globals(), number=10000))
print('Цикл', timeit.timeit(f'revers_2({enter_num})', globals=globals(), number=10000))
print('Срез', timeit.timeit(f'revers_3({enter_num})', globals=globals(), number=10000))


def main():
    revers_1(enter_num, revers_num=0)
    revers_2(enter_num, revers_num=0)
    revers_3(enter_num)


run('main()')




