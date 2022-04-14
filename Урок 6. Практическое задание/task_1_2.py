from task_1_1 import memory_time_profiler


@memory_time_profiler
def req_even_odd(num):
    print('Рекурсия')

    def even_odd(num, even=0, odd=0):
        if num == 0:
            return f'Количество четных и нечетных цифр в числе равно: {even, odd}'
        elif num % 2:
            return even_odd(num//10, even, odd+1)
        else:
            return even_odd(num//10, even+1, odd)
    return even_odd


@memory_time_profiler
def even_odd_loop(num):
    print('Цикл')
    even, odd = 0, 0
    while num != 0:
        last = num % 10
        if last % 2:
            odd += 1
        else:
            even += 1
        num = num // 10
    return even, odd


if __name__ == '__main__':
    req_even_odd(12345678910)
    even_odd_loop(12345678910)

"""
Рекурсия
Время выполнения: 0.21954159999999998
Используемая память: 0.00390625 MiB
Цикл
Время выполнения: 0.20499290000000003
Используемая память: 0.0 MiB

Цикл выполняется не только быстрее рекурсии, но и требует меньших затрат в памяти, так как каждый
вызов рекурсивной функции в данном случае пораждает еще один вызов. 
"""
