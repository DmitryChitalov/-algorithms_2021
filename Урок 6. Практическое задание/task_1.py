"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
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
from memory_profiler import memory_usage, profile
from recordclass import recordclass
from collections import namedtuple
from collections import deque
from timeit import default_timer


def decor(func):
    def wrapper(*args):
        start_time = default_timer()
        m1 = memory_usage()
        res = func(*args)
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        end_time = default_timer()
        print(f'Затраты времени: {end_time - start_time} сек.')
        return res, mem_diff
    return wrapper


@decor
@profile
def average_profit():
    try:
        n = int(input('Введите количество предприятий для расчета прибыли: '))
        i = 1
        firms = namedtuple('firm', 'name profit')
        base_firms = {}
        average = 0
        above_average = deque()
        below_average = deque()
        while i <= n:
            firma = input('Введите название предприятия: ')
            profit = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
            # sumprofit = sum(list(map(int, profit.split())))
            sumprofit = sum([int(n) for n in profit.split()])
            base_firm = firms(
                name=firma,
                profit=sumprofit
            )
            base_firms[firma] = base_firm
            i += 1
        for el in base_firms.values():
            average += el.profit
        average = average/n
        print(f'Средняя годовая прибыль всех предприятий: {average}')
        for el in base_firms.values():
            if average > el.profit:
                below_average.append(el.name)
            else:
                above_average.append(el.name)
        above_average = ', '.join(above_average)
        below_average = ', '.join(below_average)
        print(f'Предприятия, с прибылью выше среднего значения: {above_average}')
        print(f'Предприятия, с прибылью ниже среднего значения: {below_average}')
    except ValueError:
        print('Формат ввода прибыли 123 123 123 123')
        return average_profit()
    return ''

# Вариант 2


@decor
@profile
def average_profit1():
    try:
        n = int(input('Введите количество предприятий для расчета прибыли: '))
        i = 1
        firms = recordclass('firm', 'name profit')
        base_firms = {}
        average = 0
        above_average = deque()
        below_average = deque()
        while i <= n:
            firma = input('Введите название предприятия: ')
            profit = input('через пробел введите прибыль данного предприятия за каждый квартал(Всего 4 квартала): ')
            # sumprofit = sum(list(map(int, profit.split())))
            sumprofit = sum([int(n) for n in profit.split()])
            base_firm = firms(
                name=firma,
                profit=sumprofit
            )
            base_firms[firma] = base_firm
            i += 1
        for el in base_firms.values():
            average += el.profit
        average = average/n
        print(f'Средняя годовая прибыль всех предприятий: {average}')
        for el in base_firms.values():
            if average > el.profit:
                below_average.append(el.name)
            else:
                above_average.append(el.name)
        above_average = ', '.join(above_average)
        below_average = ', '.join(below_average)
        del average
        del base_firms
        print(f'Предприятия, с прибылью выше среднего значения: {above_average}')
        print(f'Предприятия, с прибылью ниже среднего значения: {below_average}')
    except ValueError:
        print('Формат ввода прибыли 123 123 123 123')
        return average_profit1()
    return ''


res, mem_diff = average_profit()
print(f"Выполнение заняло {mem_diff} Mib")
res1, mem_diff1 = average_profit1()
print(f"Выполнение заняло {mem_diff1} Mib")


# Вариант 1
# Выполнение заняло 0.40234375 Mib
# Вариант 2
# Выполнение заняло 0.140625 Mib
# Выполнение значительно дешевле благодаря убиранию ссылок, recordclass. Но согласно profile
# при мониторинге потребляет чуть больше памяти 2 вариант, но на выполние он значительно экономней

@decor
def no_lazy(num):
    numbers_list = list(range(num))
    for i in numbers_list:
        return i


@decor
def lazy(num):
    numbers_list = list(range(num))
    for i in numbers_list:
        yield i


res2, mem_diff2 = no_lazy(10000000)
print(f"Выполнение заняло {mem_diff2} Mib")
res22, mem_diff22 = lazy(10000000)
print(f"Выполнение заняло {mem_diff22} Mib")

# При использовании ленивых вычислений видно, что затраты памяти пракнически нет, так как вычисления откладываются до следущего вызова
# и тем самым мы экономим память


@decor
def lst_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


@decor
def generator_2(nums):
    return (i for i in range(len(nums)) if nums[i] % 2 == 0)


lst_p = [el for el in range(0,100000)]
res3, mem_diff3 = lst_1(lst_p)
print(f"Выполнение заняло {mem_diff3} Mib")
res33, mem_diff33 = generator_2(lst_p)
print(f"Выполнение заняло {mem_diff33} Mib")

# Генератор позволяет сократить память так, как он возвращает один элемент за другим
