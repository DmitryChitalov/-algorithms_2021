""" Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка
   и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.
   Операцию clear() не используем.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских
функций и примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты."""

from random import random
from time import time


def time_calc(func):
    """Декоратор для замеров времени выполнения функций"""
    def wrapper(obj, items):
        start_time = time()
        res = func(obj, items)
        res_time = time() - start_time
        print(f'Замер времени для ф-ции: {func.__name__}(), эл-тов:'
              f' {len(items):,d}, время: {res_time:.6f} сек.')
        return res, res_time
    return wrapper


@time_calc
def lst_fill(curr_lst: list, elements):     # O(n)
    """Заполняет список переданными элементами"""
    curr_lst = [elem for elem in elements]  # O(n)
    return curr_lst                         # O(1)


@time_calc
def dct_fill(curr_dct: dict, elements):                          # O(n)
    """Заполняет словарь переданными элементами, ключи - индекс эл-тов"""
    curr_dct = {idx: elem for idx, elem in enumerate(elements)}  # O(n)
    return curr_dct                                              # O(1)


@time_calc
def lst_insert_end(curr_lst: list, items):  # O(n)
    """Вставляет в конец переданного списка переданные элементы"""
    for item in items:          # O(n)
        curr_lst.append(item)   # O(1)
    return curr_lst             # O(1)


@time_calc
def lst_insert_begin(curr_lst: list, items):  # O(n**2)
    """Вставляет в начало переданного списка переданные элементы"""
    for item in items:              # O(n)
        curr_lst.insert(0, item)    # O(n)
    return curr_lst                 # O(1)


@time_calc
def dct_insert(curr_dct: dict, items):          # O(n)
    """Вставляет в словарь переданные значения, ключи - индексы по порядку"""
    last_dct_idx = len(curr_dct)                # O(1)
    for idx, item in enumerate(items):          # O(n)
        curr_dct[last_dct_idx + idx] = item     # O(1)
    return curr_dct                             # O(1)


@time_calc
def lst_del_end(curr_lst: list, items):  # O(n)
    """Удаляет с конца переданного списка cnt-элементов"""
    for _ in range(len(items)):          # O(n)
        curr_lst.pop()                   # O(1)
    return curr_lst                      # O(1)


@time_calc
def lst_del_begin(curr_lst: list, items):  # O(n**2)
    """Удаляет из начала переданного списка cnt-элементов"""
    for _ in range(len(items)):            # O(n)
        curr_lst.pop(0)                    # O(n)
    return curr_lst                        # O(1)


@time_calc
def dct_del(curr_dct: dict, items):        # O(n)
    """Удаляет из словаря cnt-элементов, по ключам - индексам эл-тов"""
    for idx in range(len(items)):          # O(n)
        curr_dct.pop(idx)                  # O(1)
    return curr_dct                        # O(1)


if __name__ == '__main__':

    # тестовые кол-ва элементов
    test_counts = 100000, 1000000, 10000000
    CNT_EL_100k = 100000  # кол-во элементов для вставки, удаления
    CNT_EL_1k = 1000      # кол-во элементов для вставки, удаления

    # задание а) замеры времени по заполнению элементами
    for test_cnt in test_counts:
        # генерим заданное кол-во случайных элементов
        test_set_task_1a = tuple(random() for _ in range(test_cnt))

        test_lst, test_dct = [], {}
        test_lst, test_time_lst = lst_fill(test_lst, test_set_task_1a)
        test_dct, test_time_dct = dct_fill(test_dct, test_set_task_1a)

        print(f'Разница во времени заполнения list() и dict() при '
              f'{len(test_set_task_1a):,d} элементов - '
              f'{(test_time_dct / test_time_lst):.2f} раз\n')

    # задание б) замеры прочих операций со словарем и списком

    # операция вставки элементов
    test_set_task_1b = tuple(random() for _ in range(CNT_EL_100k))

    # вставка в начало - очень затратна - возьмем немного меньше эл-тов
    test_set_task_1k = tuple(random() for _ in range(CNT_EL_1k))
    test_lst_beg, test_time_lst_beg = lst_insert_begin(test_lst,
                                                       test_set_task_1k)
    test_lst_end, test_time_lst_end = lst_insert_end(test_lst, test_set_task_1b)
    test_dct, test_time_dct = dct_insert(test_dct, test_set_task_1b)

    print(f'Разница во времени вставки list() и dict() при '
          f'{len(test_set_task_1b):,d} элементов (в конец списка):'
          f' {(test_time_dct / test_time_lst_end):.2f} раз\n')

    # операция удаления элементов
    # удаление из начала списка - очень затратно - возьмем немного меньше эл-тов
    test_lst_beg, test_time_lst_beg = lst_del_begin(test_lst, test_set_task_1k)
    test_lst_end, test_time_lst_end = lst_del_end(test_lst, test_set_task_1b)
    test_dct, test_time_dct = dct_del(test_dct, test_set_task_1b)

    print(f'Разница во времени удаления list() и dict() при '
          f'{len(test_set_task_1b):,d} элементов (из конца списка):'
          f' {(test_time_dct / test_time_lst_end):.2f} раз\n')

"""
а) Несмотря на одинаковую принципиальную линейную сложность добавления 
элементов в список и словарь - по замерам в словарь добавление элементов 
происходит медленнее в 2-2,5 раза, что по всей видимости связано с 
необходимостью проведения ряда служебных операций в словаре "под капотом" 
(создание хеша для ключа и др.

б) Операция вставки и удаления:
- вставка/удаление в начало списка - сложность O(n**2), т.к. происходит 
пересчет всех индексов. 
Словарь здесь безусловно выигрывает, особенно при больших кол-вах элементов.
- вставка/удаление в конец списка и в словарь - сложность O(n), но т.к. в 
словаре опять есть доп. накладные расходы "под капотом", то разница примерно 
в 2 раза по времени сохраняется.

Операции получения произвольного элемента - проверять смысла не вижу - и так 
все понятно:
- список - O(1) - если по индексу и O(n) - по значению.
- словарь - O(1) - по ключу и O(n) - по значению.
"""