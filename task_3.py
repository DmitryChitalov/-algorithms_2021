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
import cProfile
import timeit

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
    n1 = str(enter_num)
    n_list = list(n1)
    n_list.reverse()
    n2 = "".join(n_list)
    return n2


enter_num = 123456789123456789


print('1 -- ', timeit.timeit('revers_1(enter_num)', 'from __main__ import revers_1, enter_num', number=1000))
print('2 -- ', timeit.timeit('revers_2(enter_num)', 'from __main__ import revers_2, enter_num', number=1000))
print('3 -- ', timeit.timeit('revers_3(enter_num)', 'from __main__ import revers_3, enter_num', number=1000))
print('4 -- ', timeit.timeit('revers_4(enter_num)', 'from __main__ import revers_4, enter_num', number=1000))
print('reverse_1--------------------------------------')
cProfile.run('revers_1(enter_num)')
print('reverse_2--------------------------------------')
cProfile.run('revers_2(enter_num)')
print('reverse_3--------------------------------------')
cProfile.run('revers_3(enter_num)')
print('reverse_4--------------------------------------')
cProfile.run('revers_4(enter_num)')



#1 --  0.0050000000000000044
#2 --  0.003415299999999996
#3 --  0.0003394000000000036
#4 --  0.0007507000000000069
# 1 вариант работает дольше всего т.к.функция отрабывает (len(my)) раз
# 2 вариант производит перебор элементов и совершает еще 3 операции над ними из этого замедляет работу
# саммый эффективный вариант номер 3, встроеные методы отрабатывают быстрее всего (пример 3 и 4)
# cProfile не показал разницы между методами(везде по нулям, кроме примера один вызов рекурсивной функции вызвался 19 раз,
# что тоже показывает неэфективность метода), скорее всего cProfile нужно применять на более масштабных операциях,
# либо где элементов много либо саамих операция

