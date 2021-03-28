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

from collections import deque
from timeit import timeit


def simply_create():
    simply_list = [x for x in range(50)]
    return simply_list


def deque_create():
    deque_list = deque([x for x in range(50)])
    return deque_list


print(f'\n{"=" * 15} Создание коллекции {"=" * 15}')
print(f'Обычный список: {timeit("simply_create()", globals=globals(), number=10000)}')
print(f'deque         : {timeit("deque_create()", globals=globals(), number=10000)}')

simply_list = simply_create()
deque_list = deque_create()

print(f'\n{"=" * 10} Добавление элемента .append {"=" * 11}')
print(f'Обычный список: {timeit("simply_list.append(200)", globals=globals(), number=1000000)}')
print(f'deque в конец : {timeit("deque_list.append(200)", globals=globals(), number=1000000)}')
print(f'deque в начало: {timeit("deque_list.appendleft(200)", globals=globals(), number=1000000)}')

print(f'\n{"=" * 6} Добавление списка элементов .extend {"=" * 7}')
test_list = simply_create()
print(f'Обычный список\n'
      f'с помощью "+" : {timeit("simply_list.extend(test_list)", globals=globals(), number=100000)}')
print(f'Обычный список: {timeit("simply_list.extend(test_list)", globals=globals(), number=100000)}')
print(f'deque в конец : {timeit("deque_list.extend(test_list)", globals=globals(), number=100000)}')
print(f'deque в начало: {timeit("deque_list.extendleft(test_list)", globals=globals(), number=100000)}')

print(f'\n{"=" * 10} Добавление элементов .insert {"=" * 10}')
print(f'Обычный список: {timeit("simply_list.insert(20, 20)", globals=globals(), number=100)}')
print(f'deque         : {timeit("deque_list.insert(20, 20)", globals=globals(), number=100)}')

print(f'\n{"=" * 12} Удаление элементов .pop {"=" * 13}')
print(f'Обычный список: {timeit("simply_list.pop()", globals=globals(), number=1000000)}')
print(f'deque c конца : {timeit("deque_list.pop()", globals=globals(), number=1000000)}')
print(f'deque с начала: {timeit("deque_list.popleft()", globals=globals(), number=1000000)}')

print(f'\n{"=" * 21} Реверс {"=" * 21}')
print(f'Обычный список\n'
      f'с пом. среза  : {timeit("simply_list[::-1]", globals=globals(), number=10)}')
print(f'Обычный список\n'
      f'с пом. reverse: {timeit("simply_list.reverse()", globals=globals(), number=10)}')
print(f'deque .reverse: {timeit("deque_list.reverse()", globals=globals(), number=10)}')

print(f'\n{"=" * 15} Доступ по индексу {"=" * 16}')
print(f'Обычный список: {timeit("simply_list[20]", globals=globals(), number=1000000)}')
print(f'deque         : {timeit("deque_list[20]", globals=globals(), number=1000000)}')

print(f'\n{"=" * 10} Поиск индекса по значению {"=" * 10}')
print(f'Обычный список: {timeit("simply_list.index(20)", globals=globals(), number=100000)}')
print(f'deque         : {timeit("deque_list.index(20)", globals=globals(), number=100000)}')

"""
Исходя из проведенных замеров работы методов можно абсолютно подтвердить основное правило
list vs deque.

При добавлении, удалении значений (списков значений), а также работе со всей коллекцией, 
за исключением создания абсолютное лидерство держит deque.
А при работе со значениями коллекций перевес по скорости на стороне list.
"""











