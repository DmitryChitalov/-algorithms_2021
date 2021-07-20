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
from timeit import timeit
from cProfile import run


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


def revers_4(enter_num, revers_num=0):
    num = len(str(enter_num))
    for _ in range(num):
        num = enter_num % 10
        revers_num = (revers_num * 10) + num
        enter_num //= 10

    return revers_num


def revers_5(enter_num):
    my_list = list(str(enter_num))
    my_list.reverse()
    # converting list into number
    return ''.join(my_list)


number = 98789697987

print("revers_1: ", timeit(stmt="revers_1(number)", number=100000, globals=globals()))
print("revers_2: ", timeit(stmt="revers_2(number)", number=100000, globals=globals()))
print("revers_3: ", timeit(stmt="revers_3(number)", number=100000, globals=globals()))
print("revers_4: ", timeit(stmt="revers_3(number)", number=100000, globals=globals()))
print("revers_5: ", timeit(stmt="revers_3(number)", number=100000, globals=globals()))

run('revers_1(number)')
run('revers_2(number)')
run('revers_3(number)')
run('revers_4(number)')
run('revers_5(number)')

"""
revers_1:  1.1993071
revers_2:  0.4233123000000001
revers_3:  0.0987146000000001
revers_4:  0.09894999999999987
revers_5:  0.09915370000000001

Добавлены методы revers_4 и revers_5.

Выводы:
Самая эффективная реализация реверса числа - функция со срезами revers_3.
Имеет наименьшее время выполнения согласно библиотеки timeit и содержит 4 вызова функции на запуск которых ушло 
0 секунд, согдасно библиотеки cProfile.
  
Так же, хорошее время показали методы revers_4 и revers_5, но у revers_4 - 5 вызовов функции, а у revers_5 - 6 вызовов.
"""
