"""
2.*	Написать программу сложения и умножения двух шестнадцатиричных чисел.
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
"""
"""from collections import Counter

OBJ = Counter(['js', 'java', 'java', 'python', 'python', 'python'])

print(type(OBJ))
print(OBJ)

print(OBJ['python'])
print(OBJ['pere'])

OBJ = Counter('abrakadabra')
print(OBJ)

OBJ = Counter(python=2, java=4, ci=3)
print(list(OBJ.elements()))

print(Counter('abracadabra').most_common(2))
print(Counter('abracadabra').most_common())"""

"""from collections import defaultdict

d = dict()
d['раз'] = 1
d['два'] = 2
print(d)
# print(d['три'])

b = defaultdict(int)
b['раз'] = 1
b['два'] = 2
print(b)
print(b['три'])
print(b)"""

from collections import defaultdict

sentence = 'Ехал Грека через реку, Видит Грека - в реке рак. Сунул Грека руку в реку - рак не цапает никак!'
words = sentence.split(' ')

"""def test_simple_dict():
    Обычный словарь
    reg_dict = {}
    for word in words:
        if word in reg_dict:
            reg_dict[word] += 1
        else:
            reg_dict[word] = 1
    return reg_dict


def test_default_dict():
    Вариант с defaultdict
    d = defaultdict(int)
    for word in words:
        d[word] += 1
    return d


print(test_default_dict())
print(test_simple_dict())"""

"""from collections import deque

simple_1st = list('bcd')
deq_obj = deque(simple_1st)
print(deq_obj)

deq_obj.append('e')
print(deq_obj)

deq_obj.appendleft('a')
print(deq_obj)"""
"""from collections import ChainMap

computer_parts = {
    'system_bock': 1,
    'monitor': 1,
    'keyboard_mouse': 1
}

computer_options = {
    'RAM': '8 Gb',
    'HDD': '1000 Gb',
    'PROC': 'Intel Core i5'
}

computer_accessories = {
    'RAM': '6 Gb',
    'gaming': False,
    'divided': True
}

computer = ChainMap(computer_parts, computer_options, computer_accessories)
print(type(computer))
print(computer)"""
