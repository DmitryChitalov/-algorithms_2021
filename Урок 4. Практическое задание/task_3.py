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


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)
num = 7423756423


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


def revers_4(enter_num):
    revers_num = ''
    for i in str(enter_num):
        revers_num = i + revers_num
    return revers_num



print(revers_1(num))

print(timeit('revers_1(num)', globals=globals( )))

print(revers_2(num))

print(timeit('revers_2(num)', globals=globals( )))

print(revers_3(num))

print(timeit('revers_3(num)', globals=globals( )))

print(revers_4(num))

print(timeit('revers_4(num)', globals=globals( )))


"""
Функция reverse_1 - показывает самый худший результат по времени, т. к. вы полняет количество вызовов равное длине 
обрабатываемого числа. 
Функция reverse_2 - цикл, по сравнению с рекурсивной функцией показывает результат лучше
Функция reverse_3 - Самая быстрая из представленных. Не производит расчетов, возваращает обратные значения. Пользуемся 
встроенными функциями, они уже максимально оптимизированы.
Функция reverse_4 - Циклом  на каждой итерации берет первую цифру оставшегося числа и с помощью конкатинации прилепляет 
его к результативной строке, вариант дольше функции 3.

"""