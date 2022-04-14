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
    reverse_str = "".join(reversed(str(enter_num)))
    return reverse_str


num_s = 456789
print(f"{'~'*30}Timeit{'~'*30}"
      f"\nRevers 1 func time: {timeit('revers_1(num_s)', globals=globals())}"
      f"\nRevers 2 func time: {timeit('revers_2(num_s)', globals=globals())}"
      f"\nRevers 3 func time: {timeit('revers_3(num_s)', globals=globals())}"
      f"\nRevers 4 func time: {timeit('revers_4(num_s)', globals=globals())}"
      f"\n\n{'~'*30}cProfile{'~'*30}"
      f"\nRevers 1 func time: {run('revers_1(num_s)')}"
      f"\nRevers 2 func time: {run('revers_2(num_s)')}"
      f"\nRevers 3 func time: {run('revers_3(num_s)')}"
      f"\nRevers 4 func time: {run('revers_4(num_s)')}")
"""
Быстрее всего варианты 3 и 4. 3 вариант простой срез по строке
4 вариант чуть дольшк, т.к происходит сначала работа функции перевода в строку, а потом функции reversed. 
Функция reversed, в свою очередь, возвращает ебъект reverse, который необходимо еще и распаковать.
"""