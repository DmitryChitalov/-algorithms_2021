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
# Второе решение лучше и короче, так как мы не добавляем значение в новый список => не создаем переменную и не используем аppend
# Сложность O(n)
# 2 решение более эффективное, потому что в нем не заложен двойной проход по элементам, как в первом решении.

# Сложность O(n^2)

def sorted(rand_l):
    for i in range(len(rand_l)):
        lowest_value_index = i
        for j in range(i + 1, len(rand_l)):
            if rand_l[j][1] > rand_l[lowest_value_index][1]:
                lowest_value_index = j
                rand_l[i], rand_l[lowest_value_index] = rand_l[lowest_value_index], rand_l[i]
                return rand_l[:3]


data = {'Rosneft': 1, 'Lukoil': 2, 'Surgutneftegaz': 3, 'Bashkirneft': 4, 'Gazpromneft': 5}
val = list(data.items())
for i in sorted(val):
    print(i[0], ':', i[1])

#  Сложность O(n log n)

data_2 = {'Rosselhoz':1, 'Sberbank':2, 'MTS': 3, 'Vtb': 4, 'Alpha': 5}

val = list(data_2.items())
val.sort(key=lambda i: i[1], reverse=True)
for i in range(3):
    print(val[i][0], ':', val[i][1])