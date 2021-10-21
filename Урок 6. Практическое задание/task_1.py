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

UsageInfo = namedtuple('UsageInfo', ['time', 'memory', 'result'])


def resource_usage_decorator(func):
    def wrapper(*args, **kwargs):
        time_start, memory_start = default_timer(), memory_profiler.memory_usage()
        return UsageInfo(result=func(args[0]), time=default_timer() - time_start,
                         memory=memory_profiler.memory_usage()[0] - memory_start[0])

    return wrapper


# ------------------------------------ 1 ------------------------------------#

'''
Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
Пример:
32 -   33 - ! 34 - " 35 - # 36 - $ 37 - % 38 - & 39 - ' 40 - ( 41 - )
42 - * 43 - + 44 - , 45 - - 46 - . 47 - / 48 - 0 49 - 1 50 - 2 51 - 3
52 - 4 53 - 5 54 - 6 55 - 7 56 - 8 57 - 9 58 - : 59 - ; 60 - < 61 - =
62 - > 63 - ? 64 - @ 65 - A 66 - B 67 - C 68 - D 69 - E 70 - F 71 - G
72 - H 73 - I 74 - J 75 - K 76 - L 77 - M 78 - N 79 - O 80 - P 81 - Q
82 - R 83 - S 84 - T 85 - U 86 - V 87 - W 88 - X 89 - Y 90 - Z 91 - [
92 - \ 93 - ] 94 - ^ 95 - _ 96 - ` 97 - a 98 - b 99 - c 100 - d 101 - e
102 - f 103 - g 104 - h 105 - i 106 - j 107 - k 108 - l 109 - m 110 - n 111 - o
112 - p 113 - q 114 - r 115 - s 116 - t 117 - u 118 - v 119 - w 120 - x 121 - y
122 - z 123 - { 124 - | 125 - } 126 - ~ 127 -
'''


@resource_usage_decorator
def show_symbols_1(symbol: int, counter: int = 1) -> None:
    if symbol < 128:
        print(f'{symbol} - {chr(symbol)} ', end='\n' if counter % 10 == 0 else '')
        show_symbols_1(symbol + 1, counter + 1)


@resource_usage_decorator
def show_symbols_2(symbol: int, counter: int = 1) -> None:
    while symbol < 128:
        print(f'{symbol} - {chr(symbol)} ', end='\n' if counter % 10 == 0 else '')
        symbol += 1
        counter += 1


# print(f'Usage memory = {show_symbols_1(31).memory}')
# print(f'Usage memory = {show_symbols_2(31).memory}')

'''
Usage memory = 0.41015625
Usage memory = 0.0
Оптимизация заключается в замене рекурсии циклом, тем самым уменьшаем использование памяти
'''