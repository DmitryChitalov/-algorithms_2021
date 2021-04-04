"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""
import re
from random import randint

from memory_profiler import memory_usage
from timeit import default_timer

def decor(func):
    def wrapper(*args,**kwargs):
        start = default_timer()
        memory = memory_usage()
        result = func(*args, **kwargs)
        print(f'Затрачено памяти {memory_usage()[0] - memory[0]}')
        print(f'Время выполнения: {default_timer()-start}')
        return result
    return wrapper

# Первый пример самый простой, эксперементальный.
@decor
def func1():
    my_list = [i for i in range(1000000)]
    return my_list

@decor
def func2():
    my_list = (i for i in range(1000000))
    yield my_list

print(f'Первый пример')
func1()
print()
func2()
print()
"""
В первом примере мы видим сравнение спискового включения и работу генератора. Генератор тратит меньше памяти, т.к. 
не хранит целый список, а выдает элемент по требованию (дальше церез цикл for)
"""

# Второй пример. Работа с файлом.

@decor
def one():
    with open("text.txt", "r", encoding="UTF-8") as file:
        text = file.read()
        memory = re.findall(r'опыт', text)
    return len(memory)


@decor
def two():
    with open("text.txt", "r", encoding="UTF-8") as file:
        text = file.read()
        memory = re.findall(r'опыт', text)
    del text
    return len(memory)

print(f'Второй пример')
one()
print()
two()
print()

"""
В этих примерах мы загружаем в переменную text  весь текст из файла, что занимает нашу память. Во второй функции 
мы удаляем эту ненужную переменную, и освобождаем память.
"""


# Третий пример решето Эратосфена

my_list = [randint(1,100) for i in range(100000)]
@decor
def eratosthenes_sieve():
    sample = my_list[:]
    sample[1] = 0
    i = 2
    while i < len(sample):
        if sample[i] != 0:
            j = i + i
            while j < len(sample):
                sample[j] = 0
                j = j + i
        i += 1

    return sample


@decor
def eratosthenes_sieve_clear():
    clear_arr = []
    sample2 = my_list[:]
    sample2[1] = 0
    i = 2
    while i < len(sample2):
        if sample2[i] != 0:
            j = i + i
            while j < len(sample2):
                sample2[j] = 0
                j = j + i
        i += 1
    for x in sample2:
        if x != 0:
            clear_arr.append(i)
    del sample2
    return clear_arr

print(f'Третий пример')
eratosthenes_sieve()
print()
eratosthenes_sieve_clear()

'''
По результатам у меня во втором примеребывает как минусовое значение так и ноль. В первой функции я просто
удалил все нулевые элементы и вывел список. Соответственно используется память подэтот список. Вторая функция
пробегает по готовому списку и не нулевые элементы добавляет в новый список. потом старый список удаляется за ненадобность.
по времени они идентичны. По памяти второй получается менее затратный.
'''