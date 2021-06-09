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


def revers_4(enter_num):
    return ''.join(reversed(str(enter_num)))


en_num = 97862143239478162341789623419856243158792341589234956174235897230147896708691243976584231
print("TimeIt:")
print(timeit("revers_1(en_num)", globals=globals(), number=1000000))
print(timeit("revers_2(en_num)", globals=globals(), number=1000000))
print(timeit("revers_3(en_num)", globals=globals(), number=1000000))
print(timeit("revers_4(en_num)", globals=globals(), number=1000000))

run("revers_1(en_num)")
run("revers_2(en_num)")
run("revers_3(en_num)")
run("revers_4(en_num)")

'''
revers_1 Рекурсией неэффективна. Много строк.
revers_2 Цикл while практически как и рекурсия.
revers_3 самая быстрая за счет среза строки.
revers_4 использование метода reversed. Хуже,чем revers_3,но сразу понятно в плане кода.

Через cProfile выдают только нули. Все функции достоточно быстрые.
'''
