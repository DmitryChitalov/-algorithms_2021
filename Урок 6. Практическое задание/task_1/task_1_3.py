import random
from memory_profiler import memory_usage


time = []
size = []


def profiler(func):
    def wrapper(*args, **kwargs):
        size.append(memory_usage())
        res = func(*args)
        size.append(memory_usage())
        return res

    return wrapper


def profiler_loop(func):
    def wrapper(*args, **kwargs):
        start_size = memory_usage()
        res = func(*args)
        end_size = memory_usage()
        mem_dif = end_size[0] - start_size[0]
        print(f'Затрачено памяти на выполнение функции {func.__name__} {mem_dif} Mib')
        return res

    return wrapper


@profiler
def guessing(rand_num, attempts=1):
    print(f'Попытка номер {attempts}')
    user_num = int(input('Введите число от 0 до 100'))
    if user_num == rand_num:
        return f'Вы победили!!! Загаданное число: {rand_num}'
    elif attempts == 10:
        return f'У вас закончились попытки. Верное число: {rand_num}'
    else:
        if user_num > rand_num:
            print(f'Загаданное число меньше {user_num}')
            return guessing(rand_num, attempts + 1)
        else:
            print(f'Загаданное число больше {user_num}')
            return guessing(rand_num, attempts + 1)


@profiler_loop
def guessing_loop(rand_num, attempts=1):
    while attempts < 11:
        print(f'Попытка номер {attempts}')
        user_num = int(input('Введите число от 0 до 100'))
        if user_num == rand_num:
            return f'Вы победили!!! Загаданное число: {rand_num}'
        else:
            if user_num > rand_num:
                print(f'Загаданное число меньше {user_num}')
                attempts += 1
            else:
                print(f'Загаданное число больше {user_num}')
                attempts += 1
    return 'Вы проиграли'


if __name__ == '__main__':
    start_size = memory_usage()
    print(guessing(random.randint(1, 100)))
    finish_size = memory_usage()[0] - start_size[0]
    print(f'{"-" * 30}\nЗатрачено памяти на выполнение функции guessing = {finish_size}')
    print(f'{"-" * 30}\nЗатрачено памяти на выполнение функции guessing = {size.pop()[0] - size.pop(0)[0]}')

    # print(guessing_loop(random.randint(1, 100)))


"""
В результате замеров получили следующие данные:
Затрачено памяти на выполнение функции guessing = 0.08203125 (точки замеров в самом коде)
Затрачено памяти на выполнение функции guessing = 0.078125 (точки замеров в декораторе)
Затрачено памяти на выполнение функции guessing_loop 0.02734375 Mib
Из этих данных можно сделать вывод, что циклы занимают много меньше памяти, чем рекурсия за счет отсутствия 
стека вызовов
"""