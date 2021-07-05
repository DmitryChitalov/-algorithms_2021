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


def simple(i):
    #Без использования «Решета Эратосфена»
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


def eratosthenes(n):
    # Среди чисел, меньших 4, не будет вычеркнутых.
    if n < 4:
        return

    # Создание и заполнение списка чисел из интервала [0; n].
    a = [i for i in range(n + 1)]
    # Число 1 не является простым числом.
    # Все числа, не являющиеся простыми, будем вычеркивать (заменять нулём).
    a[1] = 0
    # Список вычеркнутых чисел пока пуст.
    b = []

    # Перебор всех чисел от 2 до n.
    for i in range(2, n + 1):
        # Перебрать все кратные ему числа <= n.
        for j in range(i * 2, n + 1, i):
            # Если число еще не вычеркнуто.
            if a[j] != 0:
                # Вычеркнуть это число.
                a[j] = 0
                # Поместить в список вычеркнутых.
                b.append(j)

    # Вывести составные числа в порядке их вычеркивания.
    print(" ".join(str(x) for x in b))


eratosthenes(int(input('Максимальное число n = ')))

(lambda x:  [[[x.remove(elem), print(elem)]  for elem in x if elem % i == 0 and elem != i] for i in x])  ([i for i in range(2, int(input()) + 1)])

def primes_sieve2(limit):
    a = [True] * limit               # Initialize the primality list
    a[0] = a[1] = False
    sqrt = int(math.sqrt(limit))+1
    for i in xrange(sqrt):
        isprime = a[i]
        if isprime:
            yield i
            for n in xrange(i*i, limit, i):     # Mark factors non-prime
                a[n] = False
    for (i, isprime) in enumerate(a[sqrt:]):
        if isprime:
            yield i+sqrt