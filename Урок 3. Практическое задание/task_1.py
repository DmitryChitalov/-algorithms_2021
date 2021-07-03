"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность.
   Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

import time
import timeit


def time_dec(func):
    def wrapper(*args):
        start_val = time.time()
        result = func(*args)
        end_val = time.time()
        print(f"Время выполнения {func.__name__}: {end_val - start_val:.4f} сек")
        return result
    return wrapper


@ time_dec
def fill_dict(num):
    new_dict = {elem + 1: str(elem) for elem in range(num)}
    return new_dict
# Сложность функции в работе - O(1), так как мы каждый раз передаем конкретное значение num


@ time_dec
def fill_list(num):
    new_list = [elem + 1 for elem in range(num)]
    return new_list
# Сложность функции в работе - O(1), так как мы каждый раз передаем конкретное значение num


fill_dict(100000)
# у меня занимает ~ 0.0312 - 0.0469 сек
fill_list(100000)
# у меня занимает ~ 0.0000 - 0.0156 сек

'''
a) Вывод:
Dict comprehension чуть медленнее, чем list comprehension, так как создаются
не только ключи, но и значения, а также выполняется встроенное хэширование.
В документации Python указано, что comprehensions обычно быстрее, чем циклы.
Сomprehensions хороши там, где нужно создать не очень большие объекты списков
или словарей.

Ради интереса я попробовала заполнение словаря и списка через map.
Выводы меня удивили: заполнение словаря через map оказалось быстрее, чем comprehensions,
а вот списка - медленнее. Не могли бы вы объяснить, чем такое различие обусловлено?
'''


@ time_dec
def fill_dict_with_map(num):
    return dict(map(lambda x: (x, x+1), range(1, num)))
# Честно говоря, я не нашла информации о стоимости map, но могу предположить, что в
# данном случае сложность та же O(1), так как мы каждый раз передаем конкретное значение num


@ time_dec
def fill_list_with_map(num):
    return list(map(lambda b: b + 1, range(1, num)))
# Сложность, думаю, та же - O(1)


fill_dict_with_map(100000)
# у меня занимает ~ 0.0156 - 0.0313 сек
fill_list_with_map(100000)
# у меня занимает ~ 0.0140 - 0.0156 сек

'''
b) Вывод:
На вебинаре вы упомянули, что требуется выполнить вставку, получение, удаление элемента.
Я реализовала эти действия несколькими способами.
Все они выполняются с очень высокой скоростью.

Вне рамок основного задания мне было интересно испробовать еще один вариант замеров:
функцию timeit созвучного модуля с числом циклов измерений, равным 1000, чтоб лучше
оценить скорости операций.
Я протестировала им часть функций ниже.

Вставка элемента:
- скорость вставки эл-в словаря методом присвоения и эл-в списка методом append почти не отличаются;
- метод insert имеет сложность O(n) и уступает методу append (O(1)) для списков по скорости;

Получение элемента:
- сложность получения элемента каждой из функций O(1) и скорости почти одинаковы;

Удаление элемента:
- методы pop для списка и словаря имеют одинаковую сложность О(1);
- методы del для списка и словаря имеют сложности О(n) и О(1) соответственно.
  del для словаря шустрее за счет встроенного хэширования.
'''

my_list = [1, 2, 3, 4, 5]
my_dict = {1: '0', 2: '1', 3: '2', 4: '3', 5: '4'}


# ВСТАВКА ЭЛЕМЕНТА
@time_dec
def adding_element_dict(some_dict):   # O(1)
    some_dict['15'] = 'пятнадцать'
    return some_dict


@time_dec
def insert_element_list(some_list):   # O(n)
    some_list.insert(0, 5)
    return some_list


@time_dec
def append_element_list(some_list):   # O(1)
    some_list.append(5)
    return some_list


adding_element_dict(my_dict)
insert_element_list(my_list)
append_element_list(my_list)


# ПОЛУЧЕНИЕ ЭЛЕМЕНТА
@time_dec
def appeal_by_index_dict(some_dict):  # O(1)
    return some_dict[1]


@time_dec
def get_element_dict(some_dict):      # O(1)
    return some_dict.get(2)


@time_dec
def appeal_by_index_list(some_list):  # O(1)
    return some_list[0]


appeal_by_index_dict(my_dict)
get_element_dict(my_dict)
appeal_by_index_list(my_list)


# УДАЛЕНИЕ ЭЛЕМЕНТА
@time_dec
def pop_element_dict(some_dict):   # O(1)
    return some_dict.pop(3)


@time_dec
def pop_element_list(some_list):   # O(1)
    return some_list.pop(0)


@time_dec
def del_element_dict(some_dict):   # O(1)
    del some_dict['15']
    return some_dict


@time_dec
def del_element_list(some_list):   # O(n)
    del some_list[0]
    return some_list


pop_element_list(my_list)
del_element_list(my_list)
pop_element_dict(my_dict)
del_element_dict(my_dict)


# ЗАМЕРЫ ФУНКЦИЙ ВСТАВКИ ЭЛЕМЕНТА функцией timeit
def adding_element_dict_2(some_dict):
    some_dict['15'] = 'пятнадцать'
    return some_dict


def insert_element_list_2(some_list):
    some_list.insert(0, 5)
    return some_list


def append_element_list_2(some_list):
    some_list.append(5)
    return some_list


print(f"\nВремя выполнения adding_element_dict 1000 операций: "
      f"{timeit.timeit('adding_element_dict_2(my_dict)', number=1000, globals=globals()):.5f}")
print(f"Время выполнения insert_element_list 1000 операций: "
      f"{timeit.timeit('insert_element_list_2(my_list)', number=1000, globals=globals()):.5f}")
print(f"Время выполнения append_element_list 1000 операций: "
      f"{timeit.timeit('append_element_list_2(my_list)', number=1000, globals=globals()):.5f}")
