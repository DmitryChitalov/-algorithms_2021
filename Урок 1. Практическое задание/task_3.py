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

base_сompany = {
    'yandex': 2000,
    'gazprom': 500,
    'microsoft': 2300,
    'perecrestok': 5400,
    'rosnano': 10,
    'appel': 2000,
    'biocad': 4030,
    'apteka': 299,
    'hiomi': 569,
    'wacom': 8901,
    'adidas': 4313,
    'acron': 6703
}


# первый вариант - O(N^2)
def sorted_1(random_list):
    for i in range(len(random_list)):
        lowest_value_index = i
        for j in range(i + 1, len(random_list)):
            if random_list[j][1] > random_list[lowest_value_index][1]:
                lowest_value_index = j
        random_list[i], random_list[lowest_value_index] = random_list[lowest_value_index], random_list[i]
    return random_list[0:3]


list_from_dictionary = list(base_сompany.items())
for i in sorted_1(list_from_dictionary):
    print(i[0], ':', i[1])

print('#' * 18)


# второй вариант - O(N*logN)
list_from_dictionary = list(base_сompany.items())
list_from_dictionary.sort(key=lambda i: i[1], reverse=True)
for i in range(3):
    print(list_from_dictionary[i][0], ':', list_from_dictionary[i][1])

print('#' * 18)


# третий вариант - O(N)
def three_max(list_input):
    input_max = {}
    list_d = dict(list_input)
    for i in range(3):
        maximum = max(list_d.items(), key=lambda k_v: k_v[1])
        del list_d[maximum[0]]
        input_max[maximum[0]] = maximum[1]
    return input_max


print(three_max(base_сompany))


"Лучшим вариантом будет третий, т.к. имеет минимальную вычислительную " \
"сложность и решает поставленную задачу без изменение исходного словаря " \
"и без лишней сортировки"
