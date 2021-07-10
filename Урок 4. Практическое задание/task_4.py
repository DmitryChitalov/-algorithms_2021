"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
import timeit

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
    """ My with dict"""
    m = 0
    var = None
    work_dict = {}
    for el in array:
        if work_dict.get(el) is None:
            work_dict[el] = 1
        else:
            work_dict[el] += 1
        if work_dict[el] > m:
            m = work_dict[el]
            var = el
    return f'Чаще всего встречается число {var}, ' \
           f'оно появилось в массиве {m} раз(а)'

def func_4():
    """My better"""
    num = max(array,key=array.count)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'

print(timeit.timeit('func_1()',globals=globals()))
print(timeit.timeit('func_2()',globals=globals()))
print(timeit.timeit('func_3()',globals=globals()))
print(timeit.timeit('func_4()',globals=globals()))
print(func_4())
"""
1.4580239
1.9605932000000001
1.8465607
1.3089150999999997
Моя func_4 самая быстрая и короткая. Странно, что медленно работает вариант со словарем -
видимо слишком велики издержки на его создание. Все остальные результаты вполне ожидаемы.
"""
