"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой и по возможности самой лаконичной.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым!
"""
from collections import Counter
import random
from timeit import timeit

# Заполним массив 100 элементами.
array = []  # [1, 3, 1, 3, 4, 5, 1]
for _ in range(100):
    array.append(random.randint(1, 9))
print(array)


def func_1():
    """
    Сложность O(N)
    """
    m = 0
    num = 0
    for i in array:  # O(N)
        count = array.count(i)  # O(1)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:  # O(N)
        count2 = array.count(el)  # O(1)
        new_array.append(count2)  # O(1)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    """
    Сложность: Похоже, что O(N log N)
    """
    count_dict = Counter(array)
    max_key = max(array, key=count_dict.get)
    return f'Чаще всего встречается число {max_key}, ' \
           f'оно появилось в массиве {count_dict.get(max_key)} раз(а)'


def func_4():
    """
    Сложность O(N)
    """
    max_key = max(array, key=array.count)
    return f'Чаще всего встречается число {max_key}, ' \
           f'оно появилось в массиве {array.count(max_key)} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())

print("func_1: ", timeit(stmt="func_1()", number=100000, globals=globals()))
print("func_2: ", timeit(stmt="func_2()", number=100000, globals=globals()))
print("func_3: ", timeit(stmt="func_3()", number=100000, globals=globals()))
print("func_4: ", timeit(stmt="func_4()", number=100000, globals=globals()))

"""
Добавлена функция 3 и 4.

Время работы при 100 элементах в массиве:
func_1:  9.0255671
func_2:  9.8371873
func_3:  1.0443467999999996
func_4:  7.4886184

Время работы при 7 элементах в массиве:
func_1:  0.29870040000000003
func_2:  0.37791550000000007
func_3:  0.5356641
func_4:  0.18197719999999995

Выводы:
При большом количестве элементов в массиве, эффективней всего работает функция 3, использующая collection.Counter, 
имеющая сложность O(N log N).
При маленьком количестве элементов в массиве, эффективней всего работает функция 4, имеющая сложность O(N).
Работа со словарями, в некоторых случаях, эффективней, чем со списками. 
"""
