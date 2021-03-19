"""
Задание 2.

Реализуйте два алгоритма.

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.

Не забудьте указать где какая сложность.

Примечание:
Построить список можно через списковое включение.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.
"""

import random
import time


def algorithm_1(lst_obj):   # O(n**2)
    for element_1 in lst_obj:
        is_minimal = 1
        for element_2 in lst_obj:
            if element_1 > element_2:
                is_minimal = 0
                break
        if is_minimal == 1:
            minimal_value = element_1    
        
    return minimal_value
    
def algorithm_2(lst_obj):   # O(n)
    minimal_value = None
    for element in lst_obj:
        if(minimal_value == None):
            minimal_value = element
        else:
            if element < minimal_value:
                minimal_value = element
        
    return minimal_value    

for j in (50, 500, 1000, 5000, 1000):
    lst = random.sample(range(-100000, 100000), j)


print(algorithm_1(lst)) # O(n**2)
print(algorithm_2(lst)) # O(n)