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


def highest_profit(dict_obj):
    """
    Алгоритм 1: Функция получает словарь вида {имя компании: годовой доход}, находим компанию с
    максимальным доходом, заносим название в конец списка самых прибыльных компаний, повторяем поиск
    еще два раза исключая уже найденые компании из поиска. На вывод генерируем список, упорядоченый
    по убыванию дохода.

    Сложность: 0(n^2).
    """
    best_company = ''
    names_ordered_by_profit = []
    for _ in range(3):                                                  # O(1)
        max_profit = 0
        for k, val in dict_obj.items():                                   # 0(n)
            if val > max_profit and k not in names_ordered_by_profit:     # 0(n)
                max_profit = val
                best_company = k
        names_ordered_by_profit.append(best_company)                    # 0(1)
    return [f'{k} - {dict_obj[k]}' for k in names_ordered_by_profit]    # 0(n)


def highest_profit_2(dict_obj):
    """
    Алгоритм 2: Создается список со значениями дохода компаний взятыми из словаря с данными,
    далее находим максмимальное значение в списке, оно удаляется из списка, далее ищем по
    значению элемент словаря и добавляем его в список top_3, повторяем еще 2 раза.

    Сложность: 0(n)
    """
    profits_list = list(dict_obj.values())      # 0(n)
    top_3 = []                                  # 0(1)
    for _ in range(3):                          # 0(1)
        max_profit = max(profits_list)          # 0(n)
        profits_list.remove(max_profit)         # 0(n)
        for k, val in dict_obj.items():           # 0(n)
            if val == max_profit:                 # 0(1)
                top_3.append(f'{k} - {val}')      # 0(1)
    return top_3                                # 0(1)


COMPANIES = {
    'Industrial & Commercial Bank of China': 45783,
    'Apple': 57411,
    'SoftBank Group': 47053,
    'Saudi Aramco': 49287,
    'Microsoft': 44281}
print(highest_profit(COMPANIES))
print(highest_profit_2(COMPANIES))

# Вывод: второе решение эффективней, потому что сложность у него ниже, этого удалось
# достичь благодаря избвлению от проверки на вхождение в список 'k not in names_ordered_by_profit'.
