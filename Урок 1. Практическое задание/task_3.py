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

# Словарь для сортировки.
company_profits = dict(huawei=2000.78, mercedes=1000.34, adidas=700.24, puma=350.28, ecco=468.47, kia=987.27,
                       yandex=1500.47, google=5000.45, asus=3500.79, logitech=1300.49, microsoft=7896.14,
                       samsung=2598.46, xiaomi=1398.47, apple=4698.41)


def get_max_profit_company_1(counter, corp_profits):
    """ Вариант первый. Используем встроенную функцию сортировки sorted.
        Сложность: O(n log n)
    """

    if counter == 0 or counter > len(corp_profits):  # O(1)
        counter = len(corp_profits)  # O(1)
    # Реализация скрыта.
    sorted_dict = dict(sorted(corp_profits.items(), key=lambda item: item[1], reverse=True))  # O(n log n)
    count = int()  # O(1)
    final_dict = dict()  # O(1)
    for k, v in sorted_dict.items():  # O(N)

        if count == counter:  # O(1)
            break

        final_dict[k] = v  # O(1)
        count += 1  # O(1)

    return final_dict  # O(1)


# Вывод 1-го варианта.
print(f"Var 1 sort_dict: {get_max_profit_company_1(3, company_profits)}")


# Далее 2-е функции второго варианта. Сортировака выбором.
def find_max_from_dict(dict_obj):
    """ Функция позволяющая найти максимальное значение переданного value словаря.
        Сложность: O(N).
    """
    max_item_val = list(dict_obj.items())[0]  # O(N)
    for x in list(dict_obj.items()):  # O(N)
        if max_item_val[1] < x[1]:  # O(1)
            max_item_val = tuple(x)  # O(1)

    return max_item_val  # O(1)


def get_max_profit_company_2(counter, corp_profits):
    """ Основная функция, возвращает counter элементов отсортированного по убыванию value словаря.
        Сложность: похоже, что O(N^2). Но я сомневаюсь. Возможно в цикле нужно считать O(N) * O(N) * O(N) = O(N^3).
        Выводы: Логарифмическая сложность предпочтительнее, чем квадратичная или кубическая. 
    """
    if counter == 0 or counter > len(corp_profits):  # O(1)
        counter = len(corp_profits)  # O(1)

    final_dict = dict()  # O(1)
    for _ in range(counter):  # O(N)
        max_value = find_max_from_dict(corp_profits)  # O(N)
        final_dict[max_value[0]] = corp_profits.pop(max_value[0])  # O(1) + O(N)

    return final_dict  # O(1)


# Вывод 2-го варианта.
print(f"Var 2 sort_dict: {get_max_profit_company_2(3, company_profits)}")

# Словарь для сортировки.
company_profits = dict(huawei=2000.78, mercedes=1000.34, adidas=700.24, puma=350.28, ecco=468.47, kia=987.27,
                       yandex=1500.47, google=5000.45, asus=3500.79, logitech=1300.49, microsoft=7896.14,
                       samsung=2598.46, xiaomi=1398.47, apple=4698.41)


# Вариант 3. Быстрая сортировка. Рекурсия.
def get_sort_dict(dict_obj):
    """ Функция рекурсивно сотрирует словарь.
        Сложность: Похоже, что O(N log N).
    """
    if len(dict_obj) < 2:
        return dict_obj
    else:
        # Берем первый элемент.
        start_element = list(dict_obj.items())[0]           # O(N)

        less_start = dict()                                 # O(1)
        for i in list(dict_obj.items())[1:]:                # O(N)
            if i[1] > start_element[1]:                     # O(1)
                less_start[i[0]] = i[1]                     # O(1)

        greater_start = dict()                              # O(1)
        for i in list(dict_obj.items())[1:]:                # O(N)
            if i[1] <= start_element[1]:                    # O(1)
                greater_start[i[0]] = i[1]                  # O(1)

        start_dict = dict()                                 # O(1)
        start_dict[start_element[0]] = start_element[1]     # O(1)

        return get_sort_dict(less_start) | start_dict | get_sort_dict(greater_start)    # O(N log N)


def get_max_profit_company_3(counter, corp_profits):
    """ Основная функция, возвращает counter элементов отсортированного по убыванию value словаря.
        Сложность: # O(N log N)
        Выводы: Логарифмическая сложность предпочтительнее, чем квадратичная. Время выполнения O(N log N)
        быстрее чем О(N^2), а с увеличением размера словаря, оно становится ещё быстрее.
    """
    if counter == 0 or counter > len(corp_profits):  # O(1)
        counter = len(corp_profits)  # O(1)

    sorted_dict = get_sort_dict(company_profits)  # O(N log N)

    count = int()  # O(1)
    final_dict = dict()  # O(1)
    for k, v in sorted_dict.items():  # O(N)

        if count == counter:  # O(1)
            break

        final_dict[k] = v  # O(1)
        count += 1  # O(1)

    return final_dict  # O(1)


# Вывод 3-го варианта.
print(f"Var 3 sort_dict: {get_max_profit_company_3(3, company_profits)}")
