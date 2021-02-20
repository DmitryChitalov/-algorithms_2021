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


#Самая медленная так как здесь рекурсия
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)

#Есть цикл, что делает функцию быстрее рекурсивной
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num

#Самая быстрая функция т.к. просто задается новая строка с шагом в -1
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


num = 6495

print(timeit.repeat("revers_1(num)", globals=globals(), repeat=3))
print(timeit.repeat("revers_2(num)", globals=globals(), repeat=3))
print(timeit.repeat("revers_3(num)", globals=globals(), repeat=3))

def main():
    num = 6495769784264562
    revers_1(num)
    revers_2(num)
    revers_3(num)


run("main()")
