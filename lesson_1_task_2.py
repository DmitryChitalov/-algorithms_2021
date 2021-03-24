import random

def alg_1(lst_obj):
##  Сложность : O(n**2) - срез в цикле
    for j in range(len(lst_obj)):
        if lst_obj[j] <= min(lst_obj[j+1:]):
            return lst_obj[j]


def alg_2(lst_obj):
##  Сложность : O(n) - цикл
    min = lst_obj[0]
    for el in lst_obj:
        if el < min:
            min = el
    return min

lst = random.sample(range(0, 100),5)    #генерация какого-то списка чисел
print(lst)
print(alg_1(lst))
print(alg_2(lst))