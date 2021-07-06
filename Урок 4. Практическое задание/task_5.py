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
from timeit import timeit

'''Задачу 5, раз она не обязательная, я решала из интереса, поэтому не совсем в том векторе, который
был задан. Требовалось найти решение и разобрать его, а мне хотелось попробовать отработать рекурсию
и поучиться создавать мемоизацию. Поэтому мое решение ограничено глубиной рекурсии и неспособно
показать простые числа ряда, чей порядковый номер более 94.
Мне кажется, что изначальное решение имеет O(n^2), а мое - вероятно, O(n).

В любом случае, в timeit при большом количестве выполнений мемоизация позволила
неплохо оптимизировать скорость. Также мемоизация позволяет:
    а) если запрашиваемый порядковый номер больше предыдущих запрошенных порядковых номеров -
       начинать расчет новых чисел не с первого простого числа, а с последнего из рассчитанных
       ранее;
    б) если запрашиваемый порядковый номер уже соответствует числу ряда, рассчитанного ранее,
       результат выдается без выполнения новых расчетов.
Статью, а также решения других людей(более рациональные, чем мое), я тоже изучила, но уже не стала
сюда их переносить и разбирать.
'''


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


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))


def memoize(f):
    """Function stores previously calculated prime numbers"""
    cache = []

    def decorate(*args):
        if args[2] <= len(cache):
            return cache[args[2] - 1]

        if len(args[1]) > len(cache):
            cache.clear()
            cache.extend(args[1])
        elif len(args[1]) < len(cache):
            args = (args[1][-1], cache, args[2])
        res = f(*args)
        return res
    return decorate


@memoize
def check(checked_num, storage_list, ordinal_num, flag=0):
    """Function checks is number prime or not"""
    for elem in storage_list:
        if not checked_num % elem:
            flag = 1
    if flag == 0:
        storage_list.append(checked_num)
    return check(checked_num + 1, storage_list, ordinal_num)


def eratosthenes(my_ordinal_num):
    """My recursive solution of the Eratosthenes sieve"""
    my_storage_list = [2, ]
    my_start_num = 3
    return check(my_start_num, my_storage_list, my_ordinal_num)


i = int(input('Введите порядковый номер искомого простого числа: '))
print(eratosthenes(i))

# print(eratosthenes(10))
# print(eratosthenes(12))
# print(eratosthenes(10))
# print(eratosthenes(4))

print(f"simple:"
      f"{timeit('simple(10)', number=1, globals=globals()):.5f}")
print(f"eratosthenes:"
      f"{timeit('eratosthenes(10)', number=1, globals=globals()):.5f}")

print(f"simple:"
      f"{timeit('simple(10)', number=10, globals=globals()):.5f}")
print(f"eratosthenes:"
      f"{timeit('eratosthenes(10)', number=10, globals=globals()):.5f}")

print(f"simple:"
      f"{timeit('simple(94)', number=100, globals=globals()):.5f}")
print(f"eratosthenes:"
      f"{timeit('eratosthenes(94)', number=100, globals=globals()):.5f}")
