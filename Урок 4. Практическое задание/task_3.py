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
from timeit import timeit
from cProfile import run


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


# Сразу добавим дополнительную функцию
def my_revers(enter_num):
    if len(str(enter_num)) > 1 and str(enter_num)[1] == '0':
        return '0' * str(enter_num).count('0') + str(enter_num)[0]
    elif enter_num == 0:
        return ''
    else:
        tens = 10 ** (len(str(enter_num)) - 1)
        return my_revers(enter_num % tens) + str(enter_num // tens)


my_num = 778918320104123

print(timeit('revers_1(my_num)', globals=globals(), number=10000))
print(timeit('revers_2(my_num)', globals=globals(), number=10000))
print(timeit('revers_3(my_num)', globals=globals(), number=10000))
print(timeit('my_revers(my_num)', globals=globals(), number=10000))

"""
На основе полученных данных мы опять видим, что рекурсия показывает самые низкие результаты в плане
скорости, причем та, что была добавлена мной, выполняется за больший промежуток времени. Вероятно, 
это из-за того, что функция имеет дополнительные моменты, усложняющие ее (Дополнительное условие, 
сложение в return)
В свою очередь, функция с циклом выполняется быстрее, что очевидно, раз ее сложность меньше, чем у 
рекурсии. А функция со срезом выигрывает, так как, по сути, возвращает срез имеющегося числа в 
строковом виде.
"""

run('revers_1(my_num)')
run('revers_2(my_num)')
run('revers_3(my_num)')
run('my_revers(my_num)')

'''
Здесь же, не смотря на то, что есть функции с рекурсией, все значения в появляющихся таблицах равны 0.
И это означает, что данные функции не требуют оптимизации (Это забавно, потому что, так или иначе, 
имеется наиболее оптимальынй вариант).
'''
