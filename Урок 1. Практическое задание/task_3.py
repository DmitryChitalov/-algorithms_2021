"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""


def get_max_profit_company(dc: dict):
    """
    O(N) + 0(N log N) + O(N) + O(N) * O(N) = O(N^2)
    :param dc:
    :return:
    """
    sort_ls = list(dc.values())  # O(len(dc.values)) + O(1) = O(N)
    sort_ls.sort()  # O(N log N)
    sort_ls = sort_ls[-3:]  # O(N)
    result = {}
    for row in dc:  # O(N)
        if dc[row] in sort_ls:  # O(N)
            result[row] = dc[row]
    return result


def get_max_profit_company_second(dc: dict, i=0, result=None):
    """
    O(1) + O(N) + O(1) + O(1) = O(N) * i = O(N^3)?
    :param dc:
    :param i:
    :param result:
    :return:
    """
    if result is None:
        result = {}
    if i >= 3:  # O(1)
        return result  # O(1)
    else:
        i -= -1  # O(1)
        max_val = max(dc.values())  # O(N) + O(1)
        for k, v in dc.items():  # O(N)
            if v == max_val:  # O(1)
                dc.pop(k)  # O(1)
                result[k] = v  # O(1)
                return get_max_profit_company_second(dc, i, result)


def main():
    """
    Решение get_max_profit_company() будет эффективнее засчет меньшего количества циклов,
     что ведет к более эффективным показателям в нотации O-большое.
     Что не маловажно, проще для понятия и реализации
    :return:
    """
    from random import randint

    start, end = 1000, 100000

    dict_co = {f"CO {row}": randint(start, end) for row in range(randint(4, randint(5, 15)))}

    print(f'Сгенерированные данные: {dict_co}\n')
    first, second = get_max_profit_company(dict_co), get_max_profit_company_second(dict_co)
    print(f"Топ 3-и компании по прибыли за год: {first}")
    print(f"Топ 3-и компании по прибыли за год: {second}\n")
    if first == second:
        print('Оба ответа совпадают.')


main()
