from timeit import timeit
from cProfile import run

# рекурсия
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)

# цикл сложность O(1) * N == O(N)
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:                               # O(1)
        num = enter_num % 10                            # O(1)
        revers_num = (revers_num + num / 10) * 10       # 0(1)
        enter_num //= 10                                # 0(1)
    return revers_num                                   # 0(1)

# срез сложность O(N)
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

# рекусия с операцией вставки в конец списка
def revers_4(enter_num, revers_num=[]):
    if enter_num == 0:
        return revers_num
    else:
        i = enter_num % 10
        enter_num //= 10
        revers_num.append(i)
        return revers_4(enter_num, revers_num)


print(revers_4(123))

print(f'Time for revers_1 "Рекурсия" is {timeit("revers_1(12389)", globals=globals())} seconds')
print(f'Time for revers_2 "Цикл" is {timeit("revers_2(12389)", globals=globals())} seconds')
print(f'Time for revers_3 "Срез" is {timeit("revers_3(12389)", globals=globals())} seconds')
print(f'Time for revers_4 "Рекурсия со списком" is {timeit("revers_4(12389)", globals=globals())} seconds')
print('########################################################################################')


def main ():
    revers_1(123)
    revers_2(123)
    revers_3(123)
    revers_4(123)


run('main()')

'''
Time for revers_1 "Рекурсия" is 2.1535829 seconds
Time for revers_2 "Цикл" is 1.5263482000000002 seconds
Time for revers_3 "Срез" is 0.5291202999999998 seconds
Time for revers_4 "Рекурсия со списком" is 2.0172999000000003 seconds
########################################################################################
         17 function calls (11 primitive calls) in 0.000 seconds

   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.000    0.000    0.000    0.000 <string>:1(<module>)
        1    0.000    0.000    0.000    0.000 main.py:17(revers_2)
        1    0.000    0.000    0.000    0.000 main.py:25(revers_3)
      4/1    0.000    0.000    0.000    0.000 main.py:31(revers_4)
        1    0.000    0.000    0.000    0.000 main.py:50(main)
      4/1    0.000    0.000    0.000    0.000 main.py:7(revers_1)
        1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
        3    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

Вывод: наиболее эффективно работает срез. Цикл работает несколько медленнее. Самый затратный вариант - рекурсия. 
'''
