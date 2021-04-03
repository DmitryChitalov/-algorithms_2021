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
"""
import random
from collections import deque
from timeit import timeit


number_of_tests = 10000
list_to_process = list(random.sample(range(1, 500000), 10000))
deque_to_process = deque(random.sample(range(1, 500000), 10000))

print(list_to_process)
print(deque_to_process)

print("Append")
print(timeit("list_to_process.append('1')", number=number_of_tests, globals=globals()))
print(timeit("deque_to_process.append('1')", number=number_of_tests, globals=globals()))

print("insert vs appendleft")
print(timeit("list_to_process.insert(0,'1')", number=number_of_tests, globals=globals()))
print(timeit("deque_to_process.appendleft('1')", number=number_of_tests, globals=globals()))

print("insert")
print(timeit("list_to_process.insert(0,'1')", number=number_of_tests, globals=globals()))
print(timeit("deque_to_process.insert(0,'1')", number=number_of_tests, globals=globals()))

print("pop")
print(timeit("list_to_process.pop()", number=number_of_tests, globals=globals()))
print(timeit("deque_to_process.pop()", number=number_of_tests, globals=globals()))

print("pop vs popleft")
print(timeit("list_to_process.pop(0)", number=number_of_tests, globals=globals()))
print(timeit("deque_to_process.popleft()", number=number_of_tests, globals=globals()))

print("count")
print(timeit("list_to_process.count(1)", number=number_of_tests, globals=globals()))
print(timeit("deque_to_process.count(1)", number=number_of_tests, globals=globals()))

print("reverse")
print(timeit("list_to_process.reverse()", number=number_of_tests, globals=globals()))
print(timeit("deque_to_process.reverse()", number=number_of_tests, globals=globals()))

print("index")
print(timeit("list_to_process[8000]", number=number_of_tests, globals=globals()))
print(timeit("deque_to_process[8000]", number=number_of_tests, globals=globals()))

"""
Append - работает почти одинаково эффективно как со списком, так и с деком
0.0009765999999999941
0.0008897000000000072

insert vs appendleft - дек работает намного быстрее списка 
0.09936689999999998
0.0008583000000000063

insert - дек работает намного быстрее списка 
0.13802169999999997
0.0016645999999999606

pop - работает почти одинаково эффективно как со списком, так и с деком
0.0009971999999999759
0.000818299999999994

pop vs popleft - дек работает намного быстрее списка 
0.020596400000000015
0.0008440999999999588

count - работает почти одинаково эффективно как со списком, так и с деком
3.2581941999999997
3.4790628000000003

reverse - дек работает быстрее списка 
0.07639969999999963
0.18242629999999949

index
0.0006155000000003241
0.004326599999999736

Утверждение в начале задания верно. В операциях добавления и удаления deque работает намного быстрее.
При случайном доступе к элементам list работает намного быстрее, чем deque
"""