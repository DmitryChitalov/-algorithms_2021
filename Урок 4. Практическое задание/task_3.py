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
from cProfile import run
from timeit import timeit


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


def main():
    revers_1(1234567890)
    revers_2(1234567890)
    revers_3(1234567890)


# Выводим числа на экран
print(revers_1(1234567890))
print(revers_2(1234567890))
print(revers_3(1234567890))

######################################################################################################################

# Профилировка функции revers_1 с помощью timeit и cProfile
print('revers_1', timeit('revers_1(1234567890)', globals=globals()), 'seconds', end=f'\n{"-" * 100}\n')
run('''
for _ in range(1000000):
    revers_1(1234567890)''')

######################################################################################################################

# Профилировка функции revers_2 с помощью timeit и cProfile
print('revers_2', timeit('revers_2(1234567890)', globals=globals()), 'seconds', end=f'\n{"-" * 100}\n')
run('''
for _ in range(1000000):
    revers_2(1234567890)''')

######################################################################################################################

# Профилировка функции revers_3 с помощью timeit и cProfile
print('revers_3', timeit('revers_3(1234567890)', globals=globals()), 'seconds', end=f'\n{"-" * 100}\n')
run('''
for _ in range(1000000):
    revers_3(1234567890)''')


######################################################################################################################

# Свой вариант реверса

def revers_4(enter_num):
    lst_obj = list(str(enter_num))
    lst_obj.reverse()
    return ''.join(lst_obj)


# Профилировка функции revers_4 с помощью timeit и cProfile
print('revers_4', timeit('revers_4(1234567890)', globals=globals()), 'seconds', end=f'\n{"-" * 100}\n')
run('''
for _ in range(1000000):
    revers_4(1234567890)''')

'''
Аналитика:
Функция revers_1 самая долгая и неэффективная из-за рекурсии, а также результат получается 
не совсем правильный, тип результата float и ноль остаётся в конце. Функция revers_2 также дает некорректный 
результат и выполняется долго из-за цикла. Функция revers_3 самая удачная так как берется срез по 
обратной индексации. В функции revers_4 используются встроенные функции, поэтому скорость чуть ниже.
'''