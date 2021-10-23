import memory_profiler
from timeit import default_timer
import sys
from pympler import asizeof
from numpy import array


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        start_time = default_timer()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        mem_diff = m2[0] - m1[0]
        print(f'Выполнение заняло: {m2[0] - m1[0]}, Заняло времени: {default_timer() - start_time}')
        return res
    return wrapper


# Задание с курса 'Основы языка Python'
# Создать список, состоящий из кубов нечётных чисел от 0 до 1000:
# Вычислить сумму тех чисел из этого списка, сумма цифр которых делится нацело на 7.
# Например, число «19 ^ 3 = 6859» будем включать в сумму, так как 6 + 8 + 5 + 9 = 28 – делится нацело на 7

@decor
def firs_version(n):
    my_list = []
    full_summ = 0
    for i in range(1, n+1, 2):
        my_list.append(i ** 3)
    for i in my_list:
        num = i
        sum_num = 0
        while num > 0:
            sum_num += num % 10
            num //= 10
        if sum_num % 7 == 0:
            full_summ += i
    print(full_summ)


def nums_generator(max_num):
    for i in range(1, max_num + 1, 2):
        num = i ** 3
        sum_num = 0
        while num > 0:
            sum_num += num % 10
            num //= 10
        yield i ** 3 if sum_num % 7 == 0 else 0


@decor
def new_version(n):
    nums_gen = nums_generator(n)
    full_summ = 0

    for _ in range(1, n+1, 2):
        num = next(nums_gen)
        full_summ += num
    print(full_summ)


firs_version(1000)  # Выполнение заняло: 0.00390625, Заняло времени: 0.1120061
new_version(1000)  # Выполнение заняло: 0.0, Заняло времени: 0.1119021
print()

# Вывод
# Для оптимизации я воспользовалась генератором. В данном случае, использование
# генератора помогло существенно сократить время выполнения операций


# Урок 2. Практическое задание
# Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, то у него 3 четные цифры
# (4, 6 и 0) и 2 нечетные (3 и 5).

def count_numbers_version_1(number, even=0, odd=0):
    if number == 0:
        return even, odd
    else:
        if number % 10 % 2 == 0:
            even += 1
        else:
            odd += 1
        return count_numbers_version_1(number // 10, even, odd)


@decor
def main_f(num):
    print(f'Четных и нечетных чисел: {count_numbers_version_1(num)}')

@decor
def count_numbers_version_2(number, even=0, odd=0):
    while number > 0:
        if number % 10 % 2 == 0:
            even += 1
        else:
            odd += 1
        number //= 10
    return even, odd


main_f(66555230)
print(f'Четных и нечетных чисел: {count_numbers_version_1(6655523002)}')

# Вывод
#  Выполнение заняло: 0.00390625, Заняло времени: 0.11180849999999998
#  memory: Выполнение заняло: 0.0, Заняло времени: 0.10984040000000017
# Вывод: Отказ от рекурсии позволяет сэкономить память
print()

# Урок 4. Практическое задание
# Задание 1.
# Приведен код, который позволяет сохранить в
# массиве индексы четных элементов другого массива

@decor
def save_even_elm_ver_1(element):
    return [i for i in range(0, len(element), 2)]


@decor
def save_even_elm_ver_2(element):
    return array([i for i in range(0, len(element), 2)])


element = [num**2 for num in range(1000000)]

save_even_elm_ver_1(element)        # memory: 19.3828125, time: 0.12074570000000007
save_even_elm_ver_2(element)        # memory: 1.96875, time: 0.17786880000000016

# Вывод
# При использовании модуля numpy сразу видно экономию памяти и небольшой ущерб по времени.

