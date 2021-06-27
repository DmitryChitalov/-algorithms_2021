"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.

Не забудьте, что сравнивать, например, можно операцию appendleft дека и insert списка и т.д.
"""
from collections import deque
from timeit import timeit, repeat, default_timer
import time
from random import randint, random, choice

n = 1000
test_list = [x for x in range(n)]
test_deque = deque([x for x in range(n)])

print('Время создания списка и дека с использованием list comprehensions (100000 вызовов):')
print(timeit("test_list", globals=globals(), number=100000))
print(timeit("test_deque", globals=globals(), number=100000))
print()
print('Минимальное время выполнения 100000 вызовов среди 10 замеров:')
print(min(repeat("test_list", "from __main__ import test_list", default_timer, 10, 100000)))
print(min(repeat("test_deque", "from __main__ import test_deque", default_timer, 10, 100000)))


# время зависимости от величины "n", количества вызовов показывает
# очень разные значения и преимущество переходящее: то на стороне списка, то на стороне дека.
# Минимальное время практически не отличается.

def get_time_count(f):  # создание функции для замеров времени и использования в качестве декоратора
    def t(obj):
        start_time = time.time()
        f(obj)
        end_time = time.time()
        return end_time - start_time, type(obj)

    return t


@get_time_count
def get_list_modified(list_obj, n = 1000):
    for _ in range(n):
        list_test = list_obj.copy()
        list_test.clear()
        list_obj.append(int(random() * 1000 + 1))
        list_obj.append(int(random() * 1000 + 1))
        list_obj.extend([1, 400])
        list_obj.extend([1, 400])
        list_obj.insert(0, 'gffh')
        list_obj.remove('gffh')
        list_obj.pop()
        list_obj.pop()
        list_obj.count(list_obj[0])
        list_obj.reverse()
        list_obj[0], list_obj[-1] = list_obj[-1], list_obj[0]
        list_obj[1], list_obj[-2] = list_obj[-2], list_obj[1]
    return list_obj


@get_time_count
def get_deque_modified(deque_obj, n = 1000):
    for _ in range(n):
        deque_ = deque_obj.copy()
        deque_.clear()
        deque_obj.append(int(random() * 1000 + 1))
        deque_obj.append(int(random() * 1000 + 1))
        deque_obj.extendleft([1, 400])
        deque_obj.extendleft([1, 400])
        deque_obj.appendleft('gffh')
        deque_obj.remove('gffh')
        deque_obj.popleft()
        deque_obj.popleft()
        deque_obj.count(deque_obj[0])
        deque_obj.reverse()
        deque_obj.rotate(2)
    return deque_obj


print()
print('Время выполнения равнозначных операция со списком и деком (1000 повторов в цикле) '
      'с использованием декоратора:')
print(get_list_modified(test_list))
print(get_deque_modified(test_deque))
print()
print('Минимальное среди 10 замеров время выполнения 10000 вызовов операций со списком и деком:')
print(min(repeat("get_list_modified", "from __main__ import get_list_modified, test_list", default_timer, 10, 10000)))
print(
    min(repeat("get_deque_modified", "from __main__ import get_deque_modified, test_deque", default_timer, 10, 10000)))

# минимальное время среди повторных замеров показыает, что аналогичные оперции с деком выполняются
# быстрее,чем со списком. Использование декоратора для подсчета времени
# показывает обратные результаты: оперции со списком выполняются быстрее,чем с деком.
# Функции timeit() и repeat() модуля timeit специализированные и
# демонстрируют более точные результаты, поэтому, операясь на эти данные, делаем вывод, что
# оперции со списком выполняются быстрее,чем с деком.
# кроме того, операции слева и справа в деке имеют одинаковую производительность – O(1).
# Добавление в начало осуществляется быстрее, чем в обычных списках.
# Добавление в конец – незначительно уступает спискам.
