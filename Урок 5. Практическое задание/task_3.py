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
from timeit import timeit


def deque_filling(my_str):
    return deque(my_str)


def list_filling(my_str):
    return list(my_str)


def pop_deque(my_d):
    return my_d.popleft()


def pop_list(my_l):
    return my_l.pop(0)


def append_deque(my_d, my_str):
    return my_d.appendleft(my_str)


def append_list(my_l, my_str):
    return my_l.insert(0, my_str)


def extend_deque(my_d, n_list):
    return my_d.extendleft(n_list)


def extend_list(my_l, n_list):
    return n_list + my_l


def extend_list_2(my_l, n_list):  # Не смог сходу оценить, какой метод лучше
    my_l[:0] = n_list
    return my_l


if __name__ == '__main__':
    data = 'Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the ' \
           'industry standard dummy text ever since the 1500s, when an unknown printer took a galley of type and ' \
           'scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap ' \
           'into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the ' \
           'release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing ' \
           'software like Aldus PageMaker including versions of Lorem Ipsum. '
    print(timeit('deque_filling("".join(data.split()))', globals=globals()))  # 7.0719503999999995
    print(timeit('list_filling("".join(data.split()))', globals=globals()))  # 6.263792100000001
    data_upd = "".join(data.split())
    my_deque = deque_filling(data_upd)
    my_list = list_filling(data_upd)
    print(timeit('pop_deque(my_deque)', globals=globals(), number=400))  # 3.0299999998817384e-05
    print(timeit('pop_list(my_list)', globals=globals(), number=400))  # 5.1699999998433555e-05
    print(timeit('append_deque(my_deque, "lorem")', globals=globals()))  # 0.09055889999999994
    print(timeit('append_list(my_list, "lorem")', globals=globals()))  # 248.91978300000002
    print(timeit('extend_deque(my_deque, list("lorem"))', globals=globals()))  # 0.2576326
    print(timeit('extend_list(my_list, list("lorem"))', globals=globals()))  # 0.8520394
    print(timeit('extend_list_2(my_list, list("lorem"))', globals=globals()))  # 343.6543452300000002

# Выводы. Таким образом, заполнение очереди и списка примерно одинаково по времени, хотя очереть заполняется все же чуть
# быстрее. Popleft в очереди в два раза быстрее аналогичной операции со списком, скорее всего, потому что для списка это
# не очень сложная операция. Нужно всего лишь "откусить" первый элемент. При этом при большой длине списка - разница
# будет гораздо более существенная, о чем нам говорит нотация всех этих операций - O(n) для списка и O(1) для deque.
# дальше разница становится совсем уж неприличной, appendleft очереди быстрее на 4 порядка, extendleft(кстати для списка
# лучше первый из примененных способов) для очереди быстрее в несколько раз.
