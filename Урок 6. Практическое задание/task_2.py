"""
Задание 2.*
Предложить еще какие-либо варианты (механизмы, подходы, библиотеки, идеи)
для оптимизации памяти и
доказать!!! (наглядно, кодом) их эффективность (на примере профилировщика).
С урока ничего не дублир-ть. только новые способы
"""
from memory_profiler import profile

@profile
def number_sum(n):
    lst = list(range(n + 1))
    sum = 0
    for i in lst:
       sum += i
    del lst
    return sum

"""

"""
@profile
def number_sum_1(n):
    lst = (i for i in list(range(n + 1)))
    sum = 0
    for i in lst:
        sum += i

    return sum




if __name__ == '__main__':

    x = 100000
    print(f'Очистка переменной {number_sum(x)}')
    print(f'Использование генератора {number_sum_1(x)}')
