
# СКРИПТЫ ЗАДАЧИ №1
'''
    Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
'''

from memory_profiler import profile

n = 500

# Решение задачи через цикл for
print('Первая реализация ЗАДАЧИ №1')
@profile
def sum_row_for(n, rez, el):
    for i in range(n):
        rez = rez + el
        el = el / -2
    print(f'Количество элементов: {n}, их сумма: {rez}')


sum_row_for(n, 0, 1)

# Решение задачи через рекурсию
print('Вторая реализация ЗАДАЧИ №1')


@profile
def sum_row_recur(num):

    def sum_row(n, rez, el):
        if n > 0:
            return sum_row(n - 1, rez + el, el / -2)
        return rez

    print(f'Количество элементов: {num}, их сумма: {sum_row(num, 0, 1)}')


sum_row_recur(n)

'''
    Замеры показывают, что рекурсия не значительно, но требует больше памяти, в связи с хранением стека вызовов.
'''
