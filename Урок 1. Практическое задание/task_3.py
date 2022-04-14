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


# хранилище ('название компании': годовая прибыль), значения прибыли - выдуманы и не уникальны
data = {
    'google': 111,
    'sber': 222,
    'moderna': 789,
    'apple': 879,
    'micron': 888,
    'gazprom': 888,
    'uber': 123,
    'VTB': 444,
    'qualcomm': 999,
    'sanofi': 555,
    'facebook': 456,
    'tesla': 765,
    'samsung': 777,
    'cisco': 879,
}


# ------------------------------algorithm no. 1------------------------------

import random


def get_sort_list(list_values):
    '''
    param list_values: a list of numbers and / or real numbers
    return: sorted list of values

    complexity: O(N Log N)
    '''
    if len(list_values) > 1: # O(1)
        random_value = list_values[random.randint(0, len(list_values)-1)] # O(N)
        smaller_values = [elmt for elmt in list_values if elmt < random_value] # O(N)
        equal_values = [elmt for elmt in list_values if elmt == random_value] # O(N)
        greater_values = [elmt for elmt in list_values if elmt > random_value] # O(N)
        list_values = get_sort_list(smaller_values) + equal_values + get_sort_list(greater_values)
    return list_values

    # К сожалению, я не могу определить сложность этого алгоритма, конечно я подсмотрел его
    # с Internet и по задумке тут должна быть O(N Log N) сложность. В принципе, я понимаю как
    # он работает, проблемы с определением сложности функции random.randint() - думаю, что O(N),
    # так как подозреваю, что без цикла не обошлось в ней. Проблема с определение сложности генераторов
    # - логика следующая: там есть цикл и .append() = O(N). 
    # И самая большая проблема: я пока не понял как оценить рекурсию... Она O(1)? так как тут
    # просто  переменную возращается результат вызова или как =0 ??? 
    # Если дадите развернутые обьяснения, ссылки - буду под впечатлением =) точно.
    # А так я просто надеюсь, что "сдул" правильно, оставив ту же сложность, что и в источнике - O(N Log N).


def get_top_companies(dictionary, n_top):
    '''
    param dictionary: dictionary where values ​​are integers or natural.
    param n_top: top how much to show? 
    При чём, если будет указано 4 (конкретно только для этого примера с этим словарем data
    без уникальный значений), то в итоговом списке будет 5 значений из-за
    отсутствия этой уникальности в значениях словаря.
    return: not unique sorted list by number and value

    complexity: О(N^2)
    '''
    list_val = get_sort_list(list(dictionary.values())) # O(N Log N)
    top_values = list_val[-n_top:] # O(N)
    top_list_companies =[f'Годовая прибыль {dictionary[el]}$ компании {el}' for el in dictionary
        if dictionary[el] in top_values] # O(N) или О(N^2) - скорей всего второй вариант,
        # так как мозг подсказывает, что тут цикл O(N) в который вложен поиск по списку O(N),
        # а значит весь этот генератор = O(N^2)
    return get_sort_list(top_list_companies) # O(1)
    
top_companies = get_top_companies(data, 3)
print(f'{"="*20} algorithm no. 1 {"="*20}\n {top_companies}')


# Вывод: скорей всего всё это, имеет квадратичную сложность в лучшем случае
# Я упорно пытаюсь избежать решения с функцией sort() и lambda или max(), 
# хотя наверное зря.
# Стоит попробывать с ними.


# ------------------------------algorithm no. 2------------------------------


def get_top_companies_(dictionary):
    '''
    param dictionary: dictionary where values ​​are integers or natural.
    return: an ascending list of tuples with values, where each tuple is unique
    Будет добавлен тот кортеж, который будет первым с нужным значением.

    complexity: О(N^2)
    '''
    sort_val = sorted(dictionary.values()) # O(N log N)
    new_sor_dict = {} # O(1)

    for value in sort_val: # O(N)
        for key in dictionary.keys(): # O(N)
            if dictionary[key] == value: # O(1)
                new_sor_dict[key] = dictionary[key] # O(1)
                break
    return list(new_sor_dict.items())[-3:] # O(1)

    # Цикл в цикле = О(N^2)
    # Попробуем улучшить в следушем примере.


top_companies_= get_top_companies_(data)
print(f'{"="*20} algorithm no. 2 {"="*20}\n {top_companies_}')

# Вывод (я пишу их после того как написал функцию):
# я все же использовал встроенную функцию srted() и все же получил 
# квадратичную сложность =(, точная зная (видел на форумах), что
# использование lambda и sort можно получить O(N log N) 


# ------------------------------algorithm no. 3------------------------------


def get_top_companies__(dictionary):
    '''
    param dictionary: dictionary where values ​​are integers or natural.
    return: new sorted dictionary by values

    complexity: O(N log N) ?????
    '''
    if len(dictionary) >= 1: # O(1)
        random_value = list(dictionary.items())[random.randint(0, len(dictionary)-1)][1] # O(N)
        smaller_values = {elmt[0]:elmt[1] for elmt in dictionary.items() if elmt[1] < random_value} # O(N)
        equal_values = {elmt[0]:elmt[1] for elmt in dictionary.items() if elmt[1] == random_value} # O(N)
        greater_values = {elmt[0]:elmt[1] for elmt in dictionary.items() if elmt[1] > random_value} # O(N)
        list_values = {**get_top_companies__(smaller_values), **equal_values, **get_top_companies__(greater_values)}  # O(N) ????
    else:
        return {} # O(1)
    return list_values # O(1)

    # Здесь мне так же трудно оценить сложность функции, по идеи за каркас взята функция сортировки списка
    # что в алгоритме №1. Там эта функция должна быть O(N log N) сложности.
    # Может мне удалось перенести подход и уровень сложности со списка на словарь..


top_companies__= list(get_top_companies__(data).items())  
print(f'{"="*20} algorithm no. 3 {"="*20}\n {top_companies__[-3:]}')

# В этой попытке добился своего бзика и не использывал встроенных  функций
# но так увлекся, что забыл про ТОП 3, а не просто свести задачу к сортировке,