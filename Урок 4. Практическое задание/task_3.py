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
import cProfile
from random import randint
from timeit import timeit

TEST_NUM = randint(100000, 1000000)


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
    enter_num = str(enter_num)
    res = ''
    for i in range(len(enter_num)-1, -1, -1):
        res += enter_num[i]
    return res


def revers_5(enter_num):
    enter_num = list(str(enter_num))
    i = 0
    while i != len(enter_num):
        last = enter_num.pop()
        enter_num.insert(i, last)
        i += 1
    return ''.join(enter_num)


print(f'Фукнция revers_1', end=' ---> ')
print(timeit('revers_1(TEST_NUM)', globals=globals( )))
cProfile.run('revers_1(TEST_NUM)')
print(f'Фукнция revers_2', end='---> ')
print(timeit('revers_2(TEST_NUM)', globals=globals( )))
cProfile.run('revers_2(TEST_NUM)')
print(f'Фукнция revers_3', end='---> ')
print(timeit('revers_3(TEST_NUM)', globals=globals( )))
cProfile.run('revers_3(TEST_NUM)')
print(f'Фукнция revers_4', end='---> ')
print(timeit('revers_4(TEST_NUM)', globals=globals( )))
cProfile.run('revers_4(TEST_NUM)')
print(f'Фукнция revers_5', end='---> ')
print(timeit('revers_5(TEST_NUM)', globals=globals( )))
cProfile.run('revers_5(TEST_NUM)')

"""
Рекурсивная функция revers_1 показала один из самых медленных результатов, так как для реверса числа нам необходимо
будет осуществить такое количество вызова функции, которое было бы равно "длине" числа, что существенно замедляет время
выполнения.
Revers_2 по смыслу похожа на revers_1, однако, функция не требует дополнительных вызовов и просто осуществляет расчеты
и перезаписывает значения по ходу выполнения цикла.
Revers_3 оказалась самой быстрой. Мы пользуемся встроенными функциями, которые уже являются оптимизированными, что 
позволяет сократить время выполнения, также функция не производит никаких расчетов, а просто возвращает обратную строку.
Revers_4 по задумке похожа на revers_3, однако, реализует тот же функционал путём обхода от последнего индекса строки
к первому. В данной функции производится конкатенация строк, а также осуществляется больше вызовов сторонних функций.
Revers_5 является медленной функцией так как во время её выполнения мы вызовем выполним len(N) вызовов сторонних функций
особенное влияние на время выполнения окажет insert(), который будет производить вставку по индексу.
Таким образом, самой оптимальной функцией оказалась revers_3. 
"""