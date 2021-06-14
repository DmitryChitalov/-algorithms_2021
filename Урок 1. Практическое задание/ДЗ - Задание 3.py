  
"""
Задание 3. 18:40 - В решённых примерах Вебинара 2
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

#  Вариант - O(nlog n) - т.к. sorted()
import operator

base_сomp_sort = sorted(base_сompany.items(), key = operator.itemgetter(1))# ортировать словарь по значению
# base_сomp_sort = sorted(base_сompany.items(), key = operator.itemgetter(0))# ортировать словарь по ключу
print(base_сomp_sort)
print(type(base_сomp_sort))
print(base_сomp_sort[-3:])
#print(base_сomp_sort[-3:][0][0], " : ", base_сomp_sort[-3:][0][1])
for i in base_сomp_sort[-3:]: # Сложность - O(n)
    print(i[0], ':', i[1])



# первый вариант - O(N^2)
def sorted_1(random_list):
    for i in range(len(random_list)):
        lowest_value_index = i
        for j in range(i + 1, len(random_list)):
            if random_list[j][1] > random_list[lowest_value_index][1]:
                lowest_value_index = j
    # Сложность - O(N^2)- Так как цикл вложенный в другой цикл - ДОМИНАНТ
        random_list[i], random_list[lowest_value_index] = random_list[lowest_value_index], random_list[i]# Сложность - O(1)
    return random_list[0:3]


list_from_dictionary = list(base_сompany.items()) # Сложность - O(1)
#print(list_from_dictionary )
for i in sorted_1(list_from_dictionary): # Сложность - O(n)
    print(i[0], ':', i[1])

print('#' * 18)


# !!!!!!!!!!!!!!! третий вариант - O(N)
def three_max(list_input):
    input_max = {}
    list_d = dict(list_input)
    for i in range(3): # range(3), а не range(n) Сложность - O(1)
        maximum = max(list_d.items(), key=lambda k_v: k_v[1])# max, min - в словаре. Сложность - O(n) - ДОМИНАНТ
        # ПРИМЕР: max(list(...)) - max - O(n), list(...) - O(n) - Рез-щая Сложность - O(n)+O(n)=O(n)
        del list_d[maximum[0]]
        input_max[maximum[0]] = maximum[1]
    return input_max


print(three_max(base_сompany))

# второй вариант - O(N*logN)
list_from_dictionary = list(base_сompany.items())
list_from_dictionary.sort(key=lambda i: i[1], reverse=True)# Сортировка sort() Сложность - O(n) - ДОМИНАНТ
for i in range(3): # Обычный цикл Сложность - O(n)
    print(list_from_dictionary[i][0], ':', list_from_dictionary[i][1])

print('#' * 18)

"Лучшим вариантом будет третий, т.к. имеет минимальную вычислительную " \
"сложность и решает поставленную задачу без изменение исходного словаря " \
"и без лишней сортировки"

"""