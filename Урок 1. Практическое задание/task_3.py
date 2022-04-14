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

companies = {
    'company_1': 20000,
    'company_2': 30000,
    'company_3': 35000,
    'company_4': 1000,
    'company_5': 1000000
}

def find_top_three(comps):
    """O(N^2) если считать по большей сложности"""
    incomes = [v for v in comps.values()] # O(N)
    incomes.sort()  # O(N log N)
    # разобьем пошагово [company for company, income in companies.items() if income in incomes[-3:]]
    results = [] # O[1]
    for company, income in comps.items(): # O(N)
        if income in incomes[-3:]: # O(N)
            results.append(company) # O(1)
    return  results # O(1)

print(find_top_three(companies))

def find_top_three(comps):
    """N log N если считать по большей сложности"""
    tuples = [] # O(1)
    for k, v in comps.items():  # O(N)
        tuples.append((k, v))  # O(1)
    tuples.sort(key=lambda x: x[1])  # O(N log N)
    top_tuples = tuples[-3:]    # O(1)
    results = []    # O(1)
    for t in top_tuples:    # O(N)
        results.append(t[0])    # O(1)
    return results # O(1)

print(find_top_three(companies))


# Второе решение более эффективно, потому что сложность O(N log N) ниже, чем O(N^2)