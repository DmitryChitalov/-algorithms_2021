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

data = {'name1': 10000, 'name2': 15000, 'name3': 20000, 'name4': 12000, 'name5': 17000}

# 1)  придумайте 2-3 решения (не менее двух)
# a) Сложность O(N log N) (Линейно-логарифмическая)

third_income = sorted(data.values(), reverse=True)[2]  # O(N log N)

for key, value in data.items():  # O(N)
    if value >= third_income:  # O(1)
        print(key, value)  # O(1)

# b) Сложность O(N log N) (Линейно-логарифмическая)

sorted_data = {key: value for key, value in sorted(data.items(), key=lambda item: item[1], reverse=True)}  # O(N log N)

for i, (key, value) in enumerate(sorted_data.items()):  # O(N)
    if i < 3:  # O(1)
        print(key, value)  # O(1)
    else:
        break  # O(1)

# c) Сложность O(N) (Линейная)


(third_key, third_value), (second_key, second_value), (first_key, first_value) = \
    (None, float('-inf')), (None, float('-inf')), (None, float('-inf'))

for key, value in data.items():  # O(N)
    if value >= first_value:  # O(1)
        if value >= second_value:  # O(1)
            if value >= third_value:  # O(1)
                first_value = second_value  # O(1)
                first_key = second_key  # O(1)
                second_value = third_value  # O(1)
                second_key = third_key  # O(1)
                third_value = value  # O(1)
                third_key = key  # O(1)
            else:
                first_value = second_value  # O(1)
                first_key = second_key  # O(1)
                second_value = value  # O(1)
                second_key = key  # O(1)
        else:
            first_value = value  # O(1)
            first_key = key  # O(1)

print((third_key, third_value), (second_key, second_value), (first_key, first_value))

# 3) Третье решение самое выгодное, т.к. его сложность - линейная. Следовательно, с ростом количества элементов,
# время выполнения будет уменьшаться медленнее, чем в двух других решениях.
