"""
Задание 2.

Приведен код, который формирует из введенного числа
обратное по порядку входящих в него цифр.
Задача решена через рекурсию
Выполнена попытка оптимизировать решение через мемоизацию.
Сделаны замеры обеих реализаций.

Сделайте аналитику, нужна ли здесь мемоизация или нет и почему?!!!
Будьте внимательны, задание хитрое. Не все так просто, как кажется.
"""

from timeit import timeit
from random import randint


def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


num_100 = randint(10000, 1000000)
num_1000 = randint(1000000, 10000000)
num_10000 = randint(100000000, 10000000000000)
num_lst = [num_100, num_1000, num_10000]

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


def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            # print(cache[args])
            return cache[args]
        else:
            cache[args] = f(*args)
            # print(cache[hash(args)])
            # print(cache)
            return cache[args]
    return decorate


@memoize
def recursive_reverse_mem(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


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


"""
Показатели времени работы кода по его исполнению следующие: 
Не оптимизированная функция recursive_reverse
0.0167157
0.0184379
0.0443457
Оптимизированная функция recursive_reverse_mem
0.0015645999999999993
0.0015290999999999916
0.0016195000000000098
из показателей видно, что оптимизированная функция работает на порядок быстрее.

Выведем каждое число и результат работы каждой функции
"""

print('\n Выведем каждое число и результат работы каждой функции \n'
      'Не оптимизирована \n')
for el in num_lst:
    print(el)
    print(recursive_reverse(el))
    print('-' * 20)
print('=' * 20, '\n'
      'Оптимизирована \n')
for el in num_lst:
    print(el)
    print(recursive_reverse_mem(el))
    print('-' * 20)

"""
846195
591648
--------------------
8810363
3630188
--------------------
3994008682167
7612868004993
--------------------
==================== 
Оптимизирована 

846195
591648
--------------------
8810363
3630188
--------------------
3994008682167
7612868004993
--------------------

Обе функции работают верно.
Если добавить в функцию мемоизации вывод результата (новых вносимых значений), то видно, 
что словарь фиксирует всю последовательность операций и записывает число для каждой итерации каждой функции по отдельности.
Аргументом для записи становится перевернутое число, а ключем - исходное. В кэше представлены записи вида:
{(0,): '', (7,): '7', (75,): '57', (757,): '757', (7575,): '5757', (75750,): '05757', (757509,): '905757'}.
Результат работы функции: 905757.
Исходное число: 757509

Из особенностей этого кода: 
1. В ключах кэша представлены не хеш объекты, однако это не означает замедления работы. Наоборот, 
принудительное создание хеша ведет к замедлению на 0.0001 (Cм. memoized(func))
2. Судя по тому, как формируется словарь кэша, на Каждом применении функция будет отбирать дополнительный объем 
оперативной  памяти в количестве, пропорциональном числу разрядов переворачиваемого числа, что может вести к быстрому
наполнению кэша.
3. Судя по порядку и последовательности записи {(0,): ''} - сначала - в финале {(495011,): '110594'} 
- кэшируются все данные, число которых растет в соответствии с количеством разрядов числа, а также числом запуска функции. 
При этом, учитывая, что запись в словарь осуществляется от нуля до полного числа, можно сказать, что 
СНАЧАЛА рекурсия доходит до общего случая, а потом происходит запись результатов в словарь.
Оттуда происходит возврат значений, к которым присоединяются новые результаты работы функции. 
4. Число, возвращаемое из словаря, возвращается и для использования функцией, и вывода результата, 
в связи с чем мемоизация и рекурсивная функция должны рассматриваться как единое целове.

Вывод: Мне не нравится рекурсия в принципе. Часто это слишком "умный" код, на понимание которого тратится больше 
времени, чем оно того стоит (с точки зрения затрат ресурсов "железа" / реального времени на поиск ошибки, например), 
велика вероятность ошибки, высокий риск потер по ресурсам оперативной памяти. Мой первый порыв переписать рекурсию. 
(Например, recursive_reverse_2(num) дает следующие параметры:
Оптимизированная функция recursive_reverse_2
0.004099400000000003
0.004430099999999992
0.005149399999999998)

По существу вопроса: мемоизация существенно ускоряет реализацию кода за счет скорости доступа к словарю в памяти. 
При этом рекурсия осуществляет свою работу в полном объеме и если от приведенного кода некуда деться, то пусть так и будет.
Однако, с точки зрения работы приведенного кода, он может рассматриваться как небезопасный для ресурсов оперативной памяти.
Если предполагается ограниченное число итераций базовой функции, то можно так оставить. 
Если таких итераций предполагается много, то можно ожидать переполнения кэша и мемоизация здесь будет избыточна и вредна.

Мемоизацию хорошо использовать для повторяющихся значений
"""


def memoized(func):
    cache = {}

    def decorate(args):
        num = args
        args = hash(args)
        if args in cache:
            # print(cache[args])
            return cache[args]
        else:
            cache[args] = func(num)
            # print(cache[hash(args)])
            # print(cache)
            return cache[args]
    return decorate


@memoized
def recursive_reverse_mem_1(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse_mem(number // 10)}'


print('Оптимизированная функция recursive_reverse_mem_1')
print(
    timeit(
        'recursive_reverse_mem_1(num_100)',
        setup='from __main__ import recursive_reverse_mem_1, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem_1(num_1000)',
        setup='from __main__ import recursive_reverse_mem_1, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_mem_1(num_10000)',
        setup='from __main__ import recursive_reverse_mem_1, num_10000',
        number=10000))


def recursive_reverse_2(num):
    string_lst = list(str(num))
    string_lst.reverse()
    return ''.join(string_lst)


print('Оптимизированная функция recursive_reverse_2')
print(
    timeit(
        'recursive_reverse_2(num_100)',
        setup='from __main__ import recursive_reverse_2, num_100',
        number=10000))
print(
    timeit(
        'recursive_reverse_2(num_1000)',
        setup='from __main__ import recursive_reverse_2, num_1000',
        number=10000))
print(
    timeit(
        'recursive_reverse_2(num_10000)',
        setup='from __main__ import recursive_reverse_2, num_10000',
        number=10000))
