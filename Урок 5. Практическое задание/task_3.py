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
from timeit import timeit


def func_app(var, value=1):
    return var.append(value)


def func_pop(var):
    return var.pop()


def func_copy(var):
    return var.copy()


def func_insert(var_list, value=1):
    var_list.insert(0, value)


def func_reverse(var):
    return var.reverse()


def deque_appleft(var_deque, value=1):
    return var_deque.appendleft(value)


def deque_popleft(var_deque):
    return var_deque.popleft()


my_list = [el for el in range(10000)]
my_deque = deque(el for el in range(10000))


print(f"func_app(list): {timeit('func_app(my_list)', globals=globals(), number=10000)} sec.")
print(f"func_app(deque): {timeit('func_app(my_deque)', globals=globals(), number=10000)} sec.")
print(f"func_pop(list): {timeit('func_pop(my_list)', globals=globals(), number=10000)} sec.")
print(f"func_pop(deque): {timeit('func_pop(my_deque)', globals=globals(), number=10000)} sec.")
print(f"func_copy(list): {timeit('func_copy(my_list)', globals=globals(), number=10000)} sec.")
print(f"func_copy(deque): {timeit('func_copy(my_deque)', globals=globals(), number=10000)} sec.")
print(f"func_insert(list): {timeit('func_insert(my_list)', globals=globals(), number=10000)} sec.")
print(f"deque_appleft(deque): {timeit('deque_appleft(my_deque)', globals=globals(), number=10000)} sec.")
print(f"deque_popleft(deque): {timeit('deque_popleft(my_deque)', globals=globals(), number=10000)} sec.")
print(f"func_reverse(list): {timeit('func_reverse(my_list)', globals=globals(), number=10000)} sec.")
print(f"func_reverse(deque): {timeit('func_reverse(my_deque)', globals=globals(), number=10000)} sec.")

# func_app(list): 0.0016861999999999988 sec.
# func_app(deque): 0.0016188999999999995 sec.
#--------------------------------------------
# func_pop(list): 0.0013954999999999974 sec.
# func_pop(deque): 0.0013453000000000007 sec.
#--------------------------------------------
# func_copy(list): 0.1495028 sec.
# func_copy(deque): 0.5244376 sec.
#--------------------------------------------
# func_insert(list): 0.0530254 sec.
# deque_appleft(deque): 0.00149150000000009 sec.
# deque_popleft(deque): 0.0012620000000000964 sec.
#---------------------------------------------
# func_reverse(list): 0.05042760000000002 sec.
# func_reverse(deque): 0.0672005 sec.
#--------------------------------------------

# Добавление и удаление элементов в деку на таком же уровне что и в список.
# Копирование списка в 3 раза быстрее копирования деки.
# Вот по вставке элемената в начало дека выигрывает на порядок.
# Реверс деки оказался дольше, но значение не критично.
