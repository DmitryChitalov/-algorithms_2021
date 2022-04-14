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


def revers_4(enter_num):
    reverse_num = list(str(enter_num))
    reverse_num.reverse()
    return ''.join(reverse_num)


num = 121460
print(revers_1(num))
print(revers_2(num))
print(revers_3(num))
print(revers_4(num))
print(f'{"-" * 47}timeit{"-" * 47}')
print(f'Время работы revers_1: {timeit("revers_1(num)", globals=globals(), number=100000)}')
print(f'Время работы revers_2: {timeit("revers_2(num)", globals=globals(), number=100000)}')
print(f'Время работы revers_3: {timeit("revers_3(num)", globals=globals(), number=100000)}')
print(f'Время работы revers_4: {timeit("revers_4(num)", globals=globals(), number=100000)}')
print(f'{"-" * 46}сProfile{"-" * 46}')

run('revers_1(987416597246957)')
run('revers_2(987416597246957)')
run('revers_3(987416597246957)')
run('revers_4(987416597246957)')
"""
ИТОГ:
Проведя расчет с помощью timeit получили:
Время работы revers_1: 0.24445830000000002
Время работы revers_2: 0.1801162
Время работы revers_3: 0.05399660000000006
Время работы revers_4: 0.07808389999999998

С помощью cProfile получили практически идентичные таблицы с нулевыми значениями.

Алгоритм, использующий срез, (revers_3) оказался самым быстрым.
В отличии от других, этот алгоритм имеет константную сложность, ему не нужны дополнительные арифметические операции и
он не проходит по циклу, выполняя операции раз за разом. Четвертая функция практически повторяет срез, но использует
операции списка, что тормозит алгоритм.
"""