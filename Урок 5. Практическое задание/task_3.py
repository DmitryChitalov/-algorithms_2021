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

# Полезная документация:
# https://docs.python.org/3/library/collections.html#collections.deque

from timeit import repeat, default_timer

deque_import_code = "from collections import deque"
list_create_code = "l = list('BCDEFGHIJKLMNOPQRSTUVWXY')"
deque_create_code = "l = list('BCDEFGHIJKLMNOPQRSTUVWXY')"


# 1. Создание списка из строки

# [0.041611552999999996, 0.035245307000000003, 0.03590511099999999]
print(repeat(list_create_code, "", default_timer, 3, pow(10, 5)))
# [0.033508594, 0.033455897999999984, 0.033527002]
print(repeat(deque_create_code, deque_import_code, default_timer, 3, pow(10, 5)))

# [0.03745678700000002, 0.04363481300000005, 0.04225130300000002]
print(repeat(list_create_code, deque_import_code, default_timer, 3, pow(10, 5)))
# [0.03636483699999998, 0.03447713200000002, 0.035460424000000046]
print(repeat(list_create_code, "", default_timer, 3, pow(10, 5)))

# создание списка и deque из строки занимает примерно одинаковое время
# времени занимает больше почему то тот, который идет первым при замерах

# 2. добавление элемента в конец (справа)

print(repeat("l = list('BCDEFGHIJKLMNOPQRSTUVWXY')", list_create_code, default_timer, 3, pow(10, 5)))
# [0.033508594, 0.033455897999999984, 0.033527002]
print(repeat("d = deque('BCDEFGHIJKLMNOPQRSTUVWXY')", "from collections import deque", default_timer, 3, pow(10, 5)))