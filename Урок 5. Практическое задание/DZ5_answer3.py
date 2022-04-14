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
import collections, timeit

el = range(10)

list_elements = []
deque_elements = collections.deque([])

print('###########################СПИСОК#######################################')
print(f"{timeit.timeit('for i in el: list_elements.append(i)', globals=globals(), number=10000)} сек.")
print(f"{timeit.timeit('for i in el: list_elements.insert(0, i)', globals=globals(), number=10000)} сек. ")
print(f"{timeit.timeit('for i in el: list_elements.pop()', globals=globals(), number=10000)} сек.")
print(f"{timeit.timeit('list_elements.extend(el)', globals=globals(), number=10000)} сек.")
print(f"{timeit.timeit('list_elements.reverse()', globals=globals(), number=10000)} сек.")
print('############################ДЭК######################################')
print(f"{timeit.timeit('for i in el: deque_elements.append(i)', globals=globals(), number=10000)} сек.")
print(f"{timeit.timeit('for i in el: deque_elements.appendleft(i)', globals=globals(), number=10000)} сек.")
print(f"{timeit.timeit('for i in el: deque_elements.pop()', globals=globals(), number=10000)} сек.")
print(f"{timeit.timeit('deque_elements.extend(el)', globals=globals(), number=10000)} сек.")
print(f"{timeit.timeit('deque_elements.reverse()', globals=globals(), number=10000)} сек.")
print(f"{timeit.timeit('deque_elements.extendleft(el)', globals=globals(), number=10000)} сек.")

'''Список и дэк заполняются примерно одинаково: 0.005798899999999999 и 0.005971900000000474 сек. соответственно.
Вставка в начало для дэка проходит занчительно быстрее 0.005758799999999731 против 5.6421893 у списка.
Удаление последнего элемента происходит примерно с одинковой скоростью 0.004732899999999596 сек./0.004893100000000317 сек.
Применение .extend тоже примерно одинаково 0.0029626000000000374 сек./0.0022234000000000975 сек.
А .reverse для списка оказывается намного быстрее 0.2699348000000006 против 1.2322714000000001 для дэка
'''