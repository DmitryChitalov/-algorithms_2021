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

num = 123456789



print('1 -- ', timeit.timeit('revers_1(num)', 'from __main__ import revers_1, num', number=1000))
print('2 -- ', timeit.timeit('revers_2(num)', 'from __main__ import revers_2, num', number=1000))
print('3 -- ', timeit.timeit('revers_3(num)', 'from __main__ import revers_3, num', number=1000))


print('reverse_1--------------------------------------')
cProfile.run('revers_1(num)')
print('reverse_2--------------------------------------')
cProfile.run('revers_2(num)')
print('reverse_3--------------------------------------')
cProfile.run('revers_3(num)')




# 1 вариант работает дольше всего т.к.функция работает (len(my)) раз
# 2 вариант идет перебор элементов и делает доролнительные дейчтвия это и  замедляет работу
# саммый быстрый вариант 3, встроеные методы работают быстрее всего
# cProfile показал везьде нули, нет отличий. Только в 1 варианте вызов рекурсии показвает и это показывает
# неэфективность решения. cProfile видимо надо применять на более больших решениях.
