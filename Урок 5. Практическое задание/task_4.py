"""
Задача 4.
Поработайте с обычным словарем и OrderedDict.
Выполните операции с каждым их них (заполнение, получение элемента) и сделайте замеры.
Опишите полученные результаты, сделайте выводы.

И есть ли смысл исп-ть OrderedDict в Python 3.6 и более поздних версиях?
"""
from collections import OrderedDict
from random import randint
from timeit import timeit

'''
Анализ:
1) Операция создания и заполнения обычного словаря несколько быстрее, чем OrderedDict.
Предполагаю, что не только за счет формы хранения данных, но и потому, что он при создании
обрабатывает уже некую имеющуюся конструкцию.

2) Запрос элемента занимает примерно равное время.

3) Добавление элемента в OrderedDict выполняется немного медленнее, возможно, потому что
тратится время на присвоение ему порядкового номера в структуре и запись в нужном формате.

4) Сортировка меня особенно интересовала, т.к. прежде я читала, что OrderedDict может быть
оптимизирован для частого переупорядочивания. Но и здесь он показал результаты ниже, по всем
типам сортировки.

5) Метод popitem() тоже быстрее работает в рамках обычного словаря.

Итог:
У OrderedDict есть 2 интересных функции, .popitem(), в которую можно передавать False и менять
порядок LIFO на FIFO, а также .move_to_end(), у которой есть аргумент last, позволяющий
перемещать элемент в начало или конец (в зависимости от того, было ли передано False или True).
Но этот функционал слишком мал для того, чтобы OrderedDict мог сохранять свое практическое
значение.
Если в будущем его не оптимизируют или не расширят уникальный функционал, то этот объект и
термин уйдут в прошлое. В прошлом он, видимо, был необходим, но с версии 3.6 обычные словари
получили возможность хранить порядок элементов, а также оптимизировали работу с памятью на
20-30 процентов, как указано в документации, поэтому формат OrderedDict утерял значение.
'''

create_operations = dict(my_dict="""{k:randint(0, 50) for k in range(100)}""",
                         my_ordered_dict="""OrderedDict({k:randint(0, 50) for k in range(100)})""")

for name, text in create_operations.items():
    print(f"Создание и заполнение {name}, {timeit(stmt=text, number=1000, globals=globals()):.5f}")

my_dict = {k: randint(0, 50) for k in range(100)}
my_ordered_dict = OrderedDict({k: randint(0, 50) for k in range(100)})


requesting_data = dict(my_dict_inx="""my_dict[5]""",
                       my_ordered_dict_inx="""my_ordered_dict[5]""")

add_data = dict(my_dict_add="""my_dict[100] = 100""",
                my_ordered_dict_add="""my_ordered_dict[100] = 100""")

sort_data = dict(my_dict_sorted_key="""sorted(my_dict)""",
                 my_ordered_dict_sorted_key="""sorted(my_ordered_dict)""",
                 my_dict_sorted_value="""sorted(my_dict.values())""",
                 my_ordered_dict_sorted_value="""sorted(my_ordered_dict.values())""",
                 my_dict_sorted_items="""sorted(my_dict.items())""",
                 my_ordered_dict_sorted_items="""sorted(my_ordered_dict.items())""")

pop_data = dict(
    my_dict_pop="""
new_dict = {1:1, 2:2, 3:3}
new_dict.popitem()""",
    my_ordered_dict_pop="""
new_ord_dict = OrderedDict({1:1, 2:2, 3:3})
new_ord_dict.popitem()""",
    my_ordered_dict_pop_F="""
new_ord_dict = OrderedDict({1:1, 2:2, 3:3})
new_ord_dict.popitem(last=False)""")

for name, text in requesting_data.items():
    print(f"Запрос элемента по индексу {name}, "
          f"{timeit(stmt=text, number=1000,globals=globals()):.5f}")

for name, text in add_data.items():
    print(f"Добавление {name}, {timeit(stmt=text, number=1000, globals=globals()):.5f}")

for name, text in sort_data.items():
    print(f"Сортировка {name}, {timeit(stmt=text, number=1000, globals=globals()):.5f}")

for name, text in pop_data.items():
    print(f"Удаление popitem {name}, {timeit(stmt=text, number=1000, globals=globals()):.5f}")
