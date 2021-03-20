"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Если у вас возникают сложности, постарайтесь подумать как можно решить задачу,
а не писать "мы это не проходили)".
Алгоритмизатор должен развивать мышление, а это прежде всего практика.
А без столкновения со сложностями его не развить.

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
"""

import random

def algorithm_1(incomming_dict):    # O(N)   эффективнее чем O(NlogN), так как с увеличением числа входящих элементов, сложность возрастает медленнее 
    input_dict = dict(incomming_dict)
    drawn_companies = {}
    for draw in range(3):
        maximum_value = 0
        must_be_drawn = -1
        for dict_element_title,dict_element_value in input_dict.items():    # O(N)
            if dict_element_value > maximum_value:
                maximum_value = dict_element_value
                must_be_drawn = dict_element_title
        drawn_companies[must_be_drawn] = input_dict[must_be_drawn]
        input_dict.pop(must_be_drawn,None)
                
    return drawn_companies


def algorithm_2(incomming_dict):    # O(NlogN)   медленнее чем O(N)
    input_dict = dict(incomming_dict)
    sorted_dict = sorted(input_dict.items(),key=lambda x:x[1],reverse=True) # O(NlogN)
    drawn_companies = dict(sorted_dict[:3])        
    return drawn_companies


companies = ["Company_1","Company_2","Company_3","Company_4","Company_5","Company_6"]
companies_dict = {}
for company in companies:
    companies_dict[company] = random.choice(range(0, 100000))


print(companies_dict)
print(algorithm_1(companies_dict))  
print(algorithm_2(companies_dict))