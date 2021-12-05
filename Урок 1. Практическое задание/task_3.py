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

d = dict(short='dict', long='dictionary')

firms = dict(
    Лукойл=8036,
    Магнит=1237,
    Сургутнефтегаз=1867,
    X5_Retail_Group=1533,
    Татнефть=810,
    МТС=480
)
n = 3
"---------------------------------------------------------------------------"


def func_1(dic):   # O(1)
    lst = list(dic.values())  # O(n)
    lst.sort()  # O(n log n)
    count = 0  # O(1)
    while count < n:  # O(1)
        for k, v in dic.items():   # O(n)
            if v == lst[len(lst)-1]:   # O(1)
                print(k, v)   # O(1)
                lst.pop()   # O(1)
                count += 1   # O(1)


func_1(firms)  # сложность ф-ции O(n log n) линейно-логарифмическая


"---------------------------------------------------------------------------------------------------------------------"


def func_2(dic):   # O(1)
    lst = list(dic.items())   # O(n)
    l = len(lst)   # O(1)
    for i in range(l):   # O(n)
        for j in range(0, l-1):   # O(n)
            if lst[j][1] > lst[j+1][1]:   # O(1)
                lst[j], lst[j+1] = lst[j+1], lst[j]   # O(1)
    return lst[l-1], lst[l-2], lst[l-3]   # O(1)


print(func_2(firms))   # O(n2) квадратичная сложность


"-------------------------------------------------------------------------------------------"


# O(n) - линейная сложность т к выводим только три значения независимо от их количества
def func_3(dic):   # O(1)
    max_val = max(firms.items(), key=lambda item: item[1])   # O(n)
    dic.pop(max_val[0])  # O(1)
    return max_val   # O(1)


for i in range(n):    # O(1)   # n=3 всегда
    print(func_3(firms))    # O(n)


"""
Вывод: последнее решение быстрее и лаконичнее предыдущих. C увеличением кол-ва входных 
данных темп роста операций будет возрастать не так стремительно как в предыдущих решениях
"""


# key2 = max(dic, key=lambda k: dic[k])
# print("The key with the largest value:", key2)




