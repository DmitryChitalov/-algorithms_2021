"""
Задание 3.
Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
Задание творческое. Здесь нет жестких требований к выполнению.
"""

import random
import time


def my_timer(callback):
    """Функция секундомер, для подсказки"""
    def my_tmp(*args, **kwargs):
        start = time.perf_counter_ns()
        res = callback(*args, **kwargs)
        print("Время выполнения функции:", f'{(time.perf_counter_ns() - start)/(10**6):.03f}', 'мс', '\n')
        return res
    return my_tmp


@my_timer
def my_select_1(num_count, origin_dict):
    """Решение с копированием словаря и удалением содержимого из копии
    Сложность функции: O(n**2) <= O(n) + 4*O(1) + O(1) + O(n * n) + 4*O(1)
    """
    dict_corp_1 = origin_dict.copy()  # O(n)
    count, res_dict = 0, {}   # 4*O(1)
    while count < num_count:  # O(n), но так как второй параметр константа по заданию, то O(1)
        low_cost_corp = [k for k in dict_corp_1 if all(dict_corp_1[m] <= dict_corp_1[k] for m in dict_corp_1)]
        # O(log n) списки не хранят данные в сортированном виде
        res_dict.setdefault(low_cost_corp[0], dict_corp_1.get(low_cost_corp[0]))  # O(1)
        dict_corp_1.pop(low_cost_corp[0])  # O(1)
        count += 1  # O(1)
    return print(res_dict, '# O(n log n)')


@my_timer
def my_select_2(num_count, origin_dict):
    """Аналогичный первому выбор, только в обратку идет список из значений словаря
    Сложность функции: O(n**2) = O(10) + O(1) + O(n**2) + 4*O(1) + O(n**2) + 2*O(1)
    """
    money, res_dict_2 = list(origin_dict.values()), {}  # O(10) + O(1) + O(n**2)
    # money = [5, 9, 0, 2, 4, 3, 8, 1, 6, 7]
    for _ in range(len(money)):
        for n in range(len(money) - 1):  # O(n**2) - for in внутри for in
            if money[n] < money[n + 1]:  # O(1)
                a, b = money[n], money[n + 1]
                money[n], money[n + 1] = b, a  # O(1)
            elif money[n] >= money[n - 1] != money[len(money) - 1]:  # O(1)
                money[n], money[n - 1] = money[n - 1], money[n]   # O(1)
    for b in range(num_count):
        for k, v in origin_dict.items():        # O(n**2) - for in внутри for in
            if money[b] == v:                   # O(1)
                res_dict_2.setdefault(k, v)     # O(1)
    return print(res_dict_2, '# O(n**2)')


@my_timer
def my_select_3(num_count, origin_dict):
    """Сравнение части списка значений заданной длины, с остальной частью
    Сложность функции: O(n) =
    """
    my_lst = list(origin_dict.values())                 # O(1)
    my_res, res_dict_3 = my_lst[:num_count], {}         # 3*# O(1)
    my_res.sort(reverse=True)                           # O(n) максимум n,
    # так как ни в каком случае не будет требоваться весь список
    for idx in my_lst[num_count:]:                      # O(n) - т.к. остальная часть списка
        if idx > my_res[-1]:                            # O(1)
            my_res.pop()                                # O(1)
            my_res.append(idx)                          # O(1)
            my_res.sort(reverse=True)                   # O(1)
    for p in range(num_count):                          # O(1)
        my_dict = {k: v for k, v in origin_dict.items() if (my_res[p] == v)}  # O(1)
        res_dict_3.update(my_dict)                      # O(1)
    return print(res_dict_3, '# O(n)')                  # O(1)


""" Создание словаря """
dict_corp = {}
corporation = ['adidas', 'puma', 'nike', 'reebok', 'asos',
               'berton', 'spiders', 'grinders',
               'ИП Михалыч', '3AO Балтика', 'ВКО Алмаз-Антей']  # O(1) - константа присваивания
corporation.sort()  # O(n*Log(n)) - сортировка списка корпораций не уопрядочивает значения, а мне так приятнее

credit = random.sample(range(10 ** 6, 11 ** 6), len(corporation))  # O(1) - так как список корп объявлен константой
for i in range(len(corporation)):  # O(1) - константа: длина словаря задана в модуле
    dict_corp.setdefault(corporation[i], credit[i])

"""Вызов функций выбора"""
my_select_1(3, dict_corp)
my_select_2(3, dict_corp)
my_select_3(3, dict_corp)

"""
Задание 3. сделайте вывод, какое решение эффективнее и почему
my_select_1 - работает со значениями списка при этом сортировку проводит по ключам
my_select_2 - работает со значениями выделенными в список, что упрощает сортировку в половину для машины, 
но сохраняет общий уровень сложности такого алгоритма
my_select_3 - работает с частью списка
"""