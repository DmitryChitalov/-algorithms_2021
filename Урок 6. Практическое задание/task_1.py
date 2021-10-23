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
import memory_profiler
from timeit import default_timer
from pympler import asizeof
from itertools import islice


def get_time_and_memory(func):
    """
    Декоратор для замера времени выполнения и использования ОЗУ.
    Возвращает только замеряемые параметры.
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        start_time = default_timer()
        func(args[0])
        m2 = memory_profiler.memory_usage()
        return f"memory: {m2[0] - m1[0]}, time: {default_timer() - start_time}"

    return wrapper


def get_time_and_memory_and_result(func):
    """
    Декоратор для замера времени выполнения и использования ОЗУ.
    Возвращает результат вычисления функции.
    :param func:
    :return:
    """

    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        start_time = default_timer()
        result = func(args[0])
        m2 = memory_profiler.memory_usage()
        print(f"memory: {m2[0] - m1[0]}, time: {default_timer() - start_time}")
        return result

    return wrapper


"""
Вариант 1. Задание с курса основ.
Будем переписывать возврат списка нечётных чисел, на возврат генератора.
"""


@get_time_and_memory
def odd_nums(number):
    """
    Лист нечётных чисел от 1 до n (включительно)
    :param list:
    :return:
    """
    odd_list = [num for num in range(1, number + 1, 2)]
    return odd_list


@get_time_and_memory
def odd_nums_optimisation(number):
    """
    Генератор нечётных чисел от 1 до n (включительно)
    :param list:
    :return:
    """
    for num in range(1, number + 1, 2):
        yield num


my_number = 10000000

print(odd_nums(my_number))
print(*islice(odd_nums_optimisation(my_number), my_number))

"""
До оптимизации: memory: 0.41015625, time: 0.4776648000000001
После: memory: 0.0, time: 0.10974119999999998
При большом количестве вычисляемых элементов, генератор даёт преимущество.
"""

"""
Вариант 2. Задача с текущего курса. Получение перевёрнутого числа.
Будем переписывать рекурию на срез.
"""


@get_time_and_memory_and_result
def get_revers_number(input_number, revers_number=[]):
    """
    Получение перевёрнутого числа.
    :param input_number:
    :param revers_number:
    :return:
    """
    if input_number == 0:
        return "".join(str(e) for e in revers_number)
    else:
        remainder = input_number % 10
        revers_number.append(remainder)
        input_number = input_number // 10
        return get_revers_number(input_number, revers_number)


my_number = 34543756756756756767897353454365776899800657670
revs_number = get_revers_number(my_number)
print(f"Перевернутое число: {revs_number}")


@get_time_and_memory_and_result
def get_revers_number(input_number):
    return str(input_number)[::-1]


print()
revs_number = get_revers_number(my_number)
print(f"Перевернутое число: {revs_number}")

"""
memory: 0.0, time: 0.10711470000000034
memory: 0.0, time: 0.3284741000000002
memory: 0.00390625, time: 0.5471247000000004
memory: 0.0078125, time: 0.7660628999999997
memory: 0.0078125, time: 0.9804736000000007
memory: 0.01171875, time: 1.1985298000000002
memory: 0.015625, time: 1.417383
memory: 0.01953125, time: 1.6347900000000006
memory: 0.01953125, time: 1.8502759000000006
memory: 0.0234375, time: 2.0660552
memory: 0.02734375, time: 2.2828121999999995
memory: 0.02734375, time: 2.4990752999999994
memory: 0.03125, time: 2.7144477999999994
memory: 0.03515625, time: 2.9336557
memory: 0.0390625, time: 3.1522076000000006
memory: 0.0390625, time: 3.3692450000000003
memory: 0.04296875, time: 3.5894763000000003
memory: 0.046875, time: 3.8062154999999995
memory: 0.05078125, time: 4.0221176
memory: 0.05078125, time: 4.2389595
memory: 0.0546875, time: 4.457179399999999
memory: 0.05859375, time: 4.674952800000001
memory: 0.05859375, time: 4.8953519
memory: 0.0625, time: 5.1120396999999995
memory: 0.0625, time: 5.327154900000001
memory: 0.0625, time: 5.54634
memory: 0.0625, time: 5.7632098
memory: 0.0625, time: 5.9817689000000005
memory: 0.0625, time: 6.198745199999999
memory: 0.0625, time: 6.415025399999999
memory: 0.0625, time: 6.6310992
memory: 0.0625, time: 6.848371499999999
memory: 0.0625, time: 7.0689358
memory: 0.0625, time: 7.2836748
memory: 0.0625, time: 7.497774300000001
memory: 0.0625, time: 7.7162983999999994
memory: 0.0625, time: 7.9319119
memory: 0.0625, time: 8.147454100000001
memory: 0.0625, time: 8.3619114
memory: 0.0625, time: 8.577502
memory: 0.0625, time: 8.7914623
memory: 0.0625, time: 9.009523399999999
memory: 0.0625, time: 9.226925999999999
memory: 0.0625, time: 9.4429327
memory: 0.0625, time: 9.6604098
memory: 0.0625, time: 9.8787541
memory: 0.0625, time: 10.0947116
memory: 0.0625, time: 10.3131657
Перевернутое число: 07675600899867756345435379876765765765765734543

memory: 0.0, time: 0.10821870000000011
Перевернутое число: 07675600899867756345435379876765765765765734543

Очевидно, использование среза, для реверса числа, гораздо эффективней рекурсии.
"""


"""
Вариант 3. Задание с курса основ.
Добавим использование слотов.
"""


class Road:

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def calc_weight(self):
        m = (self.__length * self.__width * 25 * 5) / 1000
        return round(m, 2)


r = Road(20, 5000)
print()
print(asizeof.asizeof(r))
print(f"Необходимо {r.calc_weight()} тонн")


class NewRoad:
    __slots__ = ('length', 'width')

    def __init__(self, length, width):
        self.length = length
        self.width = width

    def calc_weight(self):
        m = (self.length * self.width * 25 * 5) / 1000
        return round(m, 2)


r2 = NewRoad(20, 5000)
print()
print(asizeof.asizeof(r2))
print(f"Необходимо {r2.calc_weight()} тонн")


"""
Общий размер обьекта: 344 
Необходимо 12500.0 тонн

Общий размер обьекта: 112
Необходимо 12500.0 тонн

Использование конструкции __slots__, позволяет не использовать динамический словарь 
для хранения атрибутов и их значений. В данном примере заменено на кортеж, что позволило съэкономить память.
"""
