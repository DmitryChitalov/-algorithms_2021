""" Эркуру домашнее задание 1 Задача 3
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


 d = dict(Comp1 = 100, Comp2 = 500, Comp3 = 1000, Comp4 = 12300, Comp5 = -100, Comp6 = 12, Comp7 = 14000)

#первый вариант решения

def max_three_companies(company_dict):
    
    if len(company_dict) < 3:
        result = 'в списке меньше трех компаний'
    elif len(company_dict) == 3:
    	comp_list = list(company_dict.keys())
        result = com_list
    else:
    	invert_dict ={}
    	for Comp in company_dict:
    		invert_dict.update({company_dict[Comp], Comp})
        valuelist = list(company_dict.values())
        valuelist.sort()
        i = 1
        complist = []
        while i < 4:
        	complist.append(invert_dict[valuelist[i-1]])
        	i = i + 1
        result = complist
    return result

#сложность O(N log N) (по сложности третьей ветки условия)


#второй вариант решения
def max_three_companies_extra(company_dict):
    """поиск максимального значения в одном цикле  """
    complist = {}
    max1 = 0
    max2 = 0
    max3 = 0
    for comp in company_dict:
        if max1 = 0:
    	    max1 = company_dict[comp]
    	    com1 = comp
    	elif max2 = 0:
    		max2 = company_dict[comp]
    		com2 = comp
        elif max3 = 0:
        	max3 = company_dict[comp]
        	com3 = comp
   
    for comp in company_dict:
        currentsum = company_dict[comp]
        if currentsum > max1:
            max1 = currentsum
            com1 = comp
        elif currentsum > max2:
        	max2 = currentsum
        	com2 = comp
        elif currentsum > max3:
        	max3 = currentsum
        	com3 = comp
    complist = [com1, com2, com3]

    return complist

#во втором варианте используется только два обхода списка, без сортировок, поэтому общая сложность O(N) + O(N) = O(N)  
#итого общая сложность первого алгоритма выше, хотя он короче и симпатичней второго на вид


