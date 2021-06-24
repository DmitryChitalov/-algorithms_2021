"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.
Без аналитики задание считается не принятым!
"""

from timeit import timeit


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'

def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'

def func_3():
    count_list_num = [array.count(i) for i in array]
    index_max_count = max(count_list_num)
    return f'Чаще всего встречается число {array[(count_list_num.index(index_max_count))]}' \
            f' оно появилось в массиве {index_max_count} раз(а)'



array = [1, 3, 1, 3, 4, 5, 1]

timeit_func_1 = timeit('''
def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'
''')

timeit_func_2 = timeit('''
def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'
''')

timeit_func_3 = timeit('''
def func_3():
    count_list_num = [array.count(i) for i in array]
    index_max_count = max(count_list_num)
    return f'Чаще всего встречается число {array[(count_list_num.index(index_max_count))]}' \
            f' оно появилось в массиве {index_max_count} раз(а)'
''')


print(f'\n{func_1()}. \nВремя выполнения func_1: {timeit_func_1}')
print(f'\n{func_2()}. \nВремя выполнения func_2: {timeit_func_2}')
print(f'\n{func_3()}. \nВремя выполнения func_3: {timeit_func_3}')



'''
Вывод: Удалось обойтись без циклов, рекурский и выполнить всё с помощью представления списков. Сложность 
        представлений ниже, поэтому и скорость выполнения ниже, что было озвучено в прошлых задачах.
        
Время выполнения func_1: 0.0499244
Время выполнения func_2: 0.057891999999999985
Время выполнения func_3: 0.042440000000000005

        Хотя после того, как запустил несколько раз данный код, то по результатам победитель оказался другой
        
Время выполнения func_2: 0.041823200000000005

        А ещё после нескольких запусков (конечно не больше прошлого рельтата func_2), но тоже неплохой результат
        
Время выполнения func_1: 0.041862500000000004
        
        В общем грубо говоря время почти одинаковое у всех фукнций.
'''
