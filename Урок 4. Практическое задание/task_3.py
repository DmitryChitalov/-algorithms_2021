"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Сделайте вывод, какая из трех реализаций эффективнее и почему!!!

И можете предложить еще свой вариант решения!
Без аналитики задание считается не принятым
"""
import timeit
import cProfile
import random


# рекурсия
def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


# цикл
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


# срез
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


# join
def revers_4(enter_num):
    lst = str(enter_num)
    lst = list(lst)
    lst.reverse()
    lst_r = ''.join(lst)
    return lst_r


num = int(random.randint(10 ** 11, 10 ** 12))
print(revers_1(enter_num=num, revers_num=0))
print(revers_2(enter_num=num, revers_num=0))
print(revers_3(enter_num=num))
print(revers_4(enter_num=num))

print('Время выполнения функций')
print(f"Рекурсия: {timeit.timeit('revers_1(num)', globals=globals(), number=10000)}")
print(f"Цикл: {timeit.timeit('revers_2(num)', globals=globals(), number=10000)}")
print(f"Срез: {timeit.timeit('revers_3(num)', globals=globals(), number=10000)}")
print(f"Join: {timeit.timeit('revers_4(num)', globals=globals(), number=10000)}")
print('Профилирование')
cProfile.run('revers_1(num)')
cProfile.run('revers_2(num)')
cProfile.run('revers_3(num)')
cProfile.run('revers_4(num)')

"""
Время выполнения функций
Рекурсия: 0.0683002
Цикл: 0.04245499999999999
Срез: 0.007536700000000007
Join: 0.014296200000000009
Анализ:
1.Самая быстрая работа через срез, т.е. реверс строки "На месте"
2.Далее идет цикл For. Чуть медленнее.
Для этих двух функций сложность O(n) - линейная.
3.Затем рекурсия. По результату из cProfile видно, что в этом случае функция
вызывает сама себя 13 раз. 
Утверждение что рекурсия облегчает работу программиста, а не программы на этом примере очевидно.
4. Функция с Join самая медленная и была добавлена для сравнения. 
В ней слишком много промежуточных действий.
"""
