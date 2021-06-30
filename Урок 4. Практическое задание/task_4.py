"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
from timeit import timeit

array = [1, 3, 1, 3, 4, 5, 1, 5, 5, 5]

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
    my_dict = {}
    for el in array:
        if el not in my_dict.keys():
            my_dict[el] = array.count(el)
    n = sorted(my_dict.items(), key= lambda x: x[1])[len(my_dict)-1][0]
    return f'Чаще всего встречается число {n}, ' \
           f'оно появилось в массиве {my_dict.get(n)} раз(а)'

def func_4():
    n = max(array, key=array.count)
    return f"Чаще всего встречается число {n}, оно появилось в массиве {array.count(n)} раз(а)"


print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(timeit("func_1()", globals=globals()))
print(timeit("func_2()", globals=globals()))
print(timeit("func_3()", globals=globals()))
print(timeit("func_4()", globals=globals()))

'''
    Самым долгим получается 3 способ реализации решения задачи из-за создания словаря, где ключом
является элемент массива, а значение ключа количество повторений, а затем выполнение сортировки 
словаря по значению для выборки последнего элемента словаря как максимального значения.
    Самым быстрым и лаконичным является 4 способ из-за прямого доступа к максимальному элементу счетчика.
'''