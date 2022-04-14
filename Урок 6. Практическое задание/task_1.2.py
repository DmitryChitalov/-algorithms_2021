from memory_profiler import profile


@profile
def wrapper(n):
    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n - 1)

    print(factorial(n))


wrapper(100)


@profile
def factorial_2(n):
    res = 1
    while (n > 0):
        res = res * n
        n = n - 1
    print(res)


factorial_2(100)

"""
Здесь разница тоже не очень заметна, однако функция с циклом все равно менее затратна по ресурсам памяти,
чем рекурсивная функция
"""