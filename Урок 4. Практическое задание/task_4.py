"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1]


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
    new_arr = sorted(array, key=array.count, reverse=True)
    return f'Чаще всего встречается число {new_arr[0]}, ' \
           f'оно появилось в массиве {new_arr.count(new_arr[0])} раз(а)'

def func_4():
    max_el = max(array, key=array.count)
    max_count = array.count(max_el)
    return f'Чаще всего встречается число {max_el}, '\
           f'оно появилось в массиве {max_count} раз(а)'

print(func_1())
print(func_2())
print(func_3())
print(func_4())

array = range(1000)
func_list = ['func_1', 'func_2', 'func_3', 'func_4']
print('Сравним варианты :')
for el in func_list:
    print(f'Функция {el}:', timeit(el+'()', number=10000, globals=globals()))

'''
Да, скорость выполнения задачи удалось увеличить.
Резкльтат:
Сравним варианты :
Функция func_1: 3.015254271
Функция func_2: 3.6519072670000003
Функция func_3: 2.030573747000001
Функция func_4: 2.0151317100000004

Честно говоря, предполагал, что func_4 отработает существенно быстрее func_3, 
т.к. при этом не требуется строить новый отсортированный список...  
При изменении количества элементов массива, ситуация с замерами не изменилась.
'''
