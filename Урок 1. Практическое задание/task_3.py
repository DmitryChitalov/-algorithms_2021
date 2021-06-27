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

my_storage = {'Рога и копыта': 20034, 'Stratton Oakmont': 50432, 'Umbrella': 45256,
              'Acme Corporation': 28475, 'Morley': 95724, 'Duff': 7462}


def find_winners_1(dict_obj):
    profit_sorted = sorted(dict_obj.values(), reverse=True)  # O(n log n) + O(1)
    winners = {}  # O(1)
    for i in profit_sorted[:3]:  # O(1)
        for k in dict_obj.keys():  # O(n) + O(1)
            if dict_obj[k] == i:  # O(1)
                winners[k] = dict_obj[k]  # O(1)
    print(winners)  # O(1)


# Сложность: (O(n log n) + O(1)) + O(1) + O(1) * (O(n) + O(1)) * O(1) + O(1) + O(1)=
# = O(n log n)

def find_winners_2(dict_obj):
    company_names = sorted(dict_obj, key=dict_obj.get, reverse=True)  # O(n log n) + O(1)
    winners = {}  # O(1)
    for name in company_names[:3]:  # O(1)
        winners[name] = dict_obj[name]  # O(1)
    print(winners)  # O(1)


# Сложность: O(n log n) + O(1) + O(1) + O(1) * O(1) + O(1)=
# = O(n log n)

def find_winners_3(dict_obj):
    inverted_values = sorted([(v, k) for (k, v)
                              in dict_obj.items()], reverse=True)  # O(n log n) + O(n) + O(1)
    winners = [(v, k) for (k, v) in inverted_values[:3]]  # O(1)
    print(winners)


# Сложность: O(n log n) + O(n) + O(1) + O(1)
# = O(n log n)

def find_winners_4(dict_obj):
    values_list = list(dict_obj.values())  # O(n) + O(1)
    counter = 1  # O(1)
    while counter < len(values_list):  # O(1)
        for i in range(len(values_list) - counter):  # O(n)
            if values_list[i] > values_list[i + 1]:  # O(1)
                values_list[i], values_list[i + 1] = values_list[i + 1], values_list[i]
                # O(1)
        counter += 1                     # O(1)
    for j in values_list[-3:]:           # O(1)
        for k, val in dict_obj.items():  # O(n)
            if val == j:                 # O(1)
                print(k, val)            # O(1)


# Сложность: O(n) + O(1) + O(1) + O(1) * O(n) * O(1) * O(1) + O(1) + O(1) * O(n) * O(1) * O(1)=
# = O(n)

# Вывод: с точки зрения краткости кода - лучшее решение 2 или 3, с точки зрения сложности
# по О-нотации - 4. Эффективность оценивается в зависимости от того, что важнее в конкретном случае.

find_winners_1(my_storage)
find_winners_2(my_storage)
find_winners_3(my_storage)
find_winners_4(my_storage)
