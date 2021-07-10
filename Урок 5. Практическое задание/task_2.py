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
'''Выполнила только одним способом, задействовав deque, на другие варианты решения времени
к сожалению, катастрофически не хватает.
Задание действительно объемное и не самое простое, хотя и интересное.

Также было не очень понятно, каким должен быть формат вывода, сделала как в примере к заданию.
'''


def cheat_sheet():
    """Function makes cheat sheet for comparison data"""
    my_cheat_sheet = list('0123456789ABCDEF')
    return deque(my_cheat_sheet)


# СЛОЖЕНИЕ
def prepare_for_add(deq_1, deq_2):
    """Makes copies of original deque objects for work and equalizes its lenght"""
    cp_dq1 = deq_1.copy()
    cp_dq2 = deq_2.copy()
    if not len(deq_1) == len(deq_2):
        if len(deq_1) < len(deq_2):
            cp_dq1.extend(['0', ] * (len(cp_dq2) - len(cp_dq1)))
        else:
            cp_dq2.extend(['0', ] * (len(cp_dq1) - len(cp_dq2)))
    return cp_dq1, cp_dq2


def simple_addition(list_of_ready_made_indexes, my_cheat_sheet, keep_in_mind=0):
    """Function of adding "in each vowel column", using a list of ready-made indexes"""
    result = deque([])
    for inx in list_of_ready_made_indexes:
        temp_result = inx + keep_in_mind
        if temp_result >= len(my_cheat_sheet):
            num = my_cheat_sheet[temp_result - len(my_cheat_sheet)]
            keep_in_mind = temp_result//len(my_cheat_sheet)
            result.append(num)
        else:
            num = my_cheat_sheet[inx + keep_in_mind]
            result.append(num)
            keep_in_mind = 0
    if keep_in_mind > 0:
        result.append(str(keep_in_mind))
    return result


def hex_addition(dq_1, dq_2):
    """Starting addition function"""
    my_cheat_sheet = cheat_sheet()
    dq_cp1, dq_cp2 = prepare_for_add(dq_1, dq_2)
    my_indexes = list(map(lambda x, y:
                          my_cheat_sheet.index(x) + my_cheat_sheet.index(y), dq_cp1, dq_cp2))
    result = simple_addition(my_indexes, my_cheat_sheet)
    return result


# УМНОЖЕНИЕ
def pairwise_add(temp_results_storage, i=0):
    """Pairwise addition of list items by recursion"""
    if i >= len(temp_results_storage)-2:
        end_of_recursion = hex_addition(temp_results_storage[i], temp_results_storage[i + 1])
        return end_of_recursion
    return hex_addition(temp_results_storage[i], pairwise_add(temp_results_storage, i+1))


def filling_temp_results_storage(multiplier_1, second_deque, hold_in_mind=0):
    """Multiplies all elements of the second list(deque) with specified multiplier"""
    my_cheat_sheet = cheat_sheet()
    temp_deque = deque([])
    for mult_2 in second_deque:
        temp_result = (my_cheat_sheet.index(multiplier_1) *
                       my_cheat_sheet.index(mult_2)) + hold_in_mind
        if temp_result > len(my_cheat_sheet):
            num = my_cheat_sheet[temp_result % len(my_cheat_sheet)]
            hold_in_mind = temp_result // len(my_cheat_sheet)
            temp_deque.append(num)
        else:
            num = my_cheat_sheet[temp_result]
            hold_in_mind = 0
            temp_deque.append(num)
    temp_deque.append(my_cheat_sheet[hold_in_mind])
    temp_deque.reverse()
    return temp_deque


def hex_multiplication(dq_1, dq_2, digit_place=0):
    """Starting multiplication function"""
    storage_deque = deque([])
    for multiplier in dq_1:
        intermediate_result = filling_temp_results_storage(multiplier, dq_2)
        intermediate_result.reverse()
        intermediate_result.extendleft(['0', ] * digit_place)
        storage_deque.append(intermediate_result)
        digit_place += 1
    result = pairwise_add(storage_deque)
    result.reverse()
    return result


def transformation_into_deque(some_list):
    """Function transforms input data into deque and prepare it for operations"""
    new_deque = deque(some_list)
    new_deque.reverse()
    return new_deque


def hex_greeting():
    """Start interactive dialog function"""
    while True:
        try:
            num1 = (input("Введите первое шестнадцатеричное число: "))
            float.fromhex(num1)
            num2 = (input("Введите второе шестнадцатеричное число: "))
            float.fromhex(num2)
            dq1 = transformation_into_deque(list(num1.upper()))
            dq2 = transformation_into_deque(list(num2.upper()))
            choise = (input("Выберите действие.  Для сложения введите +, в ином случае"
                            " будет выполнено умножение: "))
            if choise == '+':
                res = hex_addition(dq1, dq2)
                res.reverse()
                print(f"Сумма чисел: {res}")
            else:
                res = hex_multiplication(dq1, dq2)
                print(f"Произведение чисел: {res}")
            break
        except ValueError:
            print('\nВводите только шестнадцатеричные числа. Попробуйте еще раз\n')


hex_greeting()

# Числа для пробы:
# A2 C4F - CF1 7C9FE
# C333 DDA - D10D A8FD06E
# ABCD BAD678 - BB8245 7D62DFE618
# dfa67 dff67
# aaafff fffaaa
