from timeit import timeit


def simple_def(i):
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


def sieve(serial_num, arr=[2]):
    counter = 2
    num = 2
    while counter <= serial_num:
        is_simple = True
        for simple in range(len(arr)):
            if num % arr[simple] == 0:
                is_simple = False
        if is_simple:
            arr.append(num)
            counter += 1
        num += 1

    return f'Простое число с порядковым номером {serial_num} : {arr[-1]} '


# print(simple_def(i=int(input('Введите порядковый номер искомого простого числа: '))))
# print(timeit('simple(user_num)', globals=globals(), number=10000))
print(sieve(serial_num=int(input('Порядковый номер простого числа: '))))
