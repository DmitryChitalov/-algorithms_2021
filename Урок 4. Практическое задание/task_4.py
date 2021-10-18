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


def my_func():
    count_2 = 0
    number = 0
    for el in array:
        count = 0
        for el_2 in array:
            if el == el_2:
                count += 1
        if count > count_2:
            count_2 = count
            number = el
    return f'Number {number} was {count_2} times '


print(func_1())
print(func_2())
print(my_func())

print("func_1 time: ", timeit.timeit("func_1()", globals=globals()), "secs")
print("func_2 time: ", timeit.timeit("func_2()", globals=globals()), "secs")
print("my_func time: ", timeit.timeit("my_func()", globals=globals()), "secs")

# Самая быстрая функция - func_1, у меня не получилось улучшить ее результат, но если делать с помощью collections,
# у меня бы получилось лучше, но пока нельзя так делать.
