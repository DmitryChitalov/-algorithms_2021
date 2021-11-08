#Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
#В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
#Сложность такого алгоритма: O(n^2) - квадратичная.

import random

def fan(lst):
    m = lst[0]
    for j in range(len(lst) - 1):
        for i in range(j + 1, len(lst)):
            if m > lst[i]:
                m = lst[i]
                break
    return m


for j in (5, 20):
     lst = random.sample(range(-100, 100), j)

print(fan(lst))



#Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
#Сложность такого алгоритма: O(n) - линейная.

def fan2(lst):
    m = lst[0]
    for i in range(1, len(lst), ):
        if m > lst[i]:
            m = lst[i]
    return m

print(fan2(lst))


