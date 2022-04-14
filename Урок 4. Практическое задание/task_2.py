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
'''
Анализ:
Надеюсь, я не ошибаюсь, но я пришла к такому выводу.
Мемоизация не требуется и все дело в самой функции memoize(f), а точнее - в обертке decorate(*args).
При обработке конструкции if/else переход на if - а равно и обращение
к содержимому кэша - почти не используется.
Выполняется условие else и кэш(cache) только наполняется, но почти не задействован.

Его задействование происходит в 2 случаях:
- при работе второй и третьей функций скрипта в первом действии рекурсии
(обращение к паре ключ-значение (0,): '', которые хранятся после работы первой функции скрипта)
- при ПОВТОРНОМ использовании функций с теми же числами в рамках одного и того же
запуска скрипта (в частности, при замерах timeit с количеством запусков больше 1):
    когда при первом же действии рекурсии происходит обращение к уже хранящейся
    с предыдущего запуска функции паре ключ-значение, равным:
    кортеж с полностью перевернутым числом (ключ) и само исходное число (значение).

Таким образом, наполнение кэша (cache) не имеет смысла, поскольку обращение к cache:
1. При первом использовании каждой функции в рамках одного запуска скрипта:
    а) для первой функции скрипта:
    - НЕ происходит вообще в количестве вызовов рекурсии, равных n+1;
    б) для последующих функций скрипта:
    - происходит при самом первом вызове рекурсии (т.е. единожды);
    - НЕ происходит в количестве последующих вызовов рекурсии, равных n;
2. При повторном использовании каждой функции с теми же числами в рамках одного запуска скрипта:
    - происходит в первом и единственном вызове рекурсии, тк значения уже хранятся в cache;
, где n - количество цифр в числе.

При этом происходит неоптимальное использование памяти, т.к. в cache до следующего запуска скрипта
хранятся все результаты вызовов каждой из 3 рекурсий, которые больше ни разу не пригождаются.

Также, timeit по-моему, тоже не имеет здесь информативной реализации.
Так как если он возвращает время, необходимое для выполнения основного выражения number количество
раз, то если number > 1, при выполнении выражения будет уже задействован cache.
Т.е. при первом выполнении (кэш еще пуст) будет результат почти равный скорости без оптимизации,
а последующие выполнения уже будут быстрее.
В таком случае оценка суммарной скорости будет не объективной, а зависимой от числа number.

Проверка предположения на практике:
Для 1 выполнения функции:
Не оптимизированная функция recursive_reverse
0.0000063540
0.0000053760
0.0000087969
Оптимизированная функция recursive_reverse_mem
0.0000087970
0.0000097749
0.0000156399
 - Очевидно, что оптимизированная функция даже уступает в скорости, тк приходится наполнять cache

Для 2 выполнений функции
Не оптимизированная функция recursive_reverse
0.00001075200
0.00000977399
0.00001710600
Оптимизированная функция recursive_reverse_mem
0.00001026300
0.00001075200
0.00001808300
 - Оптимизированная функция только сравнивается в скорости с неоптимизированной

Для 5 выполнений функции
0.00001906000
0.00001954900
0.00003616599
Оптимизированная функция recursive_reverse_mem
0.00001124100
0.00001123999
0.00001954900
 - Оптимизированная функция быстрее примерно вдвое

Для 100 выполнений функции:
Не оптимизированная функция recursive_reverse
0.0003083859
0.0003386880
0.0006162840
Оптимизированная функция recursive_reverse_mem
0.0000346999
0.0000342099
0.0000430079
 - Оптимизированная функция уже быстрее на 1 порядок за счет обращений к заполненному cache

Для 10000 выполнений функции:
Не оптимизированная функция recursive_reverse
0.0260022199
0.0296877080
0.0571248299
Оптимизированная функция recursive_reverse_mem
0.0025765680
0.0024988599
0.0023014140
 - С увеличением количества выполнений разница остается примерно той же(~ на 1 порядок)

Для 1_000_000 выполнений функции:
Не оптимизированная функция recursive_reverse
2.627715794
2.969794241
5.647595244
Оптимизированная функция recursive_reverse_mem
0.219794608
0.223615474
0.230320805
 - Соотношение, аналогичное 10000 выполнений.

Таким образом, данная мемоизация имеет смысл только в одном случае:
если в рамках одного запуска скрипта будет множество (от 10) выполнений
одной и той же рекурсивной функции с одним и тем же исходным числом.
Мне кажется, на практике встречается редко.
И даже в этом случае cache хранит в себе слишком много лишнего, на каждое число:
    - 2 используемых элемента cache
    - n-1 неиспользуемых, где n - количество цифр в числе.
    С каждым новым числом неиспользуемая область cache увеличивается на n-1 элементов.
Замеры же timeit здесь неинформативны из-за зависимости от числа выполнений функции.
'''


def recursive_reverse(number):
    if number == 0:
        return ''
    return f'{str(number % 10)}{recursive_reverse(number // 10)}'


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


def memoize(f):
    cache = {}

    def decorate(*args):
        if args in cache:
            return cache[args]
        cache[args] = f(*args)
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
