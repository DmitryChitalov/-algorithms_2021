"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
Если у вас есть идеи, предложите вариант оптимизации, если мемоизация не имеет смысла.
Без аналитики задание считается не принятым
"""

# функциия, оснащённая декоратором меморизации даёт значительное уменьшение времени только в случае подсчёта этого самого времени.
# Например, у нас есть какое-то число, проведя над ним операцию единожды, оно попадает в кэш,
# и если при вызове timeit у нас number > 1, то при повторном проведении операции, перевёрнутое число просто достаётся из кэша.
# Попробуем поставить number=1, и зададим не рандомное число, а какое-нибудь очень огромное, для того чтобы наглядно увидеть время (без экспоненты)
# Как мы видим, при одноразовом использовании каждой из фуекций, функция без меморизации показывает резульаты даже с меньшим временем

from timeit import timeit

def recursive_reverse(number):
    if number == 0:
        return str(number % 10)
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

print('Не оптимизированная функция recursive_reverse')
print(
    timeit(
        "recursive_reverse(10 ** 100)",
        globals=globals(),
        number=1))


def memoize(f):
    cache = {}

    def decorate(*args):

        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('"Оптимизированная" функция recursive_reverse_mem')

print(
    timeit(
        'recursive_reverse_mem(10 ** 100)',
        globals=globals(),
        number=1))


# Мой скромный вариант оптимизации. Не знаю, на сколько он хорош, но благодаря тому, что я ушла от рекурсии, я значительно уменьшила время выполнения.

print('My_func')


def my_func(number):
    n = -1
    my_str = ''
    str_list = [i for i in str(number)]
    for j in range(len(str_list)):
        my_str += str_list[n]
        n -= 1
    return my_str


print(
    timeit(
        'my_func(10 ** 100)',
        globals=globals(),
        number=1))