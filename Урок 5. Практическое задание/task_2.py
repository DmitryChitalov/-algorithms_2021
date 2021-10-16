"""
2. Написать программу сложения и умножения двух шестнадцатиричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

Подсказка:
Для решения задачи обязательно примените какую-нибудь коллекцию из модуля collections
Для лучшее освоения материала можете даже сделать несколько решений этого задания,
применив несколько коллекций из модуля collections
Также попробуйте решить задачу вообще без collections и применить только ваши знания по ООП
(в частности по перегрузке методов)

__mul__
__add__

Пример:
Например, пользователь ввёл A2 и C4F.
Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’]
Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

1. вариант
defaultdict(list)
int(, 16)
reduce

2. вариант
class HexNumber:
    __add__
    __mul__

hx = HexNumber
hx + hx
hex()
"""
from collections import deque


def sum_sixteen(first_num, second_num):
    if len(second_num) > len(first_num):
        first_num, second_num = second_num, first_num

    res = deque()
    remains = [0]
    first_num.reverse()
    second_num.reverse()
    count = len(second_num)
    six_dict = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}

    for i in range((len(first_num) - 1) + 1):

        if count > 0:
            sum_el = int(first_num[i], 16) + int(second_num[i], 16) + remains[-1]
            if sum_el > 16:
                remains.append(1)
                res.appendleft(sum_el - 16)
                count -= 1
            else:
                remains.append(0)
                res.appendleft(sum_el)
                count -= 1
        else:
            if int(first_num[i], 16) + remains[-1] > 16:
                remains.append(1)
                res.appendleft(first_num[i] - 16)
            else:
                remains.append(0)
                res.appendleft(int(first_num[i], 16) + remains[-1])
    if remains[-1] == 1:
        res.appendleft(remains[-1])

    sum_res = [six_dict[i] for i in res]
    return ''.join(sum_res)


print(sum_sixteen(list(input('Введите первое число: ')), list(input('Введите второе число: '))))

"""
Сделал сам, используя те средства, которые знал. Делал до разбора ДЗ на уроке, поэтому решил оставить свое решение,
чтобы понять имеет ли право на существование данное решение. К сожалению, очень долго провозился с решение, времени на 
умножение не хватило.
Разбор на уроке посмотрел, обещаю разобраться в средствах, использованных в разборе ДЗ.
"""