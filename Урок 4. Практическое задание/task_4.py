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
    numb = max(array, key=array.count)
    return f'Чаще всего встречается число {numb}, ' \
           f'оно появилось в массиве {array.count(numb)} раз(а)'

def func_4():
    """ Мой вариант """
    el = max([array.count(x) for x in range(len(array))], key=array.count)
    return el, array.count(el)

# print(func_3())
# print(func_1())
# print(func_2())
# print(func_4())
print(timeit("func_1()", globals=globals(), number=1000000))
print(timeit("func_2()", globals=globals(), number=1000000))
print(timeit("func_3()", globals=globals(), number=1000000))
print(timeit("func_4()", globals=globals(), number=1000000))
"""
2.388198 - func_1()
3.2504465490000003 - func_2()
2.6908026290000002 - func_3()
4.971323535 - func_4()

func_4() - это мой вариант до разбора ДЗ, хотел поэксперементировать, но в итоге это 
самая долгая по времени ф-я - почти 5 сек. У нее сложность O(n), когда у func_3() тоже O(n),
но работает быстрее, за счёт чего?. Моя ф-я не эталон, но для статистики сойдет, для понимания.
Одно не пойму: ведь func_1() и func_2() тоже линейная сл. и операций больше, почему они 
быстрее выполняются? 
"""