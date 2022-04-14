"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача: 
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените, где и какие операции быстрее.
"""
from collections import deque
from timeit import timeit
from random import randint

# оцениваю создание простого списка (list) и очереди (deque)


def filling_the_list(nums):
    return [elem for elem in range(nums)]


def filling_the_deque(nums):
    return deque([elem for elem in range(nums)])


number_100 = 100
print(f'Заполнение обычного списка, кол-во элементов - 100:'
      f' {timeit("filling_the_list(number_100)", globals=globals(), number=1000)}')
print(f'Заполнение списка deque, кол-во элементов - 100:'
      f' {timeit("filling_the_deque(number_100)", globals=globals(), number=1000)}')


number_1000 = 1000
print(f'Заполнение обычного списка, кол-во элементов - 1000: '
      f'{timeit("filling_the_list(number_1000)", globals=globals())}')
print(f'Заполнение списка deque, кол-во элементов - 1000: '
      f'{timeit("filling_the_deque(number_1000)", globals=globals())}')

# Сравниваю операцию appendleft и insert


def insert_int_the_list(my_list: list, nums: int):
    for _ in range(nums):
        my_list.insert(0, randint(0, 10))
    return my_list


def append_left_in_the_deque(my_deque, nums: int):
    for _ in range(nums):
        my_deque.appendleft(randint(0, 10))
    return my_deque


simple_list = filling_the_list(number_100)
deque_list = filling_the_deque(number_100)

print('-' * 100)
print(f'Вставка в начало обычного списка 100 элементов:'
      f' {timeit("insert_int_the_list(simple_list, 100)", globals=globals(), number=1000)}')
print(f'Вставка в начало deque 100 элементов:'
      f' {timeit("append_left_in_the_deque(deque_list, 100)", globals=globals(), number=1000)}')

# Сравниваю операцию pop в списке и очереди


def pop_out_the_list_1(my_list: list, nums: int):
    for _ in range(nums):
        my_list.pop()
    return my_list


def pop_out_the_deque_1(my_deque, nums: int):
    for _ in range(nums):
        my_deque.pop()
    return my_deque


def pop_out_the_list_2(my_list: list, nums: int):
    for _ in range(nums):
        my_list.pop(0)
    return my_list


def pop_out_the_deque_2(my_deque, nums: int):
    for _ in range(nums):
        my_deque.popleft()
    return my_deque


print('-' * 100)
print(f'Извлечение с конца обычного списка 100 элементов:'
      f' {timeit("pop_out_the_list_1(simple_list, 100)", globals=globals(), number=1000)}')
print(f'Извлечение с конца deque 100 элементов:'
      f' {timeit("pop_out_the_deque_1(deque_list, 100)", globals=globals(), number=1000)}')


# Сравниваю операцию append в списке и очереди


def append_int_the_list(my_list: list, nums: int):
    for _ in range(nums):
        my_list.append(randint(0, 10))
    return my_list


def append_in_the_deque(my_deque, nums: int):
    for _ in range(nums):
        my_deque.append(randint(0, 10))
    return my_deque


print('-' * 100)
print(f'Вставка в обычный список 100 элементов:'
      f' {timeit("append_int_the_list(simple_list, 100)", globals=globals(), number=1000)}')
print(f'Вставка в deque 100 элементов:'
      f' {timeit("append_in_the_deque(deque_list, 100)", globals=globals(), number=1000)}')


print('-' * 100)
print(f'Извлечение с начала обычного списка 100 элементов:'
      f' {timeit("pop_out_the_list_2(simple_list, 100)", globals=globals(), number=1000)}')
print(f'Извлечение с начала deque 100 элементов:'
      f' {timeit("pop_out_the_deque_2(deque_list, 100)", globals=globals(), number=1000)}')

"""
По результатам измерений видно, что:
 1. создание простых списков (list) и очередей (deque) не сильно
    различаются по времени. Но небольшой перекос в пользу обычного списка имеется.
    Заполнение обычного списка, кол-во элементов - 100: 2.7142087000000004
    Заполнение списка deque, кол-во элементов - 100: 3.5462046
    Заполнение обычного списка, кол-во элементов - 1000: 30.141694400000002
    Заполнение списка deque, кол-во элементов - 1000: 37.259952000000006
 2. insert в простых списках (list) и appendleft в очередях (deque)
    очень сильно различаются по времени.
    Вставка в обычный список 100 элементов: 379.511866
    Вставка в deque 100 элементов: 0.6822537000000466
    И это "всего" на 10000 повторений
 3. Скорость удаления элемента с конца списка и с конца deque примерно одинакова,
    т.к. в обоих случаях оспользуется функция pop
    Извлечение с конца обычного списка 100 элементов: 0.004395699999989233
    Извлечение с конца deque 100 элементов: 0.004258799999988128
 4. Скорость удаления элемента с начала списка гораздо медленнее чем с начала deque
    Извлечение с начала обычного списка 100 элементов: 1.1660968000000054
    Извлечение с начала deque 100 элементов: 0.0042432000000047765  
 5. Добавление в конец deque – сопоставимо с добавлением в списки.
    Вставка в обычный список 100 элементов: 0.06740400000001046
    Вставка в deque 100 элементов: 0.06868750000001
    
Таким образом можно сделать вывод, что в некоторых случаях лучше использовать deque т.к. 
его функции оптимизированны и, как следствие, работают быстрее.
"""
