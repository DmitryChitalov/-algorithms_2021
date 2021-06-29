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


class Company:

    def __init__(self, name, profit):
        self.name = name
        self.profit = profit

    def __str__(self):
        return f"{self.name} - {self.profit}"


company_list = []
for i in range(1, 10001):
    company_list.append(Company(f"Company {i}", random.randint(100, 1000000)))


def sort_leaders(data: list):
    """
    Функция использует стандартную сортировку со сложностью О(n * log(n))
    Выводит в консоль три самых прибыльных компании
    """
    data.sort(key=lambda c: c.profit)
    for idx in range(1, 4):
        print(data[-idx])


def find_3_leaders(data: list):
    """
    Функция выводит в консоль три самых прибыльных компании
    Компании ищутся прямым перебором списка компаний и решается за 3 прохода, сложность О(n)
    :param data:
    :return:
    """
    leaders = []
    index = []
    max_profit = data[0].profit
    temp_idx = 0
    temp_cmp = data[0]
    for count in range(3):
        for idx, company in enumerate(data):
            if company.profit > max_profit and idx not in index:
                max_profit = company.profit
                temp_idx = idx
                temp_cmp = company
        leaders.append(temp_cmp)
        index.append(temp_idx)
        max_profit = 0
    [print(i) for i in leaders]


sort_leaders(company_list)
print()
find_3_leaders(company_list)

"""
Второй должен работать быстрее если в списке больше 1000 компаний ( log(1000) = 3 )
"""
