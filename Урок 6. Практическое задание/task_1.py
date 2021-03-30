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

from timeit import default_timer
from memory_profiler import memory_usage


def memory_profile(func):
    def wrapper(*args):
        start_time = default_timer()
        start_memory = memory_usage()
        func(*args)
        end_time = default_timer()
        end_memory = memory_usage()
        print(f'затраты времени: {end_time - start_time}\n затраты памяти: {end_memory[0] - start_memory[0]}')

    return wrapper


# 1

@memory_profile
def reverse_number_1(number_to_rev):
    def rev_wrap(number, reverse_digits_list=None):
        if reverse_digits_list is None:
            reverse_digits_list = []

        digit = number % 10
        new_number = number // 10

        reverse_digits_list.append(digit)

        if new_number == 0:
            result = ''
            for number in reverse_digits_list:
                result += str(number)

            return result

        rev_wrap(new_number, reverse_digits_list)

    return rev_wrap(number_to_rev)


@memory_profile
def reverse_number_2(number):
    return str(number)[::-1]


reverse_number_1(123456789012345678901234567890123456789012345678901234567890657465836574856834092370237592)
reverse_number_2(123456789012345678901234567890123456789012345678901234567890657465836574856834092370237592)

'''
затраты времени: 0.1003
затраты памяти: 0.289
затраты времени: 0.1002
затраты памяти: 0.0

reverse_number_1 требует большего объема памяти из-за рекурсивной реализации
способ выполнения задачи через reverse_number_2 не требует больших объемов памяти из-за отсутсвия рекурсии и применения
встроенных функций
в обоих случаях скорость выполнения одинакова

также при реализации reverse_number_1 был дан ответ на задание 3: при попытке применить профилировщик памяти к рекурсивной
функции, будут выведены замеры памяти для каждого вызова рекурсивной функции. для осуществеления верного профилирования
памяти в такой ситуации необходимо обернуть рекурсивную функцию во вспомогательную функцию и осуществлять профилирование
памяти уже этой внешней (вспомогательной) функции, тогда в итоге выйдет один единственно верный результат затраченной
при выполнении памяти  
'''

# 2
'''
 Для чисел в пределах от 0 до number найти числа, кратные 20 или 21
'''


@memory_profile
def get_numbers_1(end_number):
    return [i for i in range(end_number) if i % 20 == 0 or i % 21 == 0]


@memory_profile
def get_numbers_2(end_number):
    numbers_list = list(range(end_number))
    for i in numbers_list:
        if i % 20 == 0 or i % 21 == 0:
            yield i


get_numbers_1(100000000)
get_numbers_2(100000000)

'''
затраты времени: 9.0831
затраты памяти: 0.352
затраты времени: 0.1004
затраты памяти: 0.0

использование генератора позволяет расходовать меньше памяти (т.к. итоговый массив не хранится в памяти), а также
позволяет снизить время выполнения скрипта
'''


# 3
@memory_profile
def int_to_str_list_1(numbers):
    numbers_new = []
    for num in numbers:
        numbers_new.append(str(num))
    return numbers_new


@memory_profile
def int_to_str_list_2(numbers):
    return list(map(str, numbers))


test_list = [i for i in range(10000000)]

int_to_str_list_1(test_list)
int_to_str_list_2(test_list)
'''
затраты времени: 3.0275
затраты памяти: 0.309
затраты времени: 2.3119
затраты памяти: 0.016

использование функции map() позволяет существенно снизить объем требуемой памяти и незначительно ускорить время
выполнения
'''
