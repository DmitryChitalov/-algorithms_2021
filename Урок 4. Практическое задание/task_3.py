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
    revers_num = "".join(reversed(str(enter_num)))
    return revers_num


print(timeit('revers_1(15763)', globals=globals()))
print(timeit('revers_2(15763)', globals=globals()))
print(timeit('revers_3(15763)', globals=globals()))
print(timeit('revers_4(15763)', globals=globals()))
cProfile.run('revers_1(1000000)')
cProfile.run('revers_2(1000000)')
cProfile.run('revers_3(1000000)')
cProfile.run('revers_4(1000000)')

"""
Самый быстрый вариант - вариант со срезами (так как это встроенная функция и ей не приходится работать
с перебором данных, работа с индексами происходит быстрее
Далле по скорости идет reverset, потом цикл и рекурсия
"""
