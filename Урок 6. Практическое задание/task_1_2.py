# Упрощенный калькулятор из урока с рекурсиями
from memory_profiler import profile


class MyError(Exception):
    def __init__(self, txt: str):
        self.txt = txt

@profile()
def calculate(a, b, counter):
    try:
        #op = input('Введите операцию (+, -, *, / или 0 для выхода) ')
        op = '/'
        if op not in ['+', '-', '*', '/', '0']:
            raise MyError('Необходимо выбирать знак из списка')
    except MemoryError:
        print('Не верный знак')
    except MyError as err:
        print(err)
        calculate()
    if counter == 0:
        op = '0'
    if op == '0':
        return
    try:
        # a = int(input('Введите первое число '))
        # b = int(input('Введите второе число '))
        if op == '+':
            print(a + b)
        if op == '-':
            print(a - b)
        if op == '*':
            print(a * b)
        if op == '/':
            print(a / b)
        calculate(a, b, counter - 1)
    except ValueError:
        print('Вы ввели не число')
        calculate(a, b, counter - 1)
    except ZeroDivisionError:
        print('Делить на 0 нельзя')
        calculate(a, b, counter - 1)



@profile()
def calculate2(a, b, num):
    for i in range(num):
        try:
            # op = input('Введите операцию (+, -, *, / или 0 для выхода) ')
            op = '/'
            if op not in ['+', '-', '*', '/', '0']:
                raise MyError('Необходимо выбирать знак из списка')
        except MemoryError:
            print('Не верный знак')
        except MyError as err:
            print(err)
            calculate()

        if op == '0':
            return
        try:
            # a = int(input('Введите первое число '))
            # b = int(input('Введите второе число '))
            if op == '+':
                print(a + b)
            if op == '-':
                print(a - b)
            if op == '*':
                print(a * b)
            if op == '/':
                print(a / b)
        except ValueError:
            print('Вы ввели не число')
        except ZeroDivisionError:
            print('Делить на 0 нельзя')


calculate(50, 2, 3)
calculate2(50, 2, 3)

"""
Вывел только результаты замеров последней функции (так как не смог замерить рекурсию)
Оптимизация происходит за счет использования циклов вместо рекурсии
Так как рекурсия потребляет большое кол-во памяти, то переход на циклы уменьшит данные затраты
"""

# 46     14.7 MiB     14.7 MiB           1   @profile()
#     47                                         def calculate2(a, b, num):
#     48     14.7 MiB      0.0 MiB           4       for i in range(num):
#     49     14.7 MiB      0.0 MiB           3           try:
#     50                                                     # op = input('Введите операцию (+, -, *, / или 0 для выхода) ')
#     51     14.7 MiB      0.0 MiB           3               op = '/'
#     52     14.7 MiB      0.0 MiB           3               if op not in ['+', '-', '*', '/', '0']:
#     53                                                         raise MyError('Необходимо выбирать знак из списка')
#     54                                                 except MemoryError:
#     55                                                     print('Не верный знак')
#     56                                                 except MyError as err:
#     57                                                     print(err)
#     58                                                     calculate()
#     59
#     60     14.7 MiB      0.0 MiB           3           if op == '0':
#     61                                                     return
#     62     14.7 MiB      0.0 MiB           3           try:
#     63                                                     # a = int(input('Введите первое число '))
#     64                                                     # b = int(input('Введите второе число '))
#     65     14.7 MiB      0.0 MiB           3               if op == '+':
#     66                                                         print(a + b)
#     67     14.7 MiB      0.0 MiB           3               if op == '-':
#     68                                                         print(a - b)
#     69     14.7 MiB      0.0 MiB           3               if op == '*':
#     70                                                         print(a * b)
#     71     14.7 MiB      0.0 MiB           3               if op == '/':
#     72     14.7 MiB      0.0 MiB           3                   print(a / b)
#     73                                                 except ValueError:
#     74                                                     print('Вы ввели не число')
#     75                                                 except ZeroDivisionError:
#     76                                                     print('Делить на 0 нельзя')