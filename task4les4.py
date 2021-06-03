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
    n = max(array, key=array.count)
    с = array.count(n)
    return  f'Чаще всего встречается число {n}, ' \
           f'оно появилось в массиве {с} раз(а)'


print(func_1())
print(func_2())
print(func_3())

""" Резудьтаты замеров:
0.0043229000000000045
0.004320699999999997
0.0033543000000000045
У меня получилось создать функцию, которая будет быстрее выше представленных. Он быстрее, так как в нем сразу находится нужное
нам максимальное число из первоначального массива. В первой функции идет перебор всех чисел списка по порядку, а во второй
создаются новые списки, что значительно удлинняет процесс выполнения функции.
"""




t1 = timeit("func_1()", globals=globals(), number=1000)
t2 = timeit("func_2()", globals=globals(), number=1000)
t3 = timeit("func_3()", globals=globals(), number=1000)
print(t1)
print(t2)
print(t3)