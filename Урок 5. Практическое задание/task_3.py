"""
Задача 3.
В соответствии с документацией Python,
deque – это обобщение стеков и очередей.
Вот основное правило: если вам нужно что-то быстро дописать или вытащить, используйте deque.
Если вам нужен быстрый случайный доступ, используйте list.

Задача:
1) создайте простой список (list) и очередь (deque). Сделайте замеры и оцените
что заполняется быстрее.
2) Выполните различные операции с каждым из объектов. Сделайте замеры и оцените,
где и какие операции быстрее.

В первую очередь необходимо выполнить замеры для ф-ций appendleft, popleft, extendleft
дека и для их аналогов у списков.
"""
from collections import deque
from random import randint
from timeit import timeit
from dis import disassemble
'''
Анализ:
1) Простой список заполняется незначительно быстрее deque, т.к. в случае deque происходит
на одну инструкцию вызова функции больше.

2) Вставка в конец ряда объекта методами extend и append у list и deque равна по скорости.
То же самое можно сказать о методе pop().

3) Все методы вставки, работающие с началом ряда у deque - существенно быстрее.
То же самое можно сказать о методе popleft() - его скорость сравнима с pop(), т.к.
подобные операции и с концом, и с началом ряда имеют сложность O(1)

4) Поверхностная копия list на порядок быстрее, чем deque, то же происходит и с reverse.
 Очистка list и deque по занимаемому времени практически идентична.
 Вот причину этого отличия, если честно, я не выявила. Хотя разобраться было интересно.
 Ее надо искать не методом декомпиляции, а каким-то иным, так как там все с виду абсолютно
 идентично.
 Я пыталась искать информацию, но статей практически нет - есть какие-то отсылки к тому, что
 list реализован на основе метода realloc(), а deque нет, но указанная функция - из библиотеки
 С и времени хорошо вникнуть в такой пласт информации совершенно нет.
'''

create_operations = dict(creating_a_list="""my_list = [randint(0, 50) for i in range(100)]""",
                         creating_a_deque="""deque([randint(0, 50) for j in range(100)])""")

my_list = [randint(0, 50) for i in range(100)]
my_deque = deque([randint(0, 50) for j in range(100)])

add_to_end_operations = dict(append_to_list="""my_list.append('5')""",
                             extend_to_list="""my_list.extend('561')""",
                             append_to_deque="""my_deque.append('5')""",
                             extend_to_deque="""my_deque.extend('561')""")

add_to_start_operations = dict(insert_to_list="""my_list.insert(0, 5)""",
                               insert_to_deque="""my_deque.insert(0, 5)""",
                               append_to_left_deque="""my_deque.appendleft('5')""",
                               extend_to_left_deque="""my_deque.extendleft('5')""")


del_from_end_operations = dict(pop_list="""my_list.pop()""",
                               pop_deque="""my_deque.pop()""")


del_from_start_operations = dict(pop_0_list="""my_list.pop(0)""",
                                 del_0_list="""del my_list[0]""",
                                 popleft_deque="""my_deque.popleft()""")

different_operations = dict(copy_list="""my_list.copy()""",
                            copy_deque="""my_deque.copy()""",
                            reverse_list="""my_list.reverse()""",
                            reverse_deque="""my_deque.reverse()""",
                            clear_list="""my_list.clear()""",
                            clear_deque="""my_deque.clear()""")


for name, text in create_operations.items():
    print(f"Создание и заполнение {name}, {timeit(stmt=text, number=1000, globals=globals()):.5f}")

for name, text in add_to_end_operations.items():
    print(f"Вставка в конец {name}, {timeit(stmt=text, number=1000, globals=globals()):.5f}")

for name, text in add_to_start_operations.items():
    print(f"Вставка в начало {name}, {timeit(stmt=text, number=1000, globals=globals()):.5f}")

for name, text in del_from_end_operations.items():
    print(f"Удаление с конца {name}, {timeit(stmt=text, number=1000, globals=globals()):.5f}")

for name, text in del_from_start_operations.items():
    print(f"Удаление с начала {name}, {timeit(stmt=text, number=1000, globals=globals()):.5f}")

for name, text in different_operations.items():
    print(f"Разные операции {name}, {timeit(stmt=text, number=1000, globals=globals()):.5f}")


# for name, text in create_operations.items():
#     print(name)
#     code = compile(text, '<string>', 'exec')
#     disassemble(code)

# for name, text in different_operations.items():
#     print(name)
#     code = compile(text, '<string>', 'exec')
#     disassemble(code)
