""" Задание 4.

Приведены два алгоритма. В них определяется число, которое встречается в
массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и
по-возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым!"""

from collections import Counter
from random import randint
from timeit import repeat


def func_1(elems):
    # сложность O(n**2)
    max_freq, most_freq_el = 0, 0
    for el in elems:
        freq = elems.count(el)
        if freq > max_freq:
            max_freq, most_freq_el = freq, el
    return f'чаще всего встречается число {most_freq_el}, ' \
           f'оно появилось в массиве {max_freq} раз(а)'


def func_2(elems):
    # сложность O(n**2)
    freq_elems = []
    for el in elems:
        freq = elems.count(el)
        freq_elems.append(freq)

    max_freq = max(freq_elems)
    most_freq_elem = elems[freq_elems.index(max_freq)]
    return f'чаще всего встречается число {most_freq_elem}, ' \
           f'оно появилось в массиве {max_freq} раз(а)'


def func_3(elems):
    """Использование коллекции collections.Counter"""
    # сложность O(n log n)
    stats = Counter()
    for el in elems:
        stats[el] += 1
    # print(f'{stats=}\n{stats.most_common(1)=}')
    most_freq_el, most_freq = stats.most_common(1)[0]
    return f'чаще всего встречается число {most_freq_el}, ' \
           f'оно появилось в массиве {most_freq} раз(а)'


if __name__ == '__main__':
    START_NUM, END_NUM = 0, 20    # числа в случ. массиве от и до
    CNT_ELEMS = 1000              # кол-во чисел в массиве
    CNT_RUNS, CNT_RPT = 30, 5     # кол-во запусков и повторов замеров

    array = tuple(randint(START_NUM, END_NUM) for _ in range(CNT_ELEMS))

    print('Тесты функций по поиску наиболее часто встречающегося числа\n'
          f'в массиве случайных {CNT_ELEMS:,d} чисел со значениями от'
          f' {START_NUM} до {END_NUM}):\n {array[:10]} ... {array[-10:]}')
    print(f'Функция {func_1.__name__}(): {func_1(array)}')
    print(f'Функция {func_2.__name__}(): {func_2(array)}')
    print(f'Функция {func_3.__name__}(): {func_3(array)}')

    # замеры через timeit
    for idx in range(1, 4):
        stm_func_str = f'func_{idx}(array)'
        time_it = min(repeat(stm_func_str, globals=globals(),
                             number=CNT_RUNS, repeat=CNT_RPT))
        print(f'Замер {CNT_RUNS:,d} запусков скрипта func_{idx}(): '
              f'{time_it:.4f} сек.')

"""
Вроде бы обращаться из функции к "внешним" сущностям - не по феншую. Прокинул в 
функции 1 и 2 массив явным образом, также переименовал для большей 
"прозрачности" переменные. Убрал код самого скрипта в блок '__main__'. 
Как видим - перебор каждого элемента и поиск по нему частоты встречи во всем 
массиве (сложность - O(n**2)) - при больших кол-вах элементов - плох. Это 
- обе функции 1 и 2.
Использование же встроенной коллекции collections.Counter - существенно 
сокращает время выполнения задачи и дает хорошую сложность - O(n log n). 
"""