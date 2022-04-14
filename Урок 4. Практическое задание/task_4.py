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
    max_3 = max(array, key = array.count)
    count = array.count(max_3)
    return f'Чаще всего встречается число {max_3}, ' \
           f'оно появилось в массиве {count} раз(а)'


print(func_1())
print(func_2())
print(func_3())

t1 = timeit(f"func_1()", globals=globals(), number= 10000)
print(f'Время замера составило: {t1}')

t2 = timeit(f"func_2()", globals=globals(), number= 10000)
print(f'Время замера составило: {t2}')

t3 = timeit(f"func_3()", globals=globals(), number= 10000)
print(f'Время замера составило: {t3}')

#Время замера составило: 0.012146100000000003
#Время замера составило: 0.013721399999999995
#Время замера составило: 0.009967800000000006
#Вывод:третья функция работает быстрее тк:
#-она имеет меньшую сложность по сравнению с функцией 2 (цикл+ append)
#-состоит только из встроенных функций и не имеет цикла по сравнению с функцией 1
