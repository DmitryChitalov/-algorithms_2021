"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft дека и для их аналогов у списков.
"""


from collections import deque

n = 1000000


def timer(func):
    import time
    def wrapper(*arg):
        start = time.time()
        func(*arg)
        end = time.time()
        print(f'время выполнения - {end - start} \n')

    return wrapper


@timer
def test(x):
    for i in range(n):
        x.append(i)
    print('заполнение списка ')


@timer
def test1(x):
    x.insert(0, -1)
    print('добавление в начало списка')


@timer
def test_deq_1(x_deq):
    for i in range(n):
        x_deq.append(i)
    print('запонение деки')


x_deq = deque([])


@timer
def test_deq_2(x_deq):
    x_deq.appendleft(-1)
    print('добавление в начало деки')


@timer
def test2(x):
    x.append(n)
    print('добавление в конец списка')


@timer
def test_deq_3(x_deq):
    x_deq.append(n)
    print('добавление в конец деки')


@timer
def test3(x):
    x.pop(0)
    print('удаление с начала списка')


@timer
def test_deq_4(x_deq):
    x_deq.popleft
    print('удаление с начала деки')


x = []
test(x)
# print(x)
test_deq_1(x_deq)
# print(x_deq)
test1(x)
# print(x)
test_deq_2(x_deq)
# print(x_deq)
test2(x)
# print(x)
test_deq_3(x_deq)
# print(x_deq)
test3(x)
# print(x)
test_deq_4(x_deq)
# print(x_deq)
obj1 = []
obj2 = []
for i in range(n):
    obj1.append(i)
for i in range(n):
    obj2.append(i)


@timer
def test4(obj1, obj2):
    obj1.extend(obj2)
    print('расширение списка ')


test4(obj1, obj2)
# print(obj1)
x1_deq = deque([])
x2_deq = deque([])
for i in range(n):
    x1_deq.append(i)
for i in range(n):
    x2_deq.append(i)


@timer
def test_deq_5(x1_deq, x2_deq):
    x1_deq.extendleft(x2_deq)
    print('расширение деки')


test_deq_5(x1_deq, x2_deq)

'''
При тестировании список и дека ведут себя по разному в зависимости от количества элементов.
При увеличении 'n' дека начинает выигрывать по времени в большинстве тестов. 
'''
