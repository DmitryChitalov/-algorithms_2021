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

from operator import itemgetter

companies = [
    {'name': 'Ford', 'profit': 15000000},
    {'name': 'Toyota', 'profit': 10000000},
    {'name': 'Nissan', 'profit': 12000000},
    {'name': 'Lada', 'profit': 6000000},
    {'name': 'Lexus', 'profit': 23000000},
    {'name': 'Kia', 'profit': 25000000},
    {'name': 'Hyundai', 'profit': 19000000},
    {'name': 'Acura', 'profit': 12000000},
    {'name': 'GMC', 'profit': 8000000},
    {'name': 'Dodge', 'profit': 9000000},
    {'name': 'BMW', 'profit': 23000000},
    {'name': 'Mercedes', 'profit': 24000000},
    {'name': 'Audi', 'profit': 22500000},
    {'name': 'Volkswagen', 'profit': 223000000},
    {'name': 'Opel', 'profit': 2000000},
    {'name': 'ZAZ', 'profit': 1100000},
    {'name': 'Ferrari', 'profit': 14000000},
    {'name': 'Lamborghini', 'profit': 13000000},
    {'name': 'Lincoln', 'profit': 9000000},
    {'name': 'Suzuki', 'profit': 10004000},
    {'name': 'Geely', 'profit': 10006000},
    {'name': 'Great Wall', 'profit': 10008000},
    {'name': 'GAZ', 'profit': 1040000},
    {'name': 'Mazda', 'profit': 21000000}
]


# ------------------- Первый способ ------------------------------

def get_max_profit_companies_1(lst):
    """
    O(1) + O(N log N) + O(1) + О(1) = O(N logN), т.е.
    itemgetter + sorted + срез трех элементов + return
    ИТОГО: O(N log N)
    """
    return sorted(lst, key=itemgetter('profit'), reverse=True)[:3]


# ------------------- Второй способ ------------------------------

def get_max_profit_companies_2(lst):
    """
    Использование вложенных циклов - O(N**2)
    Далее построчно: O(N) + O(1) = O(N) - 79 строка
                     O(1) + O(N) = O(N) - 80
                     O(1) + O(N) = O(N) - 81
                     O(1) + O(1) + O(1) = O(1) - 82
                     O(1) + O(1) + O(1) = O(1) - 83
                     O(1) + O(1) = O(1) - 84

    ИТОГО: O(N**2)
    """
    new_lst = lst[:]
    for i in range(0, len(new_lst) - 1):
        for j in range(i + 1, len(new_lst)):
            if new_lst[j]['profit'] > new_lst[i]['profit']:
                new_lst[i], new_lst[j] = new_lst[j], new_lst[i]

    return new_lst[:3]


# ------------------- Третий способ ------------------------------

def get_max_profit_companies_3(lst):
    """
    Посрочно:
        O(N) + O(1) = O(N)
        O(1) + O(1) = O(1)
        3 раза по:
            O(1) + O(N) + O(1) = O(N)
            O(1)
            O(N)
        O(1)

    ИТОГО: O(N)
    """
    new_lst = lst.copy()
    max_profit_companies = []
    for i in range(3):
        max_profit_company = max(new_lst, key=lambda el: el['profit'])
        max_profit_companies.append(max_profit_company)
        new_lst.remove(max_profit_company)

    return max_profit_companies


print(f'Первый способ: {get_max_profit_companies_1(companies)}')  # Решение эффективнее, поскольку O(N log N)
print(f'Второй способ: {get_max_profit_companies_2(companies)}')
print(f'Третий способ: {get_max_profit_companies_3(companies)}')
