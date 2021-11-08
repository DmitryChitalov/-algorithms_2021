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

companies_profit_info = {'OOO "Ромашка"': 10,
                         'ИП "Вася Пупкин"': 100,
                         'OOO "Какие люди"': 1000,
                         'ООО "Восмиклассница"': 10000,
                         'ООО "Главбуха нет"': 100000,
                         'ООО "Вите надо выйти"': 1000000}


# Решение №1:
# Сложность: O(n log n)


def top3_profit1(storage):
    count = 3                                                   # O(1)
    top3_lst = []                                               # O(1)
    for key in sorted(storage, key=storage.get, reverse=True):  # O(n + n log n) = O(n log n)
        if count != 0:                                          # O(1)
            top3_lst.append(key)                                # O(1)
            count -= 1                                          # O(1)
        else:
            return top3_lst                                     # O(1)


print(top3_profit1(companies_profit_info))


# Решение №2:
# Сложность: O(n log n)


def top3_profit2(storage):
    storage_lst = list(storage.items())                 # O(n)
    storage_lst.sort(key=lambda x: x[1], reverse=True)  # O(n log n)
    top3_lst = storage_lst[:3]                          # O(n)
    return top3_lst                                     # O(1)


print(top3_profit2(companies_profit_info))


# Решение №3:
# Сложность: O(n^2)


def top3_profit3(storage):
    top3 = []                            # O(1)
    storage_lst = list(storage.items())  # O(n)
    max_val = storage_lst[0][1]          # O(1)
    count = 3                            # O(1)
    while count != 0:                    # O(n)
        for item in storage_lst:         # O(n)
            if item[1] > max_val:        # O(1)
                max_val = int(item[1])   # O(1)
        for item in storage_lst:         # O(n)
            if item[1] == max_val:       # O(1)
                top3.append(item)        # O(1)
                storage_lst.remove(item) # O(n)
                max_val = 0              # O(1)
        count -= 1                       # O(1)

    return top3                          # O(1)


print(top3_profit3(companies_profit_info))


"""
В моём понимании самое эффективное решение из мной предложенных - решение №2, т.к. в данном алгоритме не создаётся 
никаких дополнительных переменных, не используется цикл для перебора значений, а также потому что решение 
более компактное и читабельное.
"""