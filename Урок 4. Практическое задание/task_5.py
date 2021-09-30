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

def simple(i): # O(N^2)
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


# i = int(input('Введите порядковый номер искомого простого числа: '))
# print(simple(i))

def eratos(n):
    l = 15000
    num_list = list(range(l))
    num_list[1] = 0  # без этой строки итоговый список будет содержать единицу
    for i in num_list:
        if i > 1:
            for j in range(i + i, len(num_list), i):
                num_list[j] = 0

    return [j for j in num_list if j != 0][n - 1]

# print(eratos(i))

print(
    timeit(
        "simple(10)",
        globals=globals(),
        setup="from __main__ import simple",
        number=10),
    timeit(
        "simple(100)",
        globals=globals(),
        setup="from __main__ import simple",
        number=10),
    timeit(
        "simple(1000)",
        globals=globals(),
        setup="from __main__ import simple",
        number=10),
    timeit(
        "eratos(10)",
        globals=globals(),
        setup="from __main__ import eratos",
        number=10),
    timeit(
        "eratos(100)",
        globals=globals(),
        setup="from __main__ import eratos",
        number=10),
    timeit(
        "eratos(1000)",
        globals=globals(),
        setup="from __main__ import eratos",
        number=10), sep='\n'
)

"""
Первая функция быстрее работает только маленьких порядковых числах, но на больших она значительно проигрывает второй,
потому что у неё квадратичная сложность O(N^2), а у второй функции сложноть логарифмическая O(Nlog(logN)).
"""





"""
пытался ещё больше ускорить решение, но не хватило времени, потом обязательно вернусь к этому
"""
# def eratos_sieve(n: int, num_list: list,  p=2, count=2):
#     if p**2 > n:
#         return num_list
#
#     for i in range(count * p, n, p):
#         num_list.pop(i)
#         return eratos_sieve(n, num_list, p * count, count + 1)
#
# print(eratos_sieve(10, [i for i in range(2, 10)]))
