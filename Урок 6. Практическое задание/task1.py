import math
from memory_profiler import profile, memory_usage

companies = {'c1': 3032, 'c2': 2343, 'c3': 4853, 'c4': 3443, 'c5': 9342}

def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_usage()
        res = func(args[0])
        m2 = memory_usage()
        mem_diff = m2[0] - m1[0]
        return res, mem_diff
    return wrapper

@decor
def func1(companies):
    greatest_companies = []
    v = (max(companies.values())) #O(n)
    temp = companies.copy()
    k = 1
    while k <= 3:
        for i in temp.keys(): #O(n)
            if temp[i] == v:
                greatest_companies.append(i)
                temp[i] = -1000
                v = (max(temp.values()))
                k += 1
    return greatest_companies
#O(N)
@decor
def func2(companies):
    list_d = list(companies.items()) #O(len())
    list_d.sort(key=lambda i: i[1]) #O(N*LOG(N))
    greatest_companies = [list_d[-1][0], list_d[-2][0], list_d[-3][0]]
    return greatest_companies




@decor
def revers_1(enter_num, revers_num = 0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)
@decor
def revers_2(enter_num, revers_num = 0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num//= 10
    return revers_num
@decor
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

@decor
def sieve_without_eratosthenes(i):
    lst_prime = [2]
    number = 3
    while len(lst_prime) < i:
        flag = True
        for j in lst_prime.copy():
            if number % j == 0:
                flag = False
                break
        if flag:
            lst_prime.append(number)
        number += 1
    return lst_prime[-1]

@decor
def sieve_eratosthenes(i):
    i_max = prime_counting_function(i)
    lst_prime = [_ for _ in range(2, i_max)]

    for number in lst_prime:
        if lst_prime.index(number) <= number - 1:
            for j in range(2, len(lst_prime)):
                if number * j in lst_prime[number:]:
                    lst_prime.remove(number * j)
        else:
            break
    return lst_prime[i - 1]

def prime_counting_function(i):
    number_of_primes = 0
    number = 2
    while number_of_primes <= i:
        number_of_primes = number / math.log(number)
        number += 1
    return number


if __name__ == '__main__':
    res, mem_diff = revers_1(32649723552)
    print(f'{mem_diff} Mib')  # 015625 Mib
    res, mem_diff = revers_2(32649723552)
    print(f'{mem_diff} Mib')  # 0.0078125 Mib
    res, mem_diff = revers_3(32649723552)
    print(f'{mem_diff} Mib')  # 0.00390625 Mib


    res, mem_diff = func1(companies)
    print(f'{mem_diff} Mib')  # 0.0078125 Mib
    res, mem_diff = func2(companies)
    print(f'{mem_diff} Mib')  # 0.0078125 Mib


    res, mem_diff = sieve_without_eratosthenes(20)
    print(f'{mem_diff} Mib')  # 0.00390625 Mib
    res, mem_diff = sieve_eratosthenes(20)
    print(f'{mem_diff} Mib')  # 0.015625 Mib

# Анализируя полученные данные, можно сделать вывод что для функций reverse
# меньше всего памяти использует последняя функция, а больше всего - первая
# достигается это скорее всего благодаря отсутствию большого количества присваиваний в последних реализациях
# что позволяет использовать меньшее количество памяти

# функции func1 и func2 занимают одинаковое количество памяти, что связана со схожей структруой этих функций

# последние функции по поиску n простого числа работают по разным алгоритмам, и, как мы видим, эффективнее по памяти работает функция без использования алгоритма Эратосфена
# работая быстрее по скорости, такой реализации требуется дополнительная память, в том числе и засчет вызова вспомогательной функции внутри основной

