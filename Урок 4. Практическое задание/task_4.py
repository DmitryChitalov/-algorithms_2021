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


def func_1(array):
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2(array):
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3(array):
    max_3 = max(zip((array.count(item) for item in set(array)), set(array)))
    return f'Чаще всего встречается число {max_3[1]}, ' \
           f'оно появилось в массиве {max_3[0]} раз(а)'


def func_4(array):
    max_4 = max(array, key=array.count)
    return f'Чаще всего встречается число {max_4}, ' \
           f'оно появилось в массиве {array.count(max_4)} раз(а)'


array_7 = [1, 3, 1, 3, 4, 5, 1]
print(array_7)
print(f'func_1:', timeit("func_1(array_7)", globals=globals(), number=100000))
print(f'func_2:', timeit("func_2(array_7)", globals=globals(), number=100000))
print(f'func_3:', timeit("func_3(array_7)", globals=globals(), number=100000))
print(f'func_4:', timeit("func_4(array_7)", globals=globals(), number=100000), '\n')

array_14 = [1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1]
print(array_14)
print(f'func_1:', timeit("func_1(array_14)", globals=globals(), number=100000))
print(f'func_2:', timeit("func_2(array_14)", globals=globals(), number=100000))
print(f'func_3:', timeit("func_3(array_14)", globals=globals(), number=100000))
print(f'func_4:', timeit("func_4(array_14)", globals=globals(), number=100000), '\n')

array_28 = [1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1]
print(array_28)
print(f'func_1:', timeit("func_1(array_28)", globals=globals(), number=100000))
print(f'func_2:', timeit("func_2(array_28)", globals=globals(), number=100000))
print(f'func_3:', timeit("func_3(array_28)", globals=globals(), number=100000))
print(f'func_4:', timeit("func_4(array_28)", globals=globals(), number=100000))

array_56 = [1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4,
            5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1]
print(array_56)
print(f'func_1:', timeit("func_1(array_56)", globals=globals(), number=100000))
print(f'func_2:', timeit("func_2(array_56)", globals=globals(), number=100000))
print(f'func_3:', timeit("func_3(array_56)", globals=globals(), number=100000))
print(f'func_4:', timeit("func_4(array_56)", globals=globals(), number=100000))

'''
[1, 3, 1, 3, 4, 5, 1]
func_1: 0.343953212
func_2: 0.343738939
func_3: 0.39408304699999985
func_4: 0.209225475 

[1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1]
func_1: 0.4251660479999999
func_2: 0.5570523629999999
func_3: 0.41038902900000007
func_4: 0.41730974200000004 

[1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1]
func_1: 1.2710713229999997
func_2: 1.5367617949999994
func_3: 0.5133716709999998
func_4: 1.2134634430000002
[1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 
4, 5, 1, 1, 3, 1, 3, 4, 5, 1, 1, 3, 1, 3, 4, 5, 1]
func_1: 4.298076151999999
func_2: 4.8222151140000005
func_3: 0.7899872750000014
func_4: 4.270885824999997


При небольшой длинне массива функции отрабатывают практически одинаково, 
но при увеличении длины массива дает большое приемущество дает фукция zip() (func_3) 
'''
