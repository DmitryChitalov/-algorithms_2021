"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000
Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснвование рез-ам
"""

from timeit import timeit


# Сложность: O(n^3)
def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:                               # O(n)
        t = 1                                       # O(1)
        is_simple = True                            # O(1)
        while t <= n:                               # O(n)
            if n % t == 0 and t != 1 and t != n:    # O(n)
                is_simple = False                   # O(1)
                break                               # O(1)
            t += 1                                  # O(1)
        if is_simple:                               # O(n)
            if count == i:                          # O(n)
                break                               # O(1)
            count += 1                              # O(1)
        n += 1                                      # O(1)
    return n                                        # O(1)


num_1 = 10
num_2 = 100
num_3 = 1000

print(f'simple: {simple(num_1)}')
print(timeit('simple(num_1)', globals=globals(), number=10))

print(f'simple: {simple(num_2)}')
print(timeit('simple(num_2)', globals=globals(), number=10))

print(f'simple: {simple(num_3)}')
print(timeit('simple(num_3)', globals=globals(), number=10))


# Тоже без решета, но первое, что пришло в голову с перебором делителей
# Сложность O(n^3)
def simple_2(num):
    simple_list = []                                # O(1)
    simple_num = 1                                  # O(1)
    while len(simple_list) < num:                   # O(n)
        divider_list = []                           # O(1)
        for divider in range(simple_num, 0, -1):    # O(n)
            if simple_num % divider == 0:           # O(n)
                divider_list.append(divider)        # O(1)
            if divider == 1:                        # O(n)
                break                               # O(1)
            elif len(divider_list) > 2:             # O(n)
                break                               # O(1)
        if len(divider_list) == 2:                  # O(n)
            simple_list.append(simple_num)          # O(1)
        simple_num += 1                             # O(1)
    return simple_list[-1]                          # O(1)


print(f'simple_2: {simple_2(num_1)}')
print(timeit('simple_2(num_1)', globals=globals(), number=10))

print(f'simple_2: {simple_2(num_2)}')
print(timeit('simple_2(num_2)', globals=globals(), number=10))

print(f'simple_2: {simple_2(num_3)}')
print(timeit('simple_2(num_3)', globals=globals(), number=10))


# С решетом:
# Сложность O(n^6)
def simple_3(num):
    simple_list = [0, 1]                                                                             # O(1)
    # дополняем список, пока в нем не появится нужный нам элемент (проблема, наверняка, здесь)
    while len(simple_list) <= num:                                                                   # O(n)
        help_list = list(range(simple_list[-1] + 1, simple_list[-1] + num + 2 - len(simple_list)))   # O(n)
        simple_list.extend(help_list)                                                                # O(len(help_list))
        if 1 in simple_list:                                                                         # O(n)
            simple_list[1] = 0                                                                       # O(1)
        # Непосредственно решето, но подогнанное под код
        for i in simple_list:                                                                        # O(n)
            if i != 0:                                                                               # O(n)
                j = i + i                                                                            # O(1)
                while j < simple_list[-1]:                                                           # O(n)
                    if j in simple_list:                                                             # O(n)
                        j_pos = simple_list.index(j)                                                 # O(1)
                        simple_list.insert(j_pos, 0)                                                 # O(n)
                        simple_list.remove(j)                                                        # O(n)
                    j = j + i                                                                        # O(1)
        # Удаляем лишние элементы
        simple_list = list(set(simple_list))                                                         # O(2)
        if 0 in simple_list:                                                                         # O(n)
            simple_list.remove(0)                                                                    # O(n)
    simple_list.pop(-1)                                                                              # O(1)
    return simple_list[-1]                                                                           # O(1)


'''
По итогу, видно, что функция получилась далеко не самой компактной и простой, поэтому, думаю,
будет намного затратнее по времени (И, наверняка, ее можно было сделать проще, 
но пока только это пришло в голову)
'''

print(f'simple_3: {simple_3(num_1)}')
print(timeit('simple_3(num_1)', globals=globals(), number=10))

print(f'simple_3: {simple_3(num_2)}')
print(timeit('simple_3(num_2)', globals=globals(), number=10))

print(f'simple_3: {simple_3(num_3)}')
print(timeit('simple_3(num_3)', globals=globals(), number=10))


'''
Результаты:
simple: 29
0.0001906999999999985
simple: 541
0.024601100000000004
simple: 7919
4.0886985
simple_2: 29
0.00048759999999958836
simple_2: 541
0.09893649999999976
simple_2: 7919
26.0554483
simple_3: 29
0.0013871999999963691

В общем, с последней функцией все настолько плохо, что я даже не дождался второго результата. А раз 
функции каждый раз заново приходится перебирать элементы списка, который постоянно обновляется, то такой
результат очевиден. Более того, в получившейся функции большая вложенность, что тоже влияет на скорость.

По сравнению с неудавшейся функцией, первая сделанная мной работает куда более стабильно и быстро, 
пусть и медленнее, чем исходная (раз мы работаем непосредственно со списками, а не постепенно идем к
результату, как в исходном варианте)

Когда разобрался с О нотациями, то убедился, что разница в сложности достаточно большая, отчего и виден
такой разрыв в скорости.
'''
