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


def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'

def num_10000():
    return randint(100000000, 10000000000000)


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
# num_10000 = randint(100000000, 10000000000000)

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
print('вх.параметр генерится при каждом вызове: ',
    timeit(
        "recursive_reverse(num_10000())",
        setup='from __main__ import recursive_reverse, num_10000',
        number=10000))


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


def reverse_for(number):
    in_str = str(number)
    out_str = ''
    for i in range(len(in_str)-1,-1,-1):
        out_str += in_str[i]
    return out_str

def reverse_integrated(number):
    return reversed(str(number))

# n = 1234567890
# print(n, reverse_for(n))
# exit()

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
print('вх.параметр генерится при каждом вызове: ',
    timeit(
        'recursive_reverse_mem(num_10000())',
        setup='from __main__ import recursive_reverse_mem, num_10000',
        number=10000))

func_list = ['recursive_reverse', 'recursive_reverse_mem', 'reverse_for', 'reverse_integrated']
print('Теперь сравним варианты :')
for el in func_list:
    print(f'Функция {el}:', timeit(el+'(num_10000())', number=10000, globals=globals()))



'''
Запуск "как есть"
Не оптимизированная функция recursive_reverse
0.053577714
0.06022617599999999
0.09217042800000003
Оптимизированная функция recursive_reverse_mem
0.003592898000000011
0.0036067840000000295
0.0037577209999999917

Результаты настораживают. В случае кэширования, при изменении "работы" в 10-100 раз, результат практически не меняется.
Сделаем предположение, что входной параметр (num_100..) функции остается прежним все 10000 раз запусков.
Сделаем его принудительно-обновляемым (завернем в пользовательскую функцию - 'num_10000()'):

Не оптимизированная функция recursive_reverse
0.04855514300000002
0.058233810999999996
вх.параметр генерится при каждом вызове:  0.113600427
Оптимизированная функция recursive_reverse_mem
0.003647235999999998
0.003517429999999988
вх.параметр генерится при каждом вызове:  0.18852120000000006

Вот, теперь уже больше похоже на отсутствие примуществ кэширования рекурсии (последняя строка).
Мы на кэширование тратим больше ресурсов, нежели на выгоду от их использования при  
Ответ:
        КЭШирование при реализации такой рекурсии не дает преимуществ по скорости.
        
Добавим пару вариантов функций:
- reverse_for (переворачивает число в простом цикле)
- reverse_integrated (переворачивает число при помощи встроенной функции reversed)

Результат вполен прогнозируемый (встроенная функция самая "быстрая", потом уже обычный перебор,...):
Функция recursive_reverse: 0.113733855
Функция recursive_reverse_mem: 0.18921550899999995
Функция reverse_for: 0.05399973300000005
Функция reverse_integrated: 0.024709552000000023
'''