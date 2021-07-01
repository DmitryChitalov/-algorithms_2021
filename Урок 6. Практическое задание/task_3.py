"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""

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


if __name__ == '__main__':
    start_size = memory_usage()
    print(guessing(random.randint(1, 100)))
    finish_size = memory_usage()[0] - start_size[0]
    print(f'{"-" * 30}\nЗатрачено памяти на выполнение функции guessing = {finish_size}')
    print(f'{"-" * 30}\nЗатрачено памяти на выполнение функции guessing = {size.pop()[0] - size.pop(0)[0]}')


"""
Взял пример из задания 1.
Профилировать рекурсия через memory_usage.profile ли через декоратор с отсечками начала и конца замеров не 
целесообразно, т.к. в течении каждого вызова функции будет вызвана эта же функция с этим же декоратором, что приведет
к выводу на экран информация по каждому вызову функции. Использовав сохранение каждого замера в список мы можем 
узнать корректные данные просто произведя вычитание первого элемента из последнего 
"""