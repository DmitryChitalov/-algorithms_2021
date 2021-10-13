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
from collections import Counter

line = input('Введите строку для кодирования: ')


def get_frequency(string):
    line_dict = Counter(string)
    line_deque = deque()
    itm = line_dict.items()
    for i in itm:
        line_deque.append(i)
    return line_deque


def get_tree(l_deque):
    if len(l_deque) > 1:
        for _ in range(len(l_deque) - 1):
            freq = l_deque[0][1] + l_deque[1][1]
            tree = {0: l_deque.popleft()[0], 1: l_deque.popleft()[0]}
            l_deque.appendleft((tree, freq))
            for i in range(len(l_deque) - 1):
                if freq > l_deque[i + 1][1]:
                    l_deque[i], l_deque[i + 1] = l_deque[i + 1], l_deque[i]
                else:
                    break
    else:
        tree = {0: l_deque[0][0], 1: None}
    return tree


code_dict = {}


def encoding(my_tree, code_str=''):
    if not isinstance(my_tree, dict):
        code_dict[my_tree] = code_str
    else:
        encoding(my_tree[0], code_str=code_str + '0')
        encoding(my_tree[1], code_str=code_str + '1')


encoding(get_tree(get_frequency(line)))
for i in line:
    print(code_dict[i], end=" ")
