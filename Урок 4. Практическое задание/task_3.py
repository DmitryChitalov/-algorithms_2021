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

# Предложенный мною вариант revers_4 является самым труднозатратным. Менее затратным является revers_3 вариант -
# так как он по своей структуре превращается число в строку и переварачивает его с помощью среза. Другие варианты используют рекурсию,
# циклы, в моей варианте дополнительно заполняется список с элементами.


from cProfile import run
from timeit import timeit

num = 35685332

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


def revers_4(enter_num, my_list=[]):
    if enter_num == 0:
        return ''.join(str(x) for x in my_list)
    else:
        c = enter_num % 10
        my_list.append(c)
        enter_num = enter_num // 10
        return revers_4(enter_num)


print(timeit("revers_1(num)", globals=globals(), number=1000))
print(timeit("revers_2(num)", globals=globals(), number=1000))
print(timeit("revers_3(num)", globals=globals(), number=1000))
print(timeit("revers_4(num)", globals=globals(), number=1000))


def main():
    res_1 = revers_1(num)
    res_2 = revers_2(num)
    res_3 = revers_3(num)
    res_4 = revers_4(num)


run('main()')
