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


i = int(input('Введите порядковый номер искомого простого числа: '))
print(simple(i))
upper_num = 1000

def eratosphen(i):
    prime_num_list = [p for p in range(upper_num)]
    divider_list = [l for l in range(2, int(upper_num ** 0.5) + 1)]
    prime_num_list[1] = 0
    for q in divider_list:
        for t in prime_num_list:
            if t != 0:
                if q != t and t % q == 0:
                    prime_num_list[t] = 0
    prime_num_list = [h for h in prime_num_list if h != 0]
    return prime_num_list[i-1]


print(timeit('simple(i)', globals=globals(), number=10))            # 0.0006332989999009442
print(timeit('eratosphen(i)', globals=globals(), number=10))        # 0.043560145999890665

print(timeit('simple(i)', globals=globals(), number=100))           # 0.0057115120000617026
print(timeit('eratosphen(i)', globals=globals(), number=100))       # 0.4027847229999679

print(timeit('simple(i)', globals=globals(), number=1000))          # 0.056205343999863544
print(timeit('eratosphen(i)', globals=globals(), number=1000))      # 3.7448549129999265


# Функция на алгоритме "решето Эратосфена" работает значительно медленнее, так как имеет сложность O(n**2) и работает
# со списками. Первый алгоритм имеет также квадратичную сложность сложность, но выигрывает в силу того, что не оперирует
# множествами.