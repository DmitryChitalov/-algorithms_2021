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

from timeit import default_timer, timeit
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


# Прежде всего проверим работу функций
# Из выводов видим, что первые 2 способа разворачивают числа с нулями на конце не корректно.

print(revers_1(12300))
print(revers_2(12300))
print(revers_3(12300))


# Мы уже делали подобное задание на уроке 2. Так что код для профилирования возьму оттуда. Все равно именно то решение
# первым в голову приходит. Так же посмотрим на его вывод.

def from_tail_to_head(number):
    if not number // 10:
        return str(number)
    return from_tail_to_head(number % 10) + from_tail_to_head(number // 10)


print(from_tail_to_head(12300))

# Теперь займемся профилированием.

# Профилирование через timeit:

n = 1234568

print('Профилирование функции revers_1 через timeit: ' + str(timeit(
    'revers_1(n)',
    globals=globals())))

print('Профилирование функции revers_2 через timeit: ' + str(timeit(
    'revers_2(n)',
    globals=globals())))

print('Профилирование функции revers_3 через timeit: ' + str(timeit(
    'revers_3(n)',
    globals=globals())))

print('Профилирование функции from_tail_to_head через timeit: ' + str(timeit(
    'from_tail_to_head(n)',
    globals=globals())) + '\n')

print('Профилирование функций через cProfile')
run('revers_1(n)')
run('revers_2(n)')
run('revers_3(n)')
run('from_tail_to_head(n)')

'''
Т.к. профайлер делает только 1 запуск, везде все по нулям. Мы можем увидеть только, что рекурсии делают кучу 
дополнительных вызовов.

Через timeit (из-за миллиона запусков в дефолте) видим, что рекурии работают дольше всех, как и должны.
А самый быстрый способ из предложенных - через простой разворот строки. 
Второй метод хуже из-за цикла с вычислениями, которого в третьем методе нет.
'''