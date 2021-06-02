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

def simple(i):
    """Без использования «Решета Эратосфена»
    сложность алгоритма -  O(n^2)

    """
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


# Решето Эратосфена
def sieve(n):
    """сложность алгоритма -  O(n log(log n))"""

    list_of_nums_border = 10000
    list_of_nums = []
    for el in range(list_of_nums_border + 1):
        list_of_nums.append(el)
    list_of_nums[1] = 0
    i = 2
    while i <= list_of_nums_border:
        if list_of_nums[i] != 0:
            j = i + i
            while j  <= list_of_nums_border:
                list_of_nums[j] = 0
                j = j + i
        i += 1
    return [el for el in list_of_nums if el != 0][n-1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(f'Простое число, найденное функцией simple - {simple(i)}')
print(f'Простое число, найденное функцией sieve - {sieve(i)}')
print()
print(f'Профилирование фнукции simple: время выполнения - {timeit("simple(i)", globals=globals(), number=100)} секунды.')
print('======================================================================')
print(f'Профилирование фнукции sieve: время выполнения - {timeit("sieve(i)", globals=globals(), number=100)} секунды.')


"""

Выводы:
Решето Эратосфена показывает стабильную скорость,
независимо от величины порядкового номера искомого простого числа.
Тогда как простая функция теряет в скорости, особенно на больших порядковых номерах.


При порядковом номере 10:
Профилирование фнукции simple: время выполнения - 0.0024049999999999905 секунды.
======================================================================
Профилирование фнукции sieve: время выполнения - 0.336856995 секунды.

При порядковом номере 100:
Профилирование фнукции simple: время выполнения - 0.19364785699999998 секунды.
======================================================================
Профилирование фнукции sieve: время выполнения - 0.33528286900000004 секунды.

При порядковом номере 1000:
Профилирование фнукции simple: время выполнения - 31.884409146999996 секунды.
======================================================================
Профилирование фнукции sieve: время выполнения - 0.3272758499999995 секунды.

"""

