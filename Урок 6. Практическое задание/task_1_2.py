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

from memory_profiler import profile


# Вывести на экран коды и символы таблицы ASCII, начиная с символа
# под номером 32 и заканчивая 127-м включительно.
# Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

# решение с рекурсией до оптимизации

@profile
def output_ascii(start_char, end_char):
    if (start_char - 32 + 1) % 10 == 0:
        print("%d - %s" % (start_char, chr(start_char)))
    else:
        print("%d - %s" % (start_char, chr(start_char)), end=' ')
    if start_char == end_char:
        return
    else:
        output_ascii(start_char + 1, end_char)


output_ascii(32, 127)


# решение с циклом после оптимизации

@profile
def output_ascii2(start_char, end_char):
    while start_char < end_char:
        if (start_char - 32 + 1) % 10 == 0:
            print("%d - %s" % (start_char, chr(start_char)))
        else:
            print("%d - %s" % (start_char, chr(start_char)), end=' ')
        start_char += 1


output_ascii2(32, 127)

"""

Ниже приведены замеры для одного вызова с рекурсией и для варианта с циклом
Хотя в рамках одной рекурсии объем занимаемой памяти на 0.1 MiB меньше, за счет
формирования стека вызовов использование памяти увеличивается многократно.

Вывод - вариант с циклом предпочтительнее с точки зрения использования памяти.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    34     16.4 MiB     16.4 MiB           1   @profile
    35                                         def output_ascii(start_char, end_char):
    36     16.4 MiB      0.0 MiB           1       if (start_char - 32 + 1) % 10 == 0:
    37                                                 print("%d - %s" % (start_char, chr(start_char)))
    38                                             else:
    39     16.4 MiB      0.0 MiB           1           print("%d - %s" % (start_char, chr(start_char)), end=' ')
    40     16.4 MiB      0.0 MiB           1       if start_char == end_char:
    41     16.4 MiB      0.0 MiB           1           return
    42                                             else:
    43                                                 output_ascii(start_char + 1, end_char)
    
    

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    51     16.5 MiB     16.5 MiB           1   @profile
    52                                         def output_ascii2(start_char, end_char):
    53     16.5 MiB      0.0 MiB          96       while start_char < end_char:
    54     16.5 MiB      0.0 MiB          95           if (start_char - 32 + 1) % 10 == 0:
    55     16.5 MiB      0.0 MiB           9               print("%d - %s" % (start_char, chr(start_char)))
    56                                                 else:
    57     16.5 MiB      0.0 MiB          86               print("%d - %s" % (start_char, chr(start_char)), end=' ')
    58     16.5 MiB      0.0 MiB          95           start_char += 1

"""
