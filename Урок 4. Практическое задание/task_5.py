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

i, i1, i2 = 10, 100, 1000


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


def sieve_erato(i):
    n = 2
    l = i * 10
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n * 2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1
    return [p for p in sieve if p != 0][i - 1]


print('simple(i)', timeit("simple(i)",globals=globals(),number=100))
# среднее 0.0010342
print('simple(i1)',timeit("simple(i1)",globals=globals(),number=100))
# среднее 0.1298148
print('simple(i2)',timeit("simple(i2)",globals=globals(),number=100))
#  среднее 19.455589
print(simple(i))
print(simple(i1))
print(simple(i2))
print()

print('sieve_erato(i)', timeit("sieve_erato(i)",globals=globals(),number=100))
# среднее 0.0013938
print('sieve_erato(i1)',timeit("sieve_erato(i1)",globals=globals(),number=100))
# среднее 0.016935
print('sieve_erato(i2)',timeit("sieve_erato(i2)",globals=globals(),number=100))
# среднее 0.1894808
print(sieve_erato(i))
print(sieve_erato(i1))
print(sieve_erato(i2))

"""
Первая функция справляется с выполнением задачи на небольших числах, быстрее, чем вторая. Однако на больших
числах, вторая функция справляется гораздо быстрее.
Сложность первой функции квадратичная O(n^2).
Сложность второй функции O(n log(log n)).
Время выполнения у первой функции гораздо дольше, из-за того что каждое раз для числа (n) она начинает проверку на 
делимость с 1 (t), и при каждом следующем цикле увеличивает всего на 1, проверяя потенциальное простое число на 
делимость всех предшествующих чисел. Эта проверка излишняя, так как если оно не разделось на 2, то значит не разделится 
и на все последующие четные числа, если не разделилось на три, то не разделится на 6, 9, и тд.
Во второй функции, по алгоритму Эратосфена, после проверки минимального делителя, все последующие числа, которые делятся
на это число, заменяются нулями. Благодоря этому, числе для проверки остается все меньше и меньше, и поиск для больших
чисел проходит намного быстрее.
Однако существенным минусом алгоритма Эратосфена является то, что нам необходимо знать предел, в котором находится 
число.
"""
