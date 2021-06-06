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
print(timeit("revers_1(en_num)", globals=globals(), number=100000))
print(timeit("revers_2(en_num)", globals=globals(), number=100000))
print(timeit("revers_3(en_num)", globals=globals(), number=100000))
print(timeit("revers_4(en_num)", globals=globals(), number=100000))

run("revers_1(en_num)")
run("revers_2(en_num)")
run("revers_3(en_num)")
run("revers_4(en_num)")

'''
revers_1 функция с рекурсией - самая не эффективная, так как это рекурсия. По лаконичности тоже достаточно много строк.
revers_2 функция с циклом while - так же как и рекурсия по эффектичности и понятности написания отстаёт.
revers_3 самая быстра из всех. Практически моментальная, так как используется скрытая функция среза строки.
    Единственный минус это чтение такого способа. Может быть не всем понятен.
revers_4 использование метода reversed к строке. По эффективности на втором месте. Но как плюс сразу понятно
    что происходит в коде. Лидер по лаконичности.
    
Замеры через cProfile не выдают практически никакого результата. Так как впринципе все написанные функции достаточно
быстрые.
'''
