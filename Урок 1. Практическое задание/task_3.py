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
firm_dict = {'JSC IVANOV': 1234567, 'PETROV CORP': 12345678, 'SomeFirm': 899899900,
             'UK 4SUNS': 10457, 'GOOGLE': 45896109283645, 'Intuitive Surgical': 948563728394}
firm_lst = []


# O(N log N)
def three_best_log(firm):
    return [sorted(firm.items(), key=lambda x: x[1], reverse=True)[i][0] for i in range(3)]


# O(N) хотя, честно, не знаю как оценить рекурсию =) представим, что оценил правильно =)
def three_best_n(dct, lst):
    if len(lst) == 3:
        return lst
    else:
        max_key = max(dct, key=lambda k: dct[k])
        lst.append(max_key)
        dct.pop(max_key)
    return three_best_n(dct, lst)


print(three_best_log(firm_dict), sep='\n')
print(three_best_n(firm_dict, firm_lst), sep='\n')
"""
При условии что сложность алгоритма 2 оценена верно, то эффективнее решение номер 2: 
- меньшая алгоритмическая сложность;
- требует меньше дополнительной памяти;
"""