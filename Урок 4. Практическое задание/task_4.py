"""
Задание 4.

Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.

Сделайте профилировку каждого алгоритма через timeit

Попытайтесь написать третью версию, которая будет самой быстрой.
Сделайте замеры и опишите, получилось ли у вас ускорить задачу.

Без аналитики задание считается не принятым
"""


from timeit import timeit, repeat, default_timer


numbers_list = [1, 2, 5, 3, 4, 5, 5]


def func_1():

    m = 0

    num = 0

    for i in numbers_list:

        count = numbers_list.count(i)

        if count > m:

            m = count

            num = i

    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():

    new_array = []
    for el in numbers_list:
        count2 = numbers_list.count(el)
        new_array.append(count2)
    max_2 = max(new_array)
    elem = numbers_list[new_array.index(max_2)]
    f'оно появлялось в массиве {max_2} раз(а)'


def func_3():

    elem = sorted([item for item in numbers_list], key=lambda x: numbers_list.count(x), reverse=True)[0]

    return f'Чаще всего встречается число {elem}, ' \
           f'оно появлялось в массиве {numbers_list.count(elem)} раз(а)'


def func_4():

    elem = max(numbers_list, key=numbers_list.count)

    return f'Чаще всего встречается число {elem}, ' \
           f'оно появлялось в массиве {numbers_list.count(elem)} раз(а)'


print(func_1())

print(func_2())

print(func_3())

print(func_4())


t1 = min(repeat('func_1()', 'from __main__ import func_1', default_timer, 5, 10000))

t2 = min(repeat('func_2()', 'from __main__ import func_2', default_timer, 5, 10000))

t3 = min(repeat('func_3()', 'from __main__ import func_3', default_timer, 5, 10000))

t4 = min(repeat('func_4()', 'from __main__ import func_4', default_timer, 5, 10000))


print(f"Из 1ой и 2ой функций быстрее функция : {'func_1' if t1 < t2 else 'func_2'}")


print(f"Время выполнения 1ой функции: \t{t1}")

print(f"Время выполнения 2ой функции : \t{t2}")

print(f"Время выполнения 3ей функции : \t{t3}")

print(f"Время выполнения 4ой функции : \t{t4}")


'''
*результаты*


Чаще всего встречается число 5, оно появлялось в массиве 3 раз(а)
Чаще всего встречается число 5, оно появлялось в массиве 3 раз(а)

Из 1ой и 2ой функций быстрее функция : func_1

Время выполнения 1ой функции: 	0.011617600000000005
Время выполнения 2ой функции : 	0.013114400000000012
Время выполнения 3ей функции : 	0.018026899999999985
Время выполнения 4ой функции : 	0.011135799999999973



2ая функция медленнее 1ой, так как в ней происходит создание нового массива, а так же его заполнение. 
После его заполнения происходит пробег по уже новому массиву и происходит выборка max значения.

3ая самая медленная из всех, потому что сложность O(n log n) (ну, а такая сложность из-за сортировки).

4ая функция вышла самой быстрой из всех, так как count позволяет выбирать максимальное значение сразу.

'''
