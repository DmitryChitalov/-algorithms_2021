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


def sieve_eratosthenes(find):
    number = find * 10
    numbers = list(range(number + 1))
    numbers[1] = 0
    i = 2
    while i <= number:
        if numbers[i] != 0:
            j = i + i
            while j <= number:
                numbers[j] = 0
                j += i
        i += 1
    a = set(numbers)
    a.remove(0)
    a = sorted(list(a))
    return a[find - 1]


print(sieve_eratosthenes(i))


my_numbers = ['10', '100', '1000']

for num in my_numbers:
    print(f"{num}-й элемент найден за {round(timeit(f'simple({num})', globals=globals(), number=1), 5)} сек")

print('Решето Эратосфена:')
for num in my_numbers:
    print(f"{num}-й элемент найден за {round(timeit(f'sieve_eratosthenes({num})', globals=globals(), number=1), 5)} сек")

# Алгоритм с использованием решета Эратосфена более эффективен, имея логарифмеческую сложность по времени,
# но дополнительно затрачивает память для создания списка отсортированных (простых) чисел
# Для нахождения большего элемента по счёту нужно создавать более объемный список для наполнения его простыми числами
