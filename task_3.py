"""
Задание 3.
Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.
Сделайте профилировку каждого алгоритма через cProfile и через timeit
Обязательно предложите еще свой вариант решения и также запрофилируйте!
Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!
Без аналитики задание считается не принятым
"""
from timeit import Timer
import cProfile

enter_number = 258963

def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num

def revers_4(enter_num): # Свой вариант функции
    final_number = 0

    while enter_num > 0:
        last_num = enter_num % 10
        enter_num = enter_num // 10
        final_number = final_number * 10 + last_num
    return final_number
#функция конечно немного бредовая))) но все хорошее уже написанно выше)

t1 = Timer("revers_1(enter_number)", globals=globals())
print("revers_1 ", t1.timeit(number=1000), "seconds")

t2 = Timer("revers_3(enter_number)", globals=globals())
print("revers_2 ", t2.timeit(number=1000), "seconds")

t3 = Timer("revers_3(enter_number)", globals=globals())
print("revers_3 ", t3.timeit(number=1000), "seconds")

t4 = Timer("revers_4(enter_number)", globals=globals())
print("revers_4 ", t4.timeit(number=1000), "seconds")

def main():
    revers_1(enter_number)
    revers_2(enter_number)
    revers_3(enter_number)
    revers_4(enter_number)

cProfile.run('main()')

"""
revers_1  0.002242300019133836 seconds
revers_2  0.0004206000012345612 seconds
revers_3  0.0003996000159531832 seconds
revers_4  0.0012676999904215336 seconds
"""

"""
По результатам можно сказать что самой быстрой являеются функции revers_2 и revers_3
А самой медленной revers_1 
cProfile показал рекурсию вызовов первой функции
самой простой является функция revers_4 но время ее выполнения не самое лучшее
самым хорошим вариантом написания лично для меня является функция revers_2
"""