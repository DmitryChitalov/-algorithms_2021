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

companies = {
    "Company Z": 4052,
    "Company Y": 2100,
    "Company X": 7234,
    "Company A": 3248,
    "Company Q": 9487
}

# Вариант 1
# Сложность: O(N)

profitable = []                                                     # O(1)
sorter = sorted(companies, key=companies.get, reverse=True)[:3]     # предположительно O(1)
for key in sorter:                                                  # O(N)
    profitable.append((key, companies.get(key)))                    # O(1)
print(profitable)                                                   # O(1)

# Вариант 2
# Сложность: O(N^3)

profit = [moneys for moneys in companies.values()]  # Предположительно O(N)
profit.sort(reverse=True)                           # O(1)
for al in profit[:3]:                               # O(N)
    for name, money in companies.items():           # O(N)
        if money == al:                             # O(N)
            print(name, money)                      # O(1)

# Сложно было придумать алгорит в целом, но выбираю первый вариант, он кратче, проще и приятный на глаз
