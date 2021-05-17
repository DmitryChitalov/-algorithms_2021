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

# Простой пример, вычисляющий сумму чисел списка путем рекурсии. Ниже
# рекурсия заменена на цикл. Рекурсия, ожидаемо, потребляет больше памяти.
# Так же ниже представлена попытка объеденить в декораторе замеры времени и памяти.
# Он не работает так, как планировалось, поэтому был использован встроенный.


from memory_profiler import profile


# def time_und_memory(func):
#     import time
#     import memory_profiler
#
#     def wrapper(*args, **kwargs):
#
#         m_1 = memory_profiler.memory_usage()
#         func()
#         m_2 = memory_profiler.memory_usage()
#
#         start_time = time.time()
#         func()
#         end_time = time.time()
#
#         return f'Выполнение кода заняло {end_time - start_time} секунд.\n' \
#                f'Памяти потребовалось - {m_2[0] - m_1[0]}.'
#
#     return wrapper


@profile
def get_total_1(i=100, total=0):

    if i == 0:
        return total
    else:
        return get_total_1(i - 1, (total + i))


get_total_1()


@profile
def get_total(n=100):
    total = 0
    for number in list(range(n + 1)):
        total = total + number
    return total


get_total()


# Ниже приведен пример с использованием различного форматирования строк. f - строка
# занимает чуть больше памяти, чем метод .format


@profile
def print_text(some_text):
    return f'{some_text}'


print_text('Пример текста')


@profile
def print_some_text():
    return '{0}, {1}, {2}'.format('a', 'b', 'c')


print_some_text()


# Ниже приведен пример с удалением ненужного списка из памяти для ее освобождения.


@profile
def even():
    list_1 = [i for i in range(1, 100) if i % 2 == 0]
    len_list = len(list_1)
    del list_1
    return len_list


even()
