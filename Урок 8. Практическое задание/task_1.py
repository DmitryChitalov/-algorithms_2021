"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.


2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""

from collections import deque
from operator import itemgetter

table = dict()


class HaffmanWood:
    def __init__(self, st):
        self.st = st

    # метод считающий уникальные символы
    def count(self):
        dct = dict()
        set_val = set()
        for i in self.st:
            values = f'{i}:{self.st.count(i)}'
            set_val.add(values)
        for i in set_val:
            values = i.split(':')
            dct[values[0]] = int(values[1])
        return dct

    # метод сортирующий по возврастанию символы по повторению
    def sort_simbols(self, dct, sort_els=None):
        sort_els = deque(sorted(dct.items(), key=itemgetter(1)))
        return sort_els

    # метод для построения дерева
    def making_wood(self, sort_els):
        if len(sort_els) > 1:
            while True:
                if len(sort_els) <= 1:
                    break
                heft = sort_els[0][1] + sort_els[1][1]
                joint = dict()
                joint[0] = sort_els.popleft()[0]
                joint[1] = sort_els.popleft()[0]

                i = 0
                for el in sort_els:
                    if heft > el[1]:
                        continue
                    else:
                        sort_els.insert(i, (joint, heft))
                        break
                    i += 1
                else:
                    sort_els.append((joint, heft))
        else:
            heft = sort_els[0][1]
            joint = dict()
            joint[0] = sort_els.popleft()[0]
            joint[1] = None
            sort_els.append((joint, heft))
        return sort_els[0][0]


# функция для кодирования Хаффмана
def haff_codding(wood, track=str()):
    if not isinstance(wood, dict):
        table.update({wood: track})
    else:
        haff_codding(wood.get(0), track='%s0' % track)
        haff_codding(wood.get(1), track='%s1' % track)


# строка для кодирования
string = 'Raspberry Pi 4B and Raspberry Pi 3B+'
print()

w = HaffmanWood(string)
counter = w.count()
print(counter)
print()

'''
Результат работы метода класса подсчёта уникальных символов:

{'e': 2, 'i': 2, 'b': 2, 'a': 3, 'R': 2, 'P': 2, '4': 1, '3': 1, '+': 1, 'B': 2, 
'd': 1, 'y': 2, 's': 2, 'r': 4, 'n': 1, 'p': 2, ' ': 6}
'''

sorting = w.sort_simbols(counter)
print(sorting)
print()

'''
Результат работы метода класса для сортировки элементов по значению по возврастанию:

deque([('4', 1), ('3', 1), ('+', 1), ('d', 1), ('n', 1), ('e', 2), ('i', 2), 
('b', 2), ('R', 2), ('P', 2), ('B', 2), ('y', 2), ('s', 2), ('p', 2), ('a', 3), 
('r', 4), (' ', 6)])
'''

wood = w.making_wood(sorting)
print(wood)
print()

'''
Результат работы метода класса, который построил дерево

{0: {0: {0: 'r', 1: ' '}, 1: {0: {0: {0: {0: {0: '4', 1: '3'}, 1: '+'}, 1: 'd'}, 
1: 'n'}, 1: 'e'}}, 1: {0: {0: {0: {0: 'i', 1: 'b'}, 1: 'R'}, 1: 'P'}, 
1: {0: {0: {0: {0: 'B', 1: 'y'}, 1: 's'}, 1: 'p'}, 1: 'a'}}}
'''

haff_codding(wood)
print(table)
print()

'''
Результат работы функции, которая работая рекурсивно закодировала символы 
алгоритмом Хаффмана

{'r': '000', ' ': '001', '4': '0100000', '3': '0100001', '+': '010001', 
'd': '01001', 'n': '0101', 'e': '011', 'i': '10000', 'b': '10001', 'R': '1001', 
'P': '101', 'B': '110000', 'y': '110001', 's': '11001', 'p': '1101', 'a': '111'}
'''

code_str = str()

for i in string:
    code_str += f'{table.get(i)} '
print(code_str[:-1])

'''
Выводим все зашифрованные символы

1001 111 11001 1101 10001 011 000 000 110001 001 101 10000 001 0100000 110000
 001 111 0101 01001 001 1001 111 11001 1101 10001 011 000 000 110001 001 101
 10000 001 0100001 110000 010001
'''
