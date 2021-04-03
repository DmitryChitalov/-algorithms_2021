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
Подумайте и по возможности определите сложность каждого алгоритма
Укажите формулу сложности О-нотация каждого алгоритма
и сделайте обоснвование рез-ам
"""
import timeit


# O(n) доминанта но так как это вложенные циклы то результатирующая сложность 0(n^2)
def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1                                     # 0(1)
    n = 2                                         # 0(1)
    while count <= i:                             # O(n)
        t = 1                                     # 0(1)
        is_simple = True                          # O(1)
        while t <= n:                             # O(n)
            if n % t == 0 and t != 1 and t != n:  # 0(1)
                is_simple = False                 # 0(1)
                break
            t += 1                                # 0(1)
        if is_simple:                             # 0(1)
            if count == i:                        # 0(1)
                break
            count += 1                            # 0(1)
        n += 1                                    # 0(1)
    return n                                      # 0(1)

# доминанта O(n log n)
def erastrofen(i):
    n = 2                                         # O(1)
    l = 10000                                     # O(1)
    sieve = [x for x in range(l)]                 # O(n log n)
    sieve[1] = 0                                  # O(1)
    while n < l:                                  # O(n)
        if sieve[n] != 0:                         # O(1)
            m = n * 2                             # O(1)
            while m < l:                          # O(n)
                sieve[m] = 0                      # O(1)
                m += n                            # O(1)
        n += 1                                    # O(1)
    return [p for p in sieve if p != 0][i - 1]    # O(n log n)

print("simple", simple(10))
print("simple time10", timeit.timeit("simple(10)", globals=globals(), number=1000))
print("erastrofen", erastrofen(10))
print("erastrofen time10", timeit.timeit("erastrofen(10)", globals=globals(), number=1000))

print("simple", simple(100))
print("simple time100", timeit.timeit("simple(100)", globals=globals(), number=1000))
print("erastrofen", erastrofen(100))
print("erastrofen time100", timeit.timeit("erastrofen(100)", globals=globals(), number=1000))

#print("simple", simple(1000))
#print("simple time100", timeit.timeit("simple(1000)", globals=globals(), number=1000))
print("erastrofen", erastrofen(1000))
print("erastrofen time1000", timeit.timeit("erastrofen(1000)", globals=globals(), number=1000))

"""
так и не понял что это за эрастрофен. и будет ли мое решение все еще
эрастрофеном если я внесу в него изменнения (потому что вариант по ссылке возвращает массив).
поэтому только для сравнения по времени использовал код эрастрофена из примера.

при порядковом номере числа 10 обычный код выполняется ~0.01 тогда как эрастрофен все ~2.29
при порядковом номере числа 100 обычный код выполняется ~1.36 тогда как эрастрофен все ~2.18
при порядковом номере числа 1000 обычный код выполняется ~214.75 тогда как эрастрофен все ~2.04

отсюда вывод у метода решения через эрастрофен постоянная величина времени на выполнение, но
эффективность по сравнению с первым способом достигается только при больших (близких 1000) значениях
При таких значениях решение выполняется значительно быстрее.
"""
