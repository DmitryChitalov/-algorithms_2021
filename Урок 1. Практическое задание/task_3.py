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

company = {
    'DHL': 1500000,
    'DPD': 2000000,
    'SBR': 2500000,
    'OTP': 3000000,
    'OMZ': 3500000,
    'BP': 4000000,
    'SHELL': 4500000
}

#сложность O(n^2)
def srch1(comp):
    for i in range(len(comp)):
        down = i
        for u in range(i + 1, len(comp)):
            if comp[u][1] > comp[down][1]:
                down = u
        comp[i], comp[down] = comp[down], comp[i]
    return comp[0:4]


print(company)
lst = list(company.items())
print(lst)
for i in srch1(lst):
    print(f'компания {i[0]} получает {i[1]}$ прибыли в год')

#честно говоря делал по аналогии вторго задания

#Сложность O(n log n)
def srch2(sum, low, high):
    central = sum[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while sum[i] < central:
            i += 1
        j -= 1
        while sum[j] > central:
            j -= 1
        if i >= j:
            return j
        sum[i], sum[j] = sum[j], sum[i]

#сложность рекурсии O(n)
def sort(sum):
    def re_sort(items, low, high):
        if low < high:
            split_index = srch2(items, low, high)
            re_sort(items, low, split_index)
            re_sort(items, split_index + 1, high)

    re_sort(sum, 0, len(sum) - 1)


end_list = []

for o in company.values():
    end_list.append(o)

sort(end_list)
for o in end_list[-3:]:
    print(f'компания {list(company.keys())[list(company.values()).index(o)]} заработала за год {o}$')

    
