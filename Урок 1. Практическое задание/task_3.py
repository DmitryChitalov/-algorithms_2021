"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
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

companies_profits = {
    "Enigma": 1150,
    "ZORO": 980,
    "ABC-advance": 2470,
    "IT space": 740,
    "Constalletion": 78,
    "ONB": 9871,
    "Easy move": 190,
    "GDD": 999,
    "IT-karma": 0,
    "SUP": 8496
}

# Решение 1:
def get_top_three_1(dict_obj):  # доминирующая сложность линейная O(N)
    top_three = {}  # O(1)
    transit_dict = dict_obj.copy()  # O(N)
    while len(dict_obj) - len(transit_dict) < 3:  # O(1) константная, число итераций - 3
        max_profit = 0  # O(1)
        for c, p in transit_dict.items():
            if p > max_profit:  # O(1)
                max_profit = p  # O(1)
                company = c  # O(1)
        top_three[company] = max_profit  # O(1)
        del transit_dict[company]  # O(1)
    return top_three  # O(N) зависит от длины


print(f'top three companies ranged by year profit: {get_top_three_1(companies_profits)}')
print()


# Решение 2:
def get_top_three_2(dict_obj):  # доминирующая сложность линейная O(N)
    profits_list = list(dict_obj.values())  # O(N) зависит от числа элементов
    companies_list = list(dict_obj.keys())  # O(N)
    while len(profits_list) != 3:  # O(1) константная, число итераций - 3
        min_profit = profits_list[0]  # O(1)
        for i in range(len(profits_list)): # O(N) зависит от числа элементов
            if profits_list[i] <= min_profit:  # O(1)
                min_profit = profits_list[i]  # O(1)
                idx = i  # O(1)
        del profits_list[idx]  # O(N)
        del companies_list[idx]  # O(N)
    return dict(zip(companies_list, profits_list))  # O(len(...))- сложность dict (зависит от длины
    # аргумента, здесь это N),  O(N) - сложность zip. Итоговая  O(N)


print(f'top three companies ranged by year profit: {get_top_three_2(companies_profits)}')
print()


# Решение 3:
def get_top_three_3(dict_obj):  # доминирующая сложность логарифмическая O(N*logN)
    ranged_dict_obj = {}  # O(1)
    sorted_keys = sorted(dict_obj, key=dict_obj.get)  # O(N*logN) по аналогии с .sort для списка
    for c in sorted_keys:  # O(N)
        ranged_dict_obj[c] = dict_obj[c]  # O(1)
        k = 0  # O(1)
    for c, p in ranged_dict_obj.items():  # O(N)
        k += 1  # O(1)
        if k > len(ranged_dict_obj) - 3:  # O(1) + O(1) - подсчет длины и сравнение
            print(c + ':', p, end='  ')  # O(1)
    print('- ', end=' ')  # O(1)
    return ('top three companies ranged by year profit')  # O(1)


print(get_top_three_3(companies_profits))
print()


# Решение 4:
def get_top_three_4(dict_obj):  # доминирующая сложность линейная O(N)
    top_three = {}
    dict_obj_1 = dict(dict_obj)
    for i in range(3):
        maximum = max(dict_obj_1.items(), key=lambda k_v: k_v[1])
        del dict_obj_1[maximum[0]]
        top_three[maximum[0]] = maximum[1]
    return top_three

print(get_top_three_4(companies_profits))


# Вывод: 1,2,4 варианты имеют линейную сложность - самая оптимальная из предложенных вариантов решений,
# ВАРИАНТ 3 имеет линейно-логарифмическую сложность, он хуже линейной
