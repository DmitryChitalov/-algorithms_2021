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

# Делаю предположение что не может быть одинаковой прибыли у разных компаний (для того чтобы не усложнять код).

companies = {
    'IBM': 6000000,
    'Microsoft': 7000000,
    'Oracle': 5000000,
    'Google': 6500000,
    'Apple': 6700000,
    'Lenovo': 3000000,
    'Asus': 4300000
}


# O (N Log N)
def profit1(companies_dict):
    companies_list = list(companies_dict.items())                           # O(N)
    companies_list.sort(key=lambda i: i[1], reverse=True)                   # O(N Log N)
    max_profit_companies_list = [item[0] for item in companies_list[:3]]    # 0(3)
    return max_profit_companies_list                                        # 0(1)


# O(N)
def profit2(companies_dict):
    companies_dict_working = companies_dict.copy()                          # O(N)
    max_profit_companies_list = list()                                      # O(1)
    for i in range(3):                                                      # O(3)
        max_profit = 0                                                      # O(1)
        max_profit_company = None                                           # O(1)
        for k, v in companies_dict_working.items():                         # O(N)
            if max_profit < v:                                              # O(1)
                max_profit = v                                              # O(1)
                max_profit_company = k                                      # O(1)
        companies_dict_working.pop(max_profit_company)                      # O(1)
        max_profit_companies_list.append(max_profit_company)                # O(1)
    return max_profit_companies_list                                        # O(1)


# O(N)
def profit3(companies_dict):
    max_profit_companies_list = list()                                      # O(1)
    profits_list = list(companies_dict.values())                            # O(N)
    for i in range(3):                                                      # O(3)
        max_profit = max(profits_list)                                      # O(N)
        profits_list.remove(max_profit)                                     # O(1)
        for k, v in companies_dict.items():                                 # O(N)
            if v == max_profit:                                             # O(1)
                max_profit_companies_list.append(k)                         # O(1)
    return max_profit_companies_list                                        # O(1)

# Решения 2 и 3 кажутся более эффективными потому что O(N) эффективнее O(N Log N).
# Решение 2 кажется более эффективным чем 3, потому что ынем меньшее количество O(N), но не уверен :-)


print(profit1(companies))
print(profit2(companies))
print(profit3(companies))
