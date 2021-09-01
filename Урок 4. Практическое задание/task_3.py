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

from time import sleep
from timeit import timeit
from cProfile import run

def revers_1(enter_num, revers_num=0):
    sleep(2)
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    sleep(2)
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    sleep(2)
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

    
def revers_4(enter_num):
    sleep(2)
    list_1 = str(enter_num).split()
    return list_1[0][::-1]

    
def main(enter_num):
    revers_1(enter_num)
    revers_2(enter_num)
    revers_3(enter_num)
    revers_4(enter_num)


enter_num = 123456789

print(timeit("revers_1(enter_num)", globals=globals(),number=1))
print(timeit("revers_2(enter_num)", globals=globals(),number=1))
print(timeit("revers_3(enter_num)", globals=globals(),number=1))
print(timeit("revers_4(enter_num)", globals=globals(),number=1))

run('main(enter_num)')

"""
Cамой эффективной можно считать 3 функцию, за ней идет 4, потом 2, а самой неэффективной можно считать 1.
1 является неэффективной из-за решения через рекурсию, 2 более эффективна так как решена через цикл,
3 самая эффективная так как в ней используется всего 2 присваивания, одна функия и разворот, 4 же
является не самой эффективной, так как там используется создание списка, использование функции str
и метода split, а так же возврат определенного элемента с разворотом этого элемента.
"""
