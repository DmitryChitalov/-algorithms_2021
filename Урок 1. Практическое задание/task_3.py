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
import random
def rnd_str(num=3):
    """ Возвращает случайную строку символов. Параметр - ее длина. По умолчанию 3"""
    out_str =''
    for i in range(num):
        new_char = chr(random.randint(65,122))
        if new_char.isalpha():
            out_str = out_str + new_char
        else:
            i -= 1
    return out_str

def rnd_company(num = 100):
    """Возвращает список уникальных названий фирм. Параметр задает количество. По умолчанию 100"""
    company_set = set()
    while len(company_set) < num:
        company_set.add(rnd_str(random.randint(5,10)))
    return company_set

def method_1():
    """ Сложность O(N)"""
    company_lst = list(rnd_company())
    revenue_lst = [(company_lst[i],random.randint(0,10000)) for i in range(100)]
    top_lst = []
    top_lst.append(revenue_lst[0])
    for el in revenue_lst:
        if el[1] > top_lst[len(top_lst)-1][1]:
            if len(top_lst) > 2:
                top_lst = top_lst[1:]
                top_lst.append(el)
            else:
                top_lst.append(el)
    print("Три компании с наибольшей выручкой")
    for el in top_lst:
        print(f'{el[0]}  {el[1]}')

def method_2():
    """Квадратичная сложность"""
    company_lst = list(rnd_company())
    revenue_lst = [(company_lst[i],random.randint(0,10000)) for i in range(100)]
    n = len(revenue_lst)
    for i in range(n):
        for j in range(0, n-i-1):
            if revenue_lst[j][1] > revenue_lst[j+1][1] :
                revenue_lst[j], revenue_lst[j+1] = revenue_lst[j+1], revenue_lst[j]
    print("Три компании с наибольшей выручкой")
    for el in revenue_lst[len(revenue_lst)-3:]:
        print(f'{el[0]}  {el[1]}')

method_1()
method_2()
