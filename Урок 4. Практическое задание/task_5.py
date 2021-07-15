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


# def
def e_cieve(n, offset = 1, ls=[]):
    arr = [*filter(lambda x: x != 0, ls)]
    if len(arr) == n:
        return arr
    else:
        if offset == 2 and len(arr) == 0:
            ls.append(2)
        else:
            for el in arr:
                if offset % el == 0 or offset % 2 == 0 or offset == el:
                    ls.append(0)
                    break
                else:
                    ls.append(offset)
                    break
    return e_cieve(n, offset+1, ls)

print(simple(5))
print(e_cieve(5))

#i = int(input('Введите порядковый номер искомого простого числа: '))
#print(simple(i))
