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

from memory_profiler import memory_usage
from timeit import default_timer
from numpy import array
from collections import defaultdict
from collections import namedtuple
from recordclass import recordclass
import random
from string import ascii_letters
from json import dumps


def decor(func):
    def wrapper(args):
        time_start = default_timer()
        m1 = memory_usage()
        result = func(args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        timing = default_timer() - time_start
        return result, timing, mem_diff

    return wrapper


print('Выполнение функции my_func_1')

# Простая функция, выполняющая вывод нечётных чисел, до заданного числа (с помощью list comprehentions).
# Для маленьких чисел вполне безопасная, но при использовании больших чисел займёт очень много оперативной памяти.
@decor
def my_func_1(n):
    my_list = [i for i in range(1, n, 2)]
    return my_list


if __name__ == '__main__':
    result, timing, mem_diff = my_func_1(10000000)
    print(f'Время: {timing}, память: {mem_diff} MiB')
    
# Время: 0.49221086502075195, память: 193.9453125 MiB

print('Выполнение функции my_func_2')

# Воспользуемся библиотекой NumPy:
@decor
def my_func_2(n):
    my_list = array([i for i in range(1, n, 2)])
    return my_list


if __name__ == '__main__':
    result, timing, mem_diff = my_func_2(10000000)
    print(f'Время: {timing}, память: {mem_diff} MiB')

# Время: 0.9398412704467773, память: 19.61328125 MiB
# Возможности библиотеки NumPy помогли значительно снизить затраты оперативной памяти.
# Однако на реализаци этих самых возможностей нам потребовалось время, из-за чего функция отработала медленнее.

print('Выполнение функции my_func_3')
# Воспользуемся генератором:
@decor
def my_func_3(n):
    for i in range(1, n, 2):
        yield i


if __name__ == '__main__':
    result, timing, mem_diff = my_func_3(10000000)
    print(f'Время: {timing}, память: {mem_diff} MiB')
    
# Время: 0.22286105155944824, память: 0.0 MiB
# Как мы видим функция с генератором отработала не только без затрат оперативной памяти, но и быстрее.
# Это объясняется тем, что в генераторе элемент (в данном случае число) удаляется сразу же после вывода

# Вывод: генераторы не всегдаподходят для решения, но если есть возможность (как в данном случае),
# то лучше использовать их. Ибо и затраты оперативной памяти отсутствуют, и во времени мы получаем преимущество.

########################################################################################################################

print('Выполнение функции mult_and_sum_1')
# Функция нахождения суммы и произведения двух шестнадцатиричнных чисел из урока 5:
@decor
def mult_and_sum_1(nums):
    numbers = defaultdict(list)
    fst_num, sec_num = nums.split()
    numbers[fst_num] = list(fst_num)
    numbers[sec_num] = list(sec_num)
    my_sum = 0
    my_mult = 1

    for i in numbers.values():
        my_sum += (int(''.join(i), 16))
        my_mult *= int(''.join(i), 16)

    return f'Сумма введённых чисел равна {list(str(hex(my_sum))[2:])}. Произведение введённых чисел равна {list(str(hex(my_mult))[2:])}'


if __name__ == '__main__':
    result, timing, mem_diff = mult_and_sum_1("12A34BC23E6756C 56D78DF5678CE90F")
    print(f'Время: {timing}, память: {mem_diff} MiB')

# Время: 0.20985200000000004, память: 0.00390625 MiB
# У данной функции не очень больщие затраты памяти, но мы постараемся ещё сократить их.

print('Выполнение функции mult_and_sum_2')
# Воспользуемся встроенной функцией map:
@decor
def mult_and_sum_2(nums):
    numbers = defaultdict(list)
    fst_num, sec_num = nums.split()
    numbers[fst_num] = list(fst_num)
    numbers[sec_num] = list(sec_num)
    my_sum = 0
    my_mult = 1

    for i in numbers.values():
        my_sum += (int(''.join(i), 16))
        my_mult *= int(''.join(i), 16)

    return f'Сумма введённых чисел равна {list(map(list, str(hex(my_sum))[2:]))}. Произведение введённых чисел равна {list(map(list, str(hex(my_mult))[2:]))}'


if __name__ == '__main__':
    result, timing, mem_diff = mult_and_sum_2("12A34BC23E6756C 56D78DF5678CE90F")
    print(f'Время: {timing}, память: {mem_diff} MiB')

# Время: 0.21870069999999997, память: 0.0 MiB
# Функция map помогла избавиться от затрат памяти, но немного увеличила время выполнения основной функции.
# Скорее всего этого результата нам помогает достичь то, что map обходится без использования явного цикла for.
# Однако, подобное решение "проблемы" с памятью приводит к увеличению времени

print('Выполнение функции mult_and_sum_3')
@decor
def mult_and_sum_3(nums):
    numbers = defaultdict(list)
    fst_num, sec_num = nums.split()
    numbers[fst_num] = list(fst_num)
    numbers[sec_num] = list(sec_num)
    my_sum = 0
    my_mult = 1

    for i in numbers.values():
        my_sum += (int(''.join(i), 16))
        my_mult *= int(''.join(i), 16)
    yield f'Сумма введённых чисел равна {list(str(hex(my_sum))[2:])}. Произведение введённых чисел равна {list(str(hex(my_mult))[2:])}'


if __name__ == '__main__':
    result, timing, mem_diff = mult_and_sum_3("12A34BC23E6756C 56D78DF5678CE90F")
    print(f'Время: {timing}, память: {mem_diff} MiB')

# Время: 0.21804499999999993, память: 0.0 MiB
# Использование генератора вновь помогло нам избавиться от затрат памяти,
# но от увеличения затрат времени уйти не удалось.
# Вывод: в данном случае и map и генератор справились с задачей одинаково.

########################################################################################################################


print('Выполнение функции income_1')

# Немного преобразованная функция из первого задания пятого урока
@decor
def income_1(n):
    info = {}
    comp_amount = n  # количество компаний
    Company = namedtuple('Company', ['comp_name', 'inc_1', 'inc_2', 'inc_3', 'inc_4'])
    for i in range(comp_amount):
        name = random.choice(ascii_letters)  # Имя компании
        inc_1 = random.randint(1000, 100000) # Прибыльза первый квартал
        inc_2 = random.randint(1000, 100000) # Прибыль за второй квартал
        inc_3 = random.randint(1000, 100000) # Прибыль за третий квартал
        inc_4 = random.randint(1000, 100000) # Прибыль за четвёртый квартал
        comp = Company(name, int(inc_1), int(inc_2), int(inc_3), int(inc_4))
        info[comp.comp_name] = (comp.inc_1 + comp.inc_2 + comp.inc_3 + comp.inc_4) # Вставка компании и её годовой прибылли в словарь
    return info


if __name__ == '__main__':
    result, timing, mem_diff = income_1(20)
    print(f'Время: {timing}, память: {mem_diff} MiB')

# Время: 0.21180939999999998, память: 0.00390625 MiB
# Из-за рандома объём занимаемой памяти непостоянен. Но без него пришлось бы использовать input,
# а это бы очень сильно сказалось на замерах времени.

print('Выполнение функции income_2')
# Попробуем использовать модуль recordclass
@decor
def income_2(n):
    info = {}
    comp_amount = n  # количество компаний
    Company = recordclass('Company', ['comp_name', 'inc_1', 'inc_2', 'inc_3', 'inc_4'])
    for i in range(comp_amount):
        name = random.choice(ascii_letters)  # Имя компании
        inc_1 = random.randint(1000, 100000) # Прибыльза первый квартал
        inc_2 = random.randint(1000, 100000) # Прибыль за второй квартал
        inc_3 = random.randint(1000, 100000) # Прибыль за третий квартал
        inc_4 = random.randint(1000, 100000) # Прибыль за четвёртый квартал
        comp = Company(name, int(inc_1), int(inc_2), int(inc_3), int(inc_4))
        info[comp.comp_name] = (comp.inc_1 + comp.inc_2 + comp.inc_3 + comp.inc_4) # Вставка компании и её годовой прибылли в словарь
    return info


if __name__ == '__main__':
    result, timing, mem_diff = income_2(20)
    print(f'Время: {timing}, память: {mem_diff} MiB')

# Время: 0.2171494, память: 0.00390625 MiB
# Модуль recordclass никак не помог уменьшить расход памяти

print('Выполнение функции income_3')
# Воспользуемся созданием дампа
@decor
def income_3(n):
    info = {}
    comp_amount = n  # количество компаний
    Company = recordclass('Company', ['comp_name', 'inc_1', 'inc_2', 'inc_3', 'inc_4'])
    for i in range(comp_amount):
        name = random.choice(ascii_letters)  # Имя компании
        inc_1 = random.randint(1000, 100000) # Прибыльза первый квартал
        inc_2 = random.randint(1000, 100000) # Прибыль за второй квартал
        inc_3 = random.randint(1000, 100000) # Прибыль за третий квартал
        inc_4 = random.randint(1000, 100000) # Прибыль за четвёртый квартал
        comp = Company(name, int(inc_1), int(inc_2), int(inc_3), int(inc_4))
        info[comp.comp_name] = (comp.inc_1 + comp.inc_2 + comp.inc_3 + comp.inc_4) # Вставка компании и её годовой прибылли в словарь
    dumped_info = dumps(info)
    return dumped_info


if __name__ == '__main__':
    result, timing, mem_diff = income_3(20)
    print(f'Время: {timing}, память: {mem_diff} MiB')


# Время: 0.2192757999999999, память: 0.0 MiB
# На создание дампа, конечно, потребовалось некоторое время, но оно не очень значительно.
# Зато мы смогли избавиться от затрат оперативной памяти: хранение данных ввиде строки намного меньше чем ввиде словаря.




