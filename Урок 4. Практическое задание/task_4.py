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
import collections


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


def my_func1():
    counts = {array.count(el): el for el in tuple(array)}
    answer = max(counts)
    return f'Чаще всего встречается число {counts[answer]}, ' \
           f'оно появилось в массиве {answer} раз(а)'


def my_func2():
    answer = collections.Counter(array).most_common(1)
    return f'Чаще всего встречается число {answer[0][0]}, ' \
           f'оно появилось в массиве {answer[0][1]} раз(а)'


print(func_1())
print(func_2())
print(my_func1())
print(my_func2())

print(timeit('func_1()', globals=globals()))
print(timeit('func_2()', globals=globals()))
print(timeit('my_func1()', globals=globals()))
print(timeit('my_func2()', globals=globals()))


"""
1.5709109790041111
1.9759373359847814
1.9328459029784426
3.7066746919881552

исходя из данных, самая быстрая функция - func_1
в my_func1 делаю через словарь - по скорости сравним со списком (что странно)
в my_func2 использую модуль collections и специально заточенную по это функцию Counter, 
что к моему удивлению привод к увеличению работы функции в 2 раза.
Варианта ускорить задачу не нашла =((
"""