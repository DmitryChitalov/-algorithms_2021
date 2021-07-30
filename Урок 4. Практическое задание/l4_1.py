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
from time import time as time


def timer(func):
    def temporary(*args, **kwargs):
        start_time = time()
        result = func(*args, **kwargs)
        delta_time = time() - start_time
        print(f'функция «{str(func.__name__).capitalize()}» вернула результат — {result} за {delta_time} сек.')
        return result

    return temporary


@timer
def simple(i):  # O(n^2)
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i:  # O(n)
        t = 1
        is_simple = True
        while t <= n:  # O(n)
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


@timer
def eratosthenes(x):  # O(n^2)

    if x <= 10:
        n = 29
    elif x <= 100:
        n = 541
    elif x <= 1000:
        n = 7919
    elif x > 1000:
        n = 104743
        print(f'Для безопасной работы компьютера максимально отображаемым числом возможно 10000-ое в списке простых!')

    a = [k for k in range(n + 1)]
    a[1] = 0
    i = 2

    while i <= n:  # O(n)

        if a[i] != 0:
            j = i + i

            while j <= n:
                a[j] = 0
                j = j + i
        i += 1

    while 0 in a:  # O(n^2)
        a.remove(0)

    return a[x-1]


@timer
def eratosthenes2(q):  # O(n)

    simple_nums = {2}
    n = 3

    while len(simple_nums) < q:  # O(n)

        p = 1

        for num in simple_nums:
            if n % num == 0:
                p = None
                break

        if p:
            simple_nums.add(n)
        n += 1

    return max(simple_nums)  # O(n)


for elem in [10, 100, 1000, 5000]:
    print(f'Для {elem}-ого простого числа:')
    simple(elem)  # 0.0005006790161132812, 0.00250244140625, 0.4158945083618164, 12.801678657531738
    eratosthenes(elem)  # 10-5, 0.0010006427764892578, 0.12361741065979004, 18.718789100646973
    eratosthenes2(elem)  # 10-5, 0.0005009174346923828, 0.038537025451660156, 0.9779298305511475
    print()

'''Самым быстрым является третий способ при выводе резудьтата для любого числа за счёт работы со множеством
и отсутвием лишнего перебора в цикле. Второй способ быстрее первого, но медленнее третьего, может выполняться дольше
первого в случаях, когда числа больше 1000 ближе к самой 1000, так как алгоритм второй функции  предполагает 
заполнение и дальнейший перебор списка до 10000 числа включительно.'''