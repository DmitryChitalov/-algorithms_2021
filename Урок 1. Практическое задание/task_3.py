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

import random

repository = {
    'name_1': random.randint(1, random.randint(2, 10000000)),
    'name_2': random.randint(1, random.randint(2, 10000000)),
    'name_3': random.randint(1, random.randint(2, 10000000)),
    'name_4': random.randint(1, random.randint(2, 10000000)),
    'name_5': random.randint(1, random.randint(2, 10000000)),
    'name_6': random.randint(1, random.randint(2, 10000000))}

print(repository)


def sorted_1(items_of_repo):

"""
	Сложность: O(n^2).

"""

    sorted_1_list = []   #O(1)

    for i in range(len(items_of_repo)):   #O(n)
        lowest_value_index = i                   #O(1)
        for j in range(i + 1, len(items_of_repo)):         #O(n)
            if items_of_repo[j][1] > items_of_repo[lowest_value_index][1]:       #O(1)
                lowest_value_index = j                 #O(1)
        items_of_repo[i], items_of_repo[lowest_value_index] = items_of_repo[lowest_value_index], items_of_repo[i]       #O(1)

    for i in range(len(items_of_repo[:3])):           #O(1)
        sorted_1_list.append(f'{items_of_repo[i][0]}: {items_of_repo[i][1]}.')            #O(1)

    return sorted_1_list           #O(1)


print(sorted_1(list(repository.items())))

#############################################################################################################


def sorted_2():

"""
	Сложность: O(n).

"""

    lst = []       #O(1)
    lst_of_3_max = []        #O(1)

    for value in repository.values():     #O(1)
        lst.append(value)                  #O(1)
        
    for i in range(3):                    #O(1)
        lst_of_3_max.append(max(lst))      #O(1)
        lst.remove(max(lst))               #O(n)

    return lst_of_3_max                   #O(1)                      


print(sorted_2())


Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""