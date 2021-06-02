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

"""
Выводим данные по компании и ее прибыли.
Предпочтительнее выглядит вариант 3, т.к. используется меньше кода + читабельнее)

1ый метод воспроизвел с помощью 2х функций - сложность O(n**2) (вызов из цикла со сложностью 0(n) функции с цилом 0(n) 
"""

def funct_data2(ebitda):
    max_ebitda = 0
    max_name = ''
    for key, value in ebitda.items():
        if max_ebitda < value:
             max_ebitda = value
             max_name = key
    return max_name

def funct_data(dict_comp):
    company_dict = {}
    dict_compcopy = dict_comp.copy()
    for i in range (3):
        m = funct_data2(dict_compcopy)
        company_dict[i]= {m, dict_compcopy.get(m)}
        del dict_compcopy[m]
    return company_dict

#Далее реализация 2 и 3 методов через сортировку, сложность обоих O(n log n)
def func_2data(dict_comp):
    company_lst = []
    for key, value in dict_comp.items():
        company_lst.append((value,key))
    company_lst.sort(reverse = True)
    return company_lst[:3]


def func_3data(dict_comp):
    company_lstsrt = sorted(dict_comp.items(), key=lambda x: x[1], reverse=True)[:3]
    return company_lstsrt

dict_comp = {'Samsung' : 200, 'Apple' : 150, 'Nokia' : 600, 'Xiomi' : 300, 'Motorola' : 100, 'SelecLine' : 800,
    'TOR' : 950, 'YandexPhone' : 350}

print(funct_data(dict_comp))
print(func_2data(dict_comp))
print(func_3data(dict_comp))