"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

from timeit import default_timer
import memory_profiler


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        t1 = default_timer()
        func(*args, **kwargs)
        time_diff = default_timer() - t1
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        return f'Выполнение заняло: {mem_diff} MiB\nЗаняло времени: {time_diff}\n'

    return wrapper


@decor
def get_reverse_recurs(enter_num):
    return reverse_recurs(enter_num)


def reverse_recurs(enter_num, revers_num=''):
    if enter_num == 0:
        return print(f'Перевернутое число: {revers_num}')
    else:
        return reverse_recurs(enter_num // 10, revers_num + str(enter_num % 10))


num = 12345678905982370455820384028460284645294689234465330
print(f'Рекурсия:\n{get_reverse_recurs(num)}')

"""
Перевернутое число: 03356443298649254648206482048302855407328950987654321
Рекурсия:
Выполнение заняло: 0.07421875 MiB
Заняло времени: 0.00022069800000001916

Профилировку для скриптов с рекурсией надо делать через дополнительную функцию, вызывающую функцию с рекурсией, 
чтобы декоратор профилирования вызывался один раз, а не каждом рекурсисном вызове.
"""
