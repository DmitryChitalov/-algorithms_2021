from collections import deque
from timeit import timeit


def fill_list():
    test_list = [_ for _ in range(1000)]
    return test_list


def fill_deque():
    test_deque = deque([_ for _ in range(1000)])
    return test_deque


def appendleft_list(target):
    for i in range(10):
        target.insert(0, i)


def appendleft_deque(target):
    for i in range(10):
        target.appendleft(i)


def popleft_list(target):
    for i in range(10):
        target.pop(0)


def popleft_deque(target):
    for i in range(10):
        target.popleft()


def extendleft_list(target):
    test_arr = [1, 2]
    for i in range(len(test_arr)):
        target.insert(0, test_arr[i])


def extendleft_deque(target):
    target.extendleft([1, 2])


if __name__ == '__main__':
    my_list = fill_list()
    my_deque = fill_deque()
    print("Заполнение ....")
    print(f"List: {timeit('fill_list()', globals=globals(), number=1000)}")  # 0.047
    print(f"Deque: {timeit('fill_deque()', globals=globals(), number=1000)}")  # 0.055
    print("Append left....")
    print(f"List: {timeit('appendleft_list(my_list)', globals=globals(), number=1000)}")  # 0.0364
    print(f"Deque: {timeit('appendleft_deque(my_deque)', globals=globals(), number=1000)}")  # 0.0013
    print("Popleft ..")
    print(f"List: {timeit('popleft_list(my_list)', globals=globals(), number=1000)}")  # 0.0081
    print(f"Deque: {timeit('popleft_deque(my_deque)', globals=globals(), number=1000)}")  # 0.0010
    print("Extend left....")
    print(f"List: {timeit('extendleft_list(my_list)', globals=globals(), number=1000)}")  # 0.0033
    print(f"Deque: {timeit('extendleft_deque(my_deque)', globals=globals(), number=1000)}")  # 0.0003

    """
    Судя по замерам список заполняется быстрее чем deque, в остальном deque работает быстрее списка.
    """
