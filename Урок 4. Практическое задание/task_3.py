"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""

from timeit import timeit
from cProfile import run
from random import randint


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
    return str(enter_num)[::-1]


def revers_5(enter_num):
    num = list(str(enter_num))
    len_num = len(num)
    for i in range(len_num//2):
        num[i], num[len_num-i-1] = num[len_num-i-1], num[i]
    return ''.join(num)


num = randint(100000000, 1000000000000)


def main():
    revers_1(num)
    revers_2(num)
    revers_3(num)
    revers_4(num)
    revers_5(num)


print('revers_1:', timeit('revers_1(num)', globals=globals()))
print('revers_2:', timeit('revers_2(num)', globals=globals()))
print('revers_3:', timeit('revers_3(num)', globals=globals()))
print('revers_4:', timeit('revers_4(num)', globals=globals()))
print('revers_5:', timeit('revers_5(num)', globals=globals()))

print()
run('main()')

"""
Первый вариант самый долгий за счёт выполнения рекурсии.
Выриант с циклом выполняется быстрее, т.к. требуется 
всего один проход цикла для решения задачи.
Третий вариант самый быстрый из предложенных, т.к. из строки сразу берутся
элементы в обратном порядке.

Можно немного ускорить третий вариант, убрав лишние присваивания
и сразу возвратив результат.
 
Так же первые 2 варианта теряют ведущие нули итогового числа, 
т.к. возвращают число, а не строку.
Можно ускорить вариант с циклом, если превратить число в список и
проходить циклом только до половины, сразу меняя местами по два
элемента через множественное присваивание. Но взятие элементов строки
в обратном порядке всё равно будет работать значительно быстрее.

CProfile в данном случае не эффективен, т.к. единичный вызов
функции выполняется слишком быстро, что бы дать информативные
результаты.

В итоге наибольшую эффективность показывает 4я функция.
revers_1: 3.8583942
revers_2: 2.7045357
revers_3: 0.40065550000000005
revers_4: 0.3749849999999997
revers_5: 1.8483399
"""
