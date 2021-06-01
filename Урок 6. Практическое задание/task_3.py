"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

from memory_profiler import memory_usage
from random import randint


def mem_decorator(some_func):
    def wrapper(*args, **kwargs):
        result = some_func(*args, **kwargs)
        mem_list.append(str(memory_usage()))
        return result
    return wrapper



@mem_decorator
def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'



if __name__ == '__main__':
    mem_list = []
    num_10000 = randint(100000000, 10000000000000)
    print(f'Задействована память до запуска: '
          f'{str(memory_usage())} MB')
    recursive_reverse(num_10000)
    for i, mem in enumerate(list(reversed(mem_list)), 1):
        print(f'Задействована память после запуска: '
              f'{i} раз: {mem} MB')

