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


def revers_4(enter_num): return ''.join(reversed(str(enter_num)))


number = 123456789

print(f'''
revers_1: {timeit("revers_1(number)", globals=globals(), number=10000)}
revers_2: {timeit("revers_2(number)", globals=globals(), number=10000)}
revers_3: {timeit("revers_3(number)", globals=globals(), number=10000)}
revers_4: {timeit("revers_4(number)", globals=globals(), number=10000)}''')
print(f'{run("revers_1(number)")} {run("revers_2(number)")} {run("revers_3(number)")} {run("revers_4(number)")}')

print(revers_1(number), revers_2(number), revers_3(number), revers_4(number))

"""Самая быстрая функция это третия, а не моя так как reversed с join затрачивает больше времени чем срез, 
так как срез присваивается все слово сразу, а значит сложность O(1), reversed O(N), Join O(N)
, ну и потому
что срез это одно действие, а в моем целых два. run из модуля cProfile позволяет просмотреть все действия, 
особенно хорошо это видно на рекурсии он отображает сколько раз было запущена функция.Но по определению 
количество времени побеждает timeit ведь он может прогоняеть функцию множество раз, что позволяет сравнивать время"""
