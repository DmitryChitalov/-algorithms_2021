
"""
Задание 3. (На РЕВЕРС) Вебинар 17:00
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Обязательно предложите еще свой вариант решения и также запрофилируйте!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
Без аналитики задание считается не принятым
"""

# Профилировка – это измерение производительности всей программы и ее фрагментов.
# Модуль cProfile - Регистрирует функции и время их выполнения в сек., предоставляет разработчику подробную статистику замеров.

from cProfile import run # импортируем модуль и вызваем его функцию run
from timeit import timeit

# Рекурсия Сложность О(2^n - Экспоненциальная) Самая медленная
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)
print(revers_1(123593, revers_num=0))

# Цикл Сложность О(n)
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num
print(revers_2(45936, revers_num=0))

# Срез Сложность О(1) !!!!!!
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num
print(revers_3(7129))

# Функция reversed() Сложность О(n) - ЛУЧШЕ 1-ых 2-ух
def revers_4(enter_num):
    enter_num = str(enter_num)
    revers_num = ''.join(reversed(list(enter_num)))
    return revers_num
print(revers_4(369169))

def main():
    revers_1(enter_num, revers_num=0)
    revers_2(enter_num, revers_num=0)
    revers_3(enter_num)
    revers_4(enter_num)


#run('main()')

"""
  ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 Задание 3.py:53(main)
"""

# 1-ЫЙ замер:
print(f'Рекурсия :', timeit("revers_1", globals=globals(), number=1000))
# print(timeit("func_1", setup="from __main__ import func_1", number=1000)) # Аналог предыдущего

# 2-ОЙ замер:
print(f'Цикл :', timeit("revers_2", globals=globals(), number=1000))

# 3-ИЙ замер:
print(f'Срез :', timeit("revers_3", globals=globals(), number=1000))

# 4-ЫЙ замер:
print(f'Функция reversed :', timeit("revers_4", globals=globals(), number=1000))

"""
НЕ ПОНЯТНЫЙ рез-тат!!! Исходя из сложностей. Если я их правильно определил

Рекурсия : 1.6999999999999654e-05
Цикл : 1.7799999999998373e-05
Срез : 1.910000000000106e-05
Функция reversed : 1.6999999999999654e-05


"""