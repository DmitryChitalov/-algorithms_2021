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
from functools import lru_cache

# Сложность аогоритма примерно O(n^2)
def simple(i):
    """Без использования «Решета Эратосфена»"""
    count = 1
    n = 2
    while count <= i: # O(n)
        t = 1
        is_simple = True
        while t <= n: # O(n)
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
############################################################
def erat(i):
    cnt = i*100
    res_list = [el for el in range(cnt + 1)]
    res_list[1] = 0
    el = 1
    while el<=cnt:
        if res_list[el] != 0:
            el2 = el+el
            while el2<=cnt:
                res_list[el2]=0
                el2+=el
        el+=1
    res_list = set(res_list)
    res_list.remove(0)
    return sorted(list(res_list))[i-1]

@lru_cache()
def erat_mem(i):
    cnt = i*100
    res_list = [el for el in range(cnt + 1)]
    res_list[1] = 0
    el = 1
    while el<=cnt:
        if res_list[el] != 0:
            el2 = el+el
            while el2<=cnt:
                res_list[el2]=0
                el2+=el
        el+=1
    res_list = set(res_list)
    res_list.remove(0)
    return sorted(list(res_list))[i-1]


##############################################################################

i = 10
print("*"*20)
print(f"simple res :{simple(i)}")
print(f"erat res : {erat(i)}")
print(f"simple N10 time: {timeit('simple(i)',setup='from __main__ import simple,i',number=10)}")
print(f"erat N10 time: {timeit('erat(i)',setup='from __main__ import erat,i',number=10)}")
print(f"erat_mem N10 time: {timeit('erat_mem(i)',setup='from __main__ import erat_mem,i',number=2)}")

i = 100
print("*"*20)
print(f"simple res :{simple(i)}")
print(f"erat res : {erat(i)}")
print(f"simple N100 time: {timeit('simple(i)',setup='from __main__ import simple,i',number=10)}")
print(f"erat N100 time: {timeit('erat(i)',setup='from __main__ import erat,i',number=10)}")
print(f"erat_mem N100 time: {timeit('erat_mem(i)',setup='from __main__ import erat_mem,i',number=2)}")


i = 1000
print("*"*20)
print(f"simple res :{simple(i)}")
print(f"erat res : {erat(i)}")
print(f"simple N1000 time: {timeit('simple(i)',setup='from __main__ import simple,i',number=10)}")
print(f"erat N1000 time: {timeit('erat(i)',setup='from __main__ import erat,i',number=10)}")
print(f"erat_mem N1000 time: {timeit('erat_mem(i)',setup='from __main__ import erat_mem,i',number=2)}")

i = 10000
print("*"*20)
print(f"erat res : {erat(i)}")
print(f"erat N10000 time: {timeit('erat(i)',setup='from __main__ import erat,i',number=2)}")
print(f"erat_mem N10000 time: {timeit('erat_mem(i)',setup='from __main__ import erat_mem,i',number=2)}")

i = 100000
print("*"*20)
print(f"erat res : {erat(i)}")
print(f"erat N100000 time: {timeit('erat(i)',setup='from __main__ import erat,i',number=2)}")
print(f"erat_mem N100000 time: {timeit('erat_mem(i)',setup='from __main__ import erat_mem,i',number=2)}")

i = 1000000
print("*"*20)
print(f"erat_mem res : {erat(i)}")
print(f"erat_mem N100000 time: {timeit('erat_mem(i)',setup='from __main__ import erat_mem,i',number=2)}")

'''
Замеры показывают рост эффективности алгоритма Эратосфена erat() относительно предложенного 
алгоритма simple(), в зависимости от порядкового номера искомого элемента, 
чем выше порядковый номер тем эффективнее.
Кешированный алгоритм Эратосфена erat_mem() в ~10 раз быстрее erat()

****** 10 ********
simple res :29
erat res : 29
simple N10 time: 0.0002974000000000032
erat N10 time: 0.0043295
erat_mem N10 time: 0.0005379000000000078

****** 100 ********
simple res :541
erat res : 541
simple N100 time: 0.0497109
erat N100 time: 0.062306
erat_mem N100 time: 0.006850899999999993

***** 1 000 *******
simple res :7919
erat res : 7919
simple N1000 time: 6.3057765
erat N1000 time: 0.5345312
erat_mem N1000 time: 0.0491918999999994

***** 10 000 *****
simple res :104729
erat res : 104729
simple N10000 time: 144.58362540000002
erat N10000 time: 1.1422931999999832
erat_mem N10000 time: 0.6640497999999866

***** 100 000 *******
erat res : 1299709
erat N100000 time: 13.917193100000002
erat_mem N100000 time: 6.8716133999999975

****** 1 000 000 ********
erat_mem res : 15485863
erat_mem N100000 time: 72.65077180000002
'''