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
import timeit


def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1  # O(1)
    n = 2  # O(1)
    while count <= i:  # O(n)
        t = 1  # O(1)
        is_simple = True  # O(1)
        while t <= n:  # O(n)
            if n % t == 0 and t != 1 and t != n:  # O(1)
                is_simple = False  # O(1)
                break
            t += 1  # O(1)
        if is_simple:  # O(1)
            if count == i:  # O(1)
                break
            count += 1  # O(1)
        n += 1  # O(1)
    return n
# Общая сложность O(n^2)

def simple_2(simple_num):
    """С использованием «Решета Эратосфена»"""
    number = simple_num * 10    # O(1)
    numbers = list(range(number + 1))   # O(1)
    numbers[1] = 0  # O(1)
    i = 2   # O(1)
    while i <= number:  # O(n)
        if numbers[i] != 0:     # O(1)
            j = i + i           # O(1)
            while j <= number:      # O(log n)
                numbers[j] = 0      # O(1)
                j += i              # O(1)
        i += 1                      # O(1)
    a = set(numbers)                # O(len(numbers))
    a.remove(0)                     # O(1)
    a = sorted(list(a))             # O(n log n)
    return a[simple_num - 1]
# Общая сложность  O(n(log n))

print(timeit.timeit('simple(10)', globals=globals(), number=1))
print(timeit.timeit('simple(100)', globals=globals(), number=1))
print(timeit.timeit('simple(1000)', globals=globals(), number=1))

print(timeit.timeit('simple_2(10)', globals=globals(), number=1))
print(timeit.timeit('simple_2(100)', globals=globals(), number=1))
print(timeit.timeit('simple_2(1000)', globals=globals(), number=1))

# По резульатам измерения времени выяснилось, что алгоритм решета Эратосфена эффективен
# для поиска больших простых чисел, в то время как для небольших чисел он уступает первому алгоритму
# Времена замеров, соотвественно:
# 1.709999999999906e-05
# 0.0015311000000000005
# 0.2374514
# 2.7700000000019376e-05
# 0.00020580000000003373
# 0.0023695000000000244

# P.S. реализация алгоритма конечно несколько грубовата, с точки зрения чистой математики, ибо содержит не строгие
# выражения, допускающие некоторые сомнения.