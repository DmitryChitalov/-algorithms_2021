company = {'apple': 5040, 'nokia': 2200, 'nestle': 3514, 'samsung': 17252, 'romashka': 25145,
                'nike': 9251, 'adidas': 2351}

random_company = list(company.items())

"""1. Cложность алгоритма О(n^2)"""


def max_income(my_list):
    for el in range(len(my_list)):
        max_income_company = el
        for v in range(el + 1, len(my_list)):
            if my_list[v][1] > my_list[max_income_company][1]:
                max_income_company = v
        my_list[el], my_list[max_income_company] = my_list[max_income_company], my_list[el]


max_income(random_company)
print(random_company[0:3])

"""2. Сложность алгоритма O(n log n)"""
sorted_pairs = sorted(((k, v) for k, v in company.items()),
                      key=lambda pair: pair[1], reverse=True)

print(sorted_pairs[0:3])


"""Решение 2 более эффективно, по скольку имеет сложность О(n log n)
это означает, что при увелеченни объема входящих данных, врямя на обработку будет затрачено
меньше, чем при использовании первого варианта """
