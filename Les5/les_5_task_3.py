from collections import deque
from timeit import timeit
deq_obj = deque()
my_list = list()


def list_test_1():
    my_list.append("abc")
    my_list.insert(0, "abc")
    my_list.extend([i for i in range(1000)])
    my_list.pop()
    my_list.clear()


def deq_test_1():
    deq_obj.append("abc")
    deq_obj.appendleft("abc")
    deq_obj.extend([i for i in range(1000)])
    deq_obj.pop()
    deq_obj.clear()


def list_test_2():
    m_list = []
    for i in range(1000):
        m_list.insert(0, i)


def deq_test_2():
    deq = deque()
    for d in range(1000):
        deq.appendleft(d)


def list_test_3():
    my_list = [i for i in range(1000)]
    for i in range(1000):
        my_list[i] = my_list[i] + 1


def deq_test_3():
    deq_obj = deque([i for i in range(1000)])
    for i in range(1000):
        deq_obj[i] = deq_obj[i] + 1


print("=====================")
print(f"List result: {timeit('list_test_1()', setup='from __main__ import list_test_1', number=1000)}")
print(f"Deque result: {timeit('deq_test_1()', setup='from __main__ import deq_test_1', number=1000)}")
print("#########")
print(f"List result: {timeit('list_test_2()', setup='from __main__ import list_test_2', number=1000)}")
print(f"Deque result: {timeit('deq_test_2()', setup='from __main__ import deq_test_2', number=1000)}")
print("#########")
print(f"List result: {timeit('list_test_3()', setup='from __main__ import list_test_3', number=1000)}")
print(f"Deque result: {timeit('deq_test_3()', setup='from __main__ import deq_test_3', number=1000)}")
print("=====================")

"""
Вывод: Deque лучше выполняет операции дописать вначало и т.п, а список быстрый доступ к элементам
"""
