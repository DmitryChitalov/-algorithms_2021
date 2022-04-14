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


test_array = [1, 3, 1, 3, 4, 5, 1]


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
    elem = max(set(array), key=array.count)

    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {array.count(elem)} раз(а)'


print('func_1')
print(func_1(test_array))
print('func_1',
      timeit(
          "func_1(test_array)",
          setup='from __main__ import func_1, test_array',
          number=10000))

print('func_2')
print(func_2(test_array))
print('func_2',
      timeit(
          "func_2(test_array)",
          setup='from __main__ import func_2, test_array',
          number=10000))

print('func_3')
print(func_3(test_array))
print('func_3',
      timeit(
          "func_3(test_array)",
          setup='from __main__ import func_3, test_array',
          number=10000))

# ### Результаты ###
# func_1
# Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
# func_1 0.0009416999999999967
# func_2
# Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
# func_2 0.0014520999999999978
# func_3
# Чаще всего встречается число 1, оно появилось в массиве 3 раз(а)
# func_3 0.0010198000000000013
# Выводы: Как видно из замеров, самыми быстрыми оказались func_1 и func_3, но реализованная func_3 куда более лаконичка,
# за счет использования встроенной функции max()
