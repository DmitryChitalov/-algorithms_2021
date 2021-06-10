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

import math
import pickle as pickle
import json
from numpy import array
from random import randint
from pympler import asizeof
from memory_profiler import memory_usage
from timeit import default_timer

my_dict = {el: el for el in range(10, 2000) if (el % 20) == 0 or (el % 21) == 0}

my_dict1 = {el: el for el in range(10, 2000) if (el % 20) == 0 or (el % 21) == 0}
dumped_dict = json.dumps(my_dict1)
pickle_dict = pickle.dumps(my_dict1)

print(f'Memory dictionary:{asizeof.asizeof(my_dict)}')
print(f'Memory dictionary_dumped:{asizeof.asizeof(dumped_dict)}')
print(f'Memory dictionary_pickle:{asizeof.asizeof(pickle_dict)}')

'''
The dumps () method serializes to a string.
When using serialization, the size of the stored object is reduced several times, but this
the method is suitable only for storage, when using it, you need to decode the object using json.loads
Pickle supports text protocol by default, but it also has binary protocol,which is more efficient, 
takes up less memory, but is not human readable (useful when debugging).

Метод dumps() сериализует в строку. 
При использование сериализации, размер хранимого объекта уменьшается в несколько раз, но данный
способ подходит лишь для хранения, при использовании необходимо декодировать объект используя json.loads
Pickle поддерживает по умолчанию текстовый протокол, но имеет также двоичный протокол, 
который более эффективен, занимает меньше памяти, но не читается человеком (полезно при отладке).
'''



random_num = [el + randint(0, 10) for el in range(50000)]

random_num_array = array([el + randint(0, 10) for el in range(50000)])

random_num_map = list(map(int, [el + randint(0, 10) for el in range(50000)]))

print(f'Memory random number: {asizeof.asizeof(random_num)}')
print(f'Memory random number array: {asizeof.asizeof(random_num_array)}')
print(f'Memory random number map : {asizeof.asizeof(random_num_map)}')

'''
array uses 10 times less memory.
map has no effect.

array задействует в 10 раз меньше памяти.
map не оказывает влияния.
'''

''' Decorator for time and memory profiling**********Декоратор для профилирования времени и памяти'''


def memory_time_profiler(func):
    def wrapper(*args):
        memory = memory_usage()
        timer = default_timer()
        result = func(*args)
        memory = memory_usage()[0] - memory[0]
        timer = default_timer() - timer
        print(f'Lead time(Время выполнения): {timer}\nMemory used(Используемая память): {memory}')
        return result

    return wrapper


''' Finding the factorial of a number*********Нахождение факториала числа'''


def factorial_1(n):
    if n == 0:
        return 1
    return factorial_1(n - 1) * n


def factorial_2(n):
    factorial = 1
    for el in range(1, n + 1):
        factorial *= el
        yield factorial


@memory_time_profiler
def recurs_factorial(function, n):
    return function(n)


n = 400
recurs_factorial(factorial_1, n)
recurs_factorial(factorial_2, n)

''' 
Using a generator instead of recursion decreased memory usage
Execution time remains the same (for large values of n)

При использовании генератора, вместо рекурсии задействование памяти уменьшилось
Время выполнения остается прежним(при больших значениях n)
'''

''' 
Finding even and odd numbers in a string************Поиск четных и не четных чисел в строке
'''


def digit_counter(num, even, odd):
    if num == 0:
        return f'The number of even and odd digits in a number is equal to: ({even}, {odd})'
    elif num % 2 == 1:
        return digit_counter(num // 10, even, odd + 1)
    else:
        return digit_counter(num // 10, even + 1, odd)


def digit_counter_2(num, even, odd):
    for el in str(num):
        if (int(el) % 2) == 1:
            odd += 1
        else:
            even += 1
        return f'The number of even and odd digits in a number is*\n' \
               f'Количество четных и нечетных цифр в числе равно: ({even}, {odd})'


@memory_time_profiler
def recurs_digit_counter(func, num, even, odd):
    return func(num, even, odd)


num = math.factorial(222)
even = 0
odd = 0
recurs_digit_counter(digit_counter, num, even, odd)
recurs_digit_counter(digit_counter_2, num, even, odd)
print(f'Test number Factorial (222): {num}')
''' 
Using a generator instead of recursion decreased memory usage
Execution time remains the same (for large values of n)

При использовании генератора, вместо рекурсии задействование памяти уменьшилось
Время выполнения остается прежним (для больших значений n)
'''
'''
C:\Users\79115\AppData\Local\Programs\Python\Python39\python.exe "C:/Users/79115/Desktop/2 Урок Алгоритмы/Урок 2. Коды примеров/AlgorithmMy6.1.py"
Memory dictionary:15392
Memory dictionary_dumped:2512
Memory dictionary_pickle:1144
Memory random number: 2041656
Memory random number array: 200120
Memory random number map : 2041560
Lead time(Время выполнения): 0.10924479999999992
Memory used(Используемая память): 0.2421875
Lead time(Время выполнения): 0.10991410000000001
Memory used(Используемая память): 0.0
Lead time(Время выполнения): 0.10909229999999992
Memory used(Используемая память): 0.01953125
Lead time(Время выполнения): 0.10940749999999988
Memory used(Используемая память): 0.0
Test number Factorial (222): 11205075580064413918282465787428850331618234483620107256641806644257517065448960498845547308589123
31527222551582158208355091185677704255556649499546150835003041294501592836203788950087902880253311400664495648264845
086575793159256069174809550137801963923701418514184652520492639441452609118711474453282037451685103688549156372800995
882648661943229479756605490957651656939929600000000000000000000000000000000000000000000000000000

Process finished with exit code 0

'''
