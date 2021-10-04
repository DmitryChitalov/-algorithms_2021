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
    num = max(array, key=array.count)
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {array.count(num)} раз(а)'


if __name__ == '__main__':
    print(timeit("func_1()", globals=globals()))  # 2.55
    print(timeit("func_2()", globals=globals()))  # 3.38
    print(timeit("func_3()", globals=globals()))  # 2.19

    """
    func2() самая медленная, так как происходит добавление в список элементов + функция max()
    func1() следующая по скорости так как в ней перебор в цикле
    func3() самый быстрый и лаконичный вариант
    """