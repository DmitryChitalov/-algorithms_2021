from memory_profiler import profile


@profile
def simple_alg(i):
    """Перебор делителей"""
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


@profile
def eratosfen_alg(i):
    """Решето Эратосфена"""
    n = 2
    l = 10000
    sieve = [x for x in range(l)]
    sieve[1] = 0
    while n < l:
        if sieve[n] != 0:
            m = n*2
            while m < l:
                sieve[m] = 0
                m += n
        n += 1

    return [p for p in sieve if p != 0][i-1]


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple_alg(i))
print(eratosfen_alg(i))


""" 
Незначительный инкремент Решета обусловлен необходимостью генерации списка.
Величина инкремента может изменяться, в зависимости от объема списка.
При этом в целом инкремент находится в рамках нормы.
Оптимизация не требуется.
"""
