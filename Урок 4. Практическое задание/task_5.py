"""
Задание 5.**

Приведен наивный алгоритм нахождения i-го по счёту
простого числа (через перебор делителей).

Попробуйте решить эту же задачу,
применив алгоритм "Решето Эратосфена" (https://younglinux.info/algorithm/sieve)

Подсказка:
Сравните алгоритмы по времени на разных порядковых номерах чисел:
10, 100, 1000

Опишите результаты, сделайте выводы, где и какой алгоритм эффективнее
Подумайте и по возможности определите сложность каждого алгоритма.

Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснование результатам.
"""
# Перебор чисел подряд неудобен и медленный, вероятно все найденные простые числа надо закидывать в кэш и
# потом использовать. Не понятно, как выбирать диапазон для поиска следующего простого числа, зная предыдущее.
# Чисто гипотетически можно ходить шагом равным последнему простому числу. Взял пример с просеиванием чисел до n
# получилось медленнее, чем простым наивным перебором. Наверное из-за реккурсии. Добавил мемоизацию. Все равно
# медленнее. В общем надо еще думать, но сам корявый алгоритм придумал быстро, результат соответствующий))).
from timeit import timeit
from cProfile import run


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:
        t = 1
        is_simple = True
        while t <= n:
            if n % t == 0 and t != 1 and t != n:
                is_simple = False
                break
            t += 1
        if is_simple:
            if count == i:
                break
            count += 1
        n += 1
    return n


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
def get_simple(n):
    if n == 1:
        return 2
    elif n == 2:
        return 3
    else:
        x = n + 2
        while not gen_prime(x).get(n):
            x += get_simple(n-1)
    return gen_prime(x).get(n)


@memoize
def gen_prime(x):
    multiples = []
    results = {}
    k = 1
    for i in range(2, x+1):
        if i not in multiples:
            results[k] = i
            k += 1
            for j in range(i*i, x+1, i):
                multiples.append(j)

    return results


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
print(get_simple(i))

print(timeit("simple(500)", globals=globals(), number=10))
print(timeit("get_simple(500)", globals=globals(), number=10))

run('simple(500)')
run('get_simple(500)')
