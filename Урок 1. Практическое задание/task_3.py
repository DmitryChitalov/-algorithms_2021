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
compani = {"rogaAndKopita": 1300, "samiSUsami": 1500, "umelieRuki": 5000, "compA": 700, "compB": 300, "compC": 1200}
# 1
"""O(n**4 + n**2)"""
three_max = [0]                                                 # O(1)
for i in compani:                                               # O(n)
    if compani[i] > min(three_max):                             # O(n)
        if 3 > len(three_max):                                  # O(1)
            three_max.append(compani[i])                        # O(1)
        else:
            three_max.remove(min(three_max))                    # O(n**2)
            three_max.append(compani[i])                        # O(1)
for i in three_max:                                             # O(n)
    for j in compani:                                           # O(n)
        if i == compani[j]:                                     # O(1)
            print(j)                                            # O(1)


# 2
"""O(n log n)"""
three_max_god_pr = list(compani.values())                    # O(len(...))
three_max_god_pr.sort()                                      # O(n log n)
three_max_god_pr = three_max_god_pr[-3:]                     # O(k+n)
for i in compani:                                            # O(n)
    if compani[i] in three_max_god_pr:                       # O(1)
        print(f'{i} this compani have three max pribl in year')     # O(1)

""" второй алгоритм лучше т.к.меньше кол-ва вложенных операции над данными и более оптимальны по сложности"""