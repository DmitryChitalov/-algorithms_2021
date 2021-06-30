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


def simple_1(i):
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


def simple_2(i):
    """С использованием «Решета Эратосфена»"""
    sim = []
    k = 1
    while len(sim) != i:
        sim.append(k)
        print(sim)

        for el in range(1, len(sim)):
            print(el)
            if k % sim[el] == 0 and k != sim[el]:
                sim[el] = 0
        k += 1



    """
    count = 100
    k = 1
    n = 1
    my_set = set()
    sim = [1]
    print(len(sim))
    #print(sim[k-1])
    while len(my_set) != i:
        sim.append(n)
        #k = 1
        #sim = []
        while len(sim)-k+1 != 0:
            if n % sim[k-n] == 0 and k != n:
                sim[k] = 0
            k += 1
            print(sim)

        n += 1
        my_set = set(sim)
    print(my_set)
"""



'''
        for el in range(1, len(sim)):
            if sim[el] % n == 0 and sim[el] != n:
                sim[el] = 0
                sim.append(len(sim)+1)

                #sim.append(len(sim)+1)#sim.append(len(sim)+1)
                #k = k + 1
                #n = 2
                #ind = sim.index(el)


        n = n + 1
        my_set = set(sim)
        count = count - 1



    #sim = [1, 2]
    #while count == 0:
    #    while len(sim) != 100:
    #        sim.append(n)
    #    #n = n + 1
    #    count = count - 1
    print(sim)
    print(len(sim))
    my_set = set(sim)
    print(my_set)
    print(len(my_set))
'''


num = 100 #int(input('Введите порядковый номер искомого простого числа: '))
print(simple_1(num))
print(simple_2(num))

