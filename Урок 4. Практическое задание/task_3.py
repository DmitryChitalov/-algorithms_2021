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
import cProfile


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


# так как все самые популярные способы присутствуют, я воспользовался встроенной ф-цией reversed, а затем
# преобразованием
def revers_4(enter_num):
    revers_num = reversed(str(enter_num))
    return "".join(map(str, list(revers_num)))


cProfile.run('revers_1(12345678901123321)')
cProfile.run('revers_2(12345678901123321)')
cProfile.run('revers_3(12345678901123321)')
cProfile.run('revers_4(12345678901123321)')

print("Revers_1 " + str(timeit("revers_1(12345678901123321)", "from __main__ import revers_1", number=10000)))
print("Revers_2 " + str(timeit("revers_2(12345678901123321)", "from __main__ import revers_2", number=10000)))
print("Revers_3 " + str(timeit("revers_3(12345678901123321)", "from __main__ import revers_3", number=10000)))
print("Revers_4 " + str(timeit("revers_4(12345678901123321)", "from __main__ import revers_4", number=10000)))

"""
С точки зрения эффективности однозначно будет самой эффективной третья (ибо она имеет низкую сложность), 
четвертая на втором месте, вторая на третьем и первая на последнем.  
"""
