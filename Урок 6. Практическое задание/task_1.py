"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
# Задача 1 из курса основы питона. Увеличим длину генерируемого списка и уберем вывод результата на экран,
# добавим профайлер памяти и замерим время исполнения
from memory_profiler import profile
from timeit import timeit
from random import randint
from numpy import array
from recordclass import recordclass
# Представлен список чисел. Необходимо вывести элементы исходного списка,
# значения которых больше предыдущего элемента.
# Пример исходного списка: [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55].
# Результат: [12, 44, 4, 10, 78, 123].


@profile()
def format_list():
    number_list = []
    for i in range(200000):
        number_list.append(randint(0, 10))
    new_number_list = [x for i, x in enumerate(number_list) if i == 0 or x > number_list[i-1]]
    return new_number_list


# print(format_list()) на 200000 элементах печать будет выглядеть спорно
# format_list() просто запуск также не нужен т.к. декоратор сработает при запуске из timeit
print(timeit("format_list()", globals=globals(), number=1))  # повторов ставим 1 т.к. иначе память будет считаться
# на каждый запуск и выдаваться табличка профайлера все время


#  первое заполнение списка заменим генератором и формирование итогового тоже.

@profile()
def format_list2():
    def random_list_generator():
        for i in range(200000):
            yield i, randint(0, 10)

    def main_generator(generator):
        for j, el in generator:
            if j == 0 or el > el_prev:
                yield el
            el_prev = el
            continue
    return list(main_generator(random_list_generator()))


print(timeit("format_list2()", globals=globals(), number=1))

#  Память сэкономить на больших списках сэкономить удалось, а вот время нет



# Задача 2 Приведен код, который позволяет сохранить в
# массиве индексы четных элементов другого массива. Попробуем запихать список в массив из Нумпай

@profile()
def func_2():
    nums = [randint(1, 50000) for el in range(1, 100000)]
    new_arr = [number for number, el in enumerate(nums) if el % 2 == 0]
    return new_arr


print(timeit("func_2()", globals=globals(), number=1))


@profile()
def func_2_numpy():
    nums = array([randint(1, 50000) for el in range(1, 100000)])
    new_arr = [number for number, el in enumerate(nums) if el % 2 == 0]
    return new_arr


print(timeit("func_2_numpy()", globals=globals(), number=1))

#  Действительно память значительно меньше затратилась, а вот время осталось таким же.

# Задача 3 Имеется хранилище с информацией о компаниях: название и годовая прибыль.
# Для реализации хранилища можно применить любой подход,
# который вы придумаете, например, реализовать словарь.
# Реализуйте поиск трех компаний с наибольшей годовой прибылью.
# Выведите результат.

# Заменим словарь на recordclass
@profile()
def top3_3():
    storage = {"gazflot": 500,
               "gazprem": 1500,
               "nashneft": 5200,
               "glavrpz": 50,
               "gazmyas": 7950,
               "aeroflot": 100}
    res_list = []
    for i in range(0, 3):
        a = max(storage, key=lambda x: storage.get(x))   # функция max со сложностью O(n)
        res_list.append(a)
        storage.pop(a)
    return res_list


print(timeit("top3_3()", globals=globals(), number=1))

# @profile()
def top3_3_recordclass():

    StorageNames = recordclass('StorageNames', 'gazflot gazprem nashneft glavrpz gazmyas aeroflot')
    storage = StorageNames(500, 1500, 5200, 50, 7950, 100)
    print(storage)
    print(storage.__doc__)
    print(max(storage))
# И тут я потерпел жесточайшее фиаско. Как перебирать ключи или, как их возвращать? Хранить отдельнов кортеже?
# могу выбрать максимум на лету, но чтобы отобрать второй по величине элемент, уже надо мучиться. Голову сломал
# но уже жалею, что связался с этим классом. Упрямство не дает оставить попытки.

    # for i in range(0, 3):
    #      a = max(storage)
    #      res_list.append(a)
    #      storage.pop(a)
    # return res_list


print(top3_3_recordclass())
# print(timeit("top3_3_recordclass", globals=globals(), number=1))
