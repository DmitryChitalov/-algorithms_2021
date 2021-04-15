"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: создайте простой список (list) и очередь (deque).
Выполните различные операции с каждым из объектов.
Сделайте замеры и оцените, насколько информация в документации
соответствует дейстивтельности.

Операции равные по семантике (по смыслу)
Но разные по используемым ф-циям

И добавить аналитику, так ли это или нет.!

ОТВЕТ: Я сравнил insert(0, 13) с appendleft(13), так же pop(0) и popleft().
Из полученых запусков кода, можно сделать вывод что Deque работает быстрее,
когда идет удаление в списке через pop(0) к примеру, чем длинее список тем
тем больше растет время, поскольку все отсальные элементы должны быть сдвинуты в лево,
когда Deque не двигает элементы посольку это двух связный список, что позволяет удалять как с начала так и с конца.

Заполнение списка через .insert  0.0281953
Заполнение списка через .appendleft  0.02428240000000001
Удаление элементов списка через .popleft 0.02319600000000001
Удаление элементов спика через .pop(0) 0.028846499999999997
"""
from collections import deque
from timeit import timeit

my_list = [el for el in range(1, 100000)]
deque_obj = deque(range(100000))


def add_list():
    my_list.insert(0, 13)
    return my_list


add_list()


def add_deque():
    deque_obj.appendleft(13)
    return deque_obj


add_deque()


def popleft_deque():
    deque_obj.popleft()
    return deque_obj


popleft_deque()


def pop_list():
    my_list.pop(0)
    return my_list


pop_list()


print(f'Заполнение списка через .insert ', timeit('add_list', globals=globals()))
print(f'Заполнение списка через .appendleft ', timeit('add_deque', globals=globals()))
print(f'Удаление элементов списка через .popleft', timeit('popleft_deque', globals=globals()))
print(f'Удаление элементов спика через .pop(0)', timeit('pop_list', globals=globals()))

