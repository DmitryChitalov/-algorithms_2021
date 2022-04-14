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

storage = [{"name": "ОАО Огород", "profit": 123456}, {"name": "Автомойка", "profit": 10000},
           {"name": "Яндекс", "profit": 999999}, {"name": "ООО Шашлычки без уксуса", "profit": 4345345345},
           {"name": "Агрохолдинг: Бессмысленное будуюещее", "profit": -3}, {"name": "Lorem", "profit": 11000}]


def top_profit_v1(company_list: list) -> list:
    """
        Сложность:
    """
    out = []
    for company in company_list:  # O(n)
        if len(out) < 3:  # O(1)
            out.append(company)  # O(1)
        else:
            for _ in range(len(out)):  # O(1)
                if company["profit"] > out[_]["profit"]:  # O(1)
                    out[0] = company  # O(1)
                    break  # O(1)
        out = sorted(out, key=lambda k: k["profit"])  # O(1) - потому что сложность sorted - O(nlog(n)),
        # но так как длина out всегде не более 3, то сложность будет
        # константной
    return out


print(top_profit_v1(storage))


def top_profit_v2(company_list: list) -> list:
    """
        Сложность: # O(n^2)
     """
    out = company_list[:]
    for company_idx in range(len(company_list)):  # O(n)
        for company_tmp_idx in range(len(company_list)):  # O(n)
            if out[company_tmp_idx]["profit"] > out[company_idx]["profit"]:  # O(1)
                tmp = out[company_idx]  # O(1)
                out[company_idx] = out[company_tmp_idx]  # O(1)
                out[company_tmp_idx] = tmp  # O(1)
    return out[-3:]  # O(1)


print(top_profit_v1(storage))
print(top_profit_v2(storage))
