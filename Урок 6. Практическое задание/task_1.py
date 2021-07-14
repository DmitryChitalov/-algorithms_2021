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
from timeit import default_timer
from random import choice
from functools import reduce
from memory_profiler import memory_usage
from recordclass import recordclass
from pympler import asizeof


def decor(func):
    """ Decorator for measuring time and memory"""
    def wrapper(*args):
        m1 = memory_usage()
        start_time = default_timer()
        res = func(args[0])
        my_time = f"{(default_timer() - start_time):.5f}"
        m2 = memory_usage()
        mem_diff = f"{(m2[0] - m1[0]):.5f}"
        return res, mem_diff, my_time
    return wrapper


"""
Скрипт 1. (ДЗ к 3 уроку Основ Python)
Задание:
Реализовать функцию get_jokes(), возвращающую n шуток,
сформированных из трех случайных слов, взятых из трёх списков:
nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]

Анализ: использование генератора существенно уменьшило затраты памяти, сохранив
функциональность кода. Также возросла скорость. Использование recordclass в данной
ситуации не повлияло, но было указано сделать минимум 2 реализации на каждый скрипт,
было сложно придумать еще одну, которая бы улучшила успехи генератора.

Из-за того, что все функции находятся в одном скрипте, данные замеров памяти не будут
корректными, поэтому приложу замеры каждого варианта скрипта, выполненные по отдельности:

Результаты замеров вариантов (усредненные показатели):
1) изначальный - 0.14453 Mib, 0.00457 сек
2) с генератором - 0.01953 Mib, 0.00001 сек
3) с генератором и recordclass - 0.01953 Mib, 0.00001 сек
"""


# Изначальное решение:
@decor
def get_jokes_original(n):
    """Returns n jokes that are made up of random words from three internal lists"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    list_jokes = []
    for inx in range(n):
        list_jokes.append(f"{choice(nouns)} {choice(adverbs)} {choice(adjectives)}")
    return list_jokes


# Вместо создания списка и его возвращения функцией использован генератор с yield:

@decor
def get_jokes_gen(n):
    nouns_2 = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs_2 = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives_2 = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    for inx in range(n):
        yield f"{choice(nouns_2)} {choice(adverbs_2)} {choice(adjectives_2)}"


# Третий вариант дополнен использованием recordclass:

@decor
def get_jokes_gen_rec(n):
    """Returns n jokes that are made up of random words from three internal lists"""
    nouns_3 = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs_3 = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives_3 = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    var_1 = recordclass('info', ('x', 'y', 'z'))
    for inx in range(n):
        yield var_1(choice(nouns_3), choice(adverbs_3), choice(adjectives_3))


"""
Скрипт 2. (ДЗ ко 2 уроку Алгоритмы и структуры данных на Python)
Задание:
Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран (мы его решали через рекурсию).

Анализ: генератор оказался выгоднее с точки зрения памяти, чем рекурсия. Затраты
по времени равны.
Сначала я сделала вариант с использованием map, так как он мне казался очевидным.
Но ради интереса испробовала и более "наивный" вариант с for и конкатенацией. Результат
удивил - выигрыш по памяти оказался еще существеннее, добавился выигрыш по времени.
Вывод сделала такой: даже самые удобные инструменты должны использоваться в зависимости
от ситуации и от того, что важнее: стиль кода, затраты времени или памяти.

Замеры проводились с выводом на печать, я ее закомментировала для того, чтоб она не
мешала в данном скрипте.
Результаты замеров вариантов:
1) изначальный - 0.03516 Mib, 0.00020 сек
2) с генератором, map и join - 0.02344 Mib, 0.00020 сек
3) с генератором, циклом for и конкатенацией - 0.01953 Mib, 0.00016 сек

C json хороших примеров из старых ДЗ не нашла, но для себя испробовала и замерила - 
разница есть даже на маленьких словарях. Для array numpy тоже не вижу хороших примеров
из ДЗ, испробовала на профилировании чужого кода (новичков на stackoverflow)
"""


# Изначальное решение:
@decor
def flip_a_number_01(user_num):
    def flipping(num):
        surplus = str(num % 10)
        if num <= 10:
            return surplus
        return surplus + flipping(num // 10)
    my_num = flipping(user_num)
    # print(f"Перевернутое число: {flipping(user_num)}")
    return my_num


# Решение с ленивыми вычислениями и map:
def flipping_01(num):
    while num > 0:
        yield str(num % 10)
        num = num // 10


@decor
def flip_a_number_02(num):
    my_num = "".join(x for x in map(lambda i: i, flipping_01(num)))
    # print(f"Перевернутое число: {my_num}")
    return my_num


# Решение с ленивыми вычислениями и конкатенацией:
def flipping_02(num):
    while num > 0:
        yield str(num % 10)
        num = num // 10


@decor
def flip_a_number_03(num):
    my_num = ''
    for x in flipping_02(num):
        my_num = my_num+x
    # print(f"Перевернутое число: {my_num}")


"""
Скрипт 3. (ДЗ ко 2 уроку Алгоритмы и структуры данных на Python)
Задание:
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
(мы его решали через рекурсию).

Анализ: рекурсия затратнее генератора с точки зрения памяти и времени выполнения.
Ее сильное место - стиль и экономия строк кода, когда нужно произвести много
сложных, но однотипных и последовательных вычислений.
Я использовала функции map и reduce вкупе с ленивыми вычислениями, они дали
уменьшение затрат памяти и времени выполнения скрипта. Их показатели примерно
равны, поэтому я не стала выносить их в отдельные решения.
Третьим решением снова был "наивный" цикл for и генератор, мне хотелось подтвердить
или опровергнуть вывод со скриптом 2. Он подтвердился, у этого варианта - самые
лучшие показатели скорости и затрат памяти. Видимо он и правда хорош в случаях, где
вычисления просты.


Замеры проводились с выводом на печать, я ее снова закомментировала.
Результаты замеров вариантов:
1) изначальный - 0.03906 Mib, 0.00021 сек
2) с генератором и map/reduce - 0.01953 Mib, 0.00019 сек
3) с генератором и циклом for - 0.01562 Mib, 0.00018 сек
"""


# Изначальное решение:
@decor
def snake_row_01(user_num_el):
    def calculation(num_el, elementary=1.0):
        if num_el == 1:
            return elementary
        return elementary + calculation(num_el-1, elementary=-(elementary / 2))
    return calculation(user_num_el)
    # print(f"Количество элементов: {user_num_el}, их сумма: {calculation(user_num_el):.5f}")


# Решение с генератором, map/reduce:
def calc_01(num):
    elementary = 1.0
    while num > 0:
        yield elementary
        elementary /= -2
        num -= 1


@decor
def snake_row_02(num_el):
    my_num = reduce(lambda x, y: x+y, calc_01(num_el))
    # my_num = sum(map(lambda x: x, calc(num_el)))
    # print(f"Количество элементов: {num_el}, их сумма: {my_num:.5f}")
    return my_num


# Решение с генератором и циклом for:
def calc_02(num):
    elementary = 1.0
    while num > 0:
        yield elementary
        elementary /= -2
        num -= 1


@decor
def snake_row_03(num_el):
    my_num = 0
    for x in calc_02(num_el):
        my_num = my_num+x
    # print(f"Количество элементов: {num_el}, их сумма: {my_num:.5f}")
    return my_num


#####################################################################################
"""
Также я испробовала метод уменьшения затрат памяти с использованием __slots__ на 
реализованном в ДЗ 11 Основ Python классе. Его не выношу как отдельно решенный скрипт,
т.к. тут оптимизация только в __slots__.
Результаты __slots__ и __dict__: 224 и 400 соответственно.

class Date:
    __slots__ = ['date_str']
    def __init__(self, date_str):
        tmp_data = self.get_elements(date_str)
        self.checkout(tmp_data)
        self.date_str = tmp_data

    @classmethod
    def get_elements(cls, date_str):
        try:
            result = [int(i) for i in date_str.split('-')]
            return result
        except (ValueError, AttributeError) as e:
            print(e, "Дата должна быть в виде строки формата «день-месяц-год», "
                  "\nгде день, месяц и год - положительные целые числа")
            exit(1)

    @staticmethod
    def checkout(list_num):
        msg = "Ошибочное значение дня, месяца или года"
        check_condition = [list_num[0] in range(1, 32), list_num[1] in range(1, 13),
                           list_num[2] > 0]
        if not all(check_condition):
            raise ValueError(msg)
"""
#####################################################################################
if __name__ == '__main__':
    res_01, mem_diff_01, my_time_01 = get_jokes_original(1000)
    print(f"get_jokes_original: {mem_diff_01} Mib, "
          f"скорость выполнения {my_time_01} сек")

    res_02, mem_diff_02, my_time_02 = get_jokes_gen(1000)
    # for i in res_02:
    #     print(i)
    print(f"get_jokes_gen: {mem_diff_02} Mib, "
          f"скорость выполнения {my_time_02} сек")

    res_03, mem_diff_03, my_time_03 = get_jokes_gen_rec(1000)
    # for i in res_03:
    #     print(i)
    print(f"get_jokes_gen_rec: {mem_diff_03} Mib, "
          f"скорость выполнения {my_time_03} сек")

    res_04, mem_diff_04, my_time_04 = flip_a_number_01(132345678900987654324142567223)
    print(f"flip_a_number_01: {mem_diff_04} Mib, "
          f"скорость выполнения {my_time_04} сек")

    res_05, mem_diff_05, my_time_05 = flip_a_number_02(132345678900987654324142567223)
    print(f"flip_a_number_02: {mem_diff_05} Mib, "
          f"скорость выполнения {my_time_05} сек")

    res_06, mem_diff_06, my_time_06 = flip_a_number_03(132345678900987654324142567223)
    print(f"flip_a_number_03: {mem_diff_06} Mib, "
          f"скорость выполнения {my_time_06} сек")

    res_07, mem_diff_07, my_time_07 = snake_row_01(50)
    print(f"snake_row_01: {mem_diff_07} Mib, "
          f"скорость выполнения {my_time_07} сек")

    res_08, mem_diff_08, my_time_08 = snake_row_02(50)
    print(f"snake_row_02: {mem_diff_08} Mib, "
          f"скорость выполнения {my_time_08} сек")

    res_09, mem_diff_09, my_time_09 = snake_row_03(50)
    print(f"snake_row_03: {mem_diff_09} Mib, "
          f"скорость выполнения {my_time_09} сек")

# # Для замеров __slots__ и __dict__
#
#     my_new_obj = Date('14-12-2001')
#     print(asizeof.asizeof(my_new_obj)) #400 и 224 соответственно
