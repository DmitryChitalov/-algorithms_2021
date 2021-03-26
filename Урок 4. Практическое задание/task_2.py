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

from timeit import timeit
from random import randint


def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        else:
            cache[args] = f(*args)
            return cache[args]

    return decorate


def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


if __name__ == '__main__':

    str_label = "=" * 20
    print(f'{str_label} Исходные данные {str_label}')

    num_100 = randint(10000, 1000000)
    num_1000 = randint(1000000, 10000000)
    num_10000 = randint(100000000, 10000000000000)

    print('Не оптимизированная функция recursive_reverse')
    print(
        timeit(
            "recursive_reverse(num_100)",
            setup='from __main__ import recursive_reverse, num_100',
            number=10000))
    print(
        timeit(
            "recursive_reverse(num_1000)",
            setup='from __main__ import recursive_reverse, num_1000',
            number=10000))
    print(
        timeit(
            "recursive_reverse(num_10000)",
            setup='from __main__ import recursive_reverse, num_10000',
            number=10000))

    print('Оптимизированная функция recursive_reverse_mem')
    print(
        timeit(
            'recursive_reverse_mem(num_100)',
            setup='from __main__ import recursive_reverse_mem, num_100',
            number=10000))
    print(
        timeit(
            'recursive_reverse_mem(num_1000)',
            setup='from __main__ import recursive_reverse_mem, num_1000',
            number=10000))
    print(
        timeit(
            'recursive_reverse_mem(num_10000)',
            setup='from __main__ import recursive_reverse_mem, num_10000',
            number=10000))

    print(f'{str_label} Аналитика {str_label}')  # ===============================
    num = randint(100000000, 10000000000000)
    quantity = [1, 2, 100, 1000, 10000]

    for i in quantity:
        print(f'Количество замеров: {i}')
        print(f"Обычная функция         : "
              f"{timeit('recursive_reverse(num)', setup='from __main__ import recursive_reverse, num', number=i)}")
        print(f"Оптимизированная функция: "
              f"{timeit('recursive_reverse_mem(num)', setup='from __main__ import recursive_reverse_mem, num', number=i)}")
        print('-' * 50)

"""
Из результата анализа замеров количества выполнения обычной и оптимизированной функции видно,
что необходимость оптимизации присутствует только если функция будет применяться неоднократно.
При единичном выполнении обычная функция показывает более лучшие результаты чем мемоизированная.

Данное происходит из-за того что при первом выполнении происходит сначала наполнение кэша, 
и только после - возвращение требуемого значения, а при повторном выполнении требуемое значение 
берется непосредственно из кэша.
"""

