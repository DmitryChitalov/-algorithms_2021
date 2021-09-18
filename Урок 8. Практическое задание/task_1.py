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

from collections import Counter, deque


class HuffmanEncoder:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def huffman_tree(self):
    count = Counter(self)
    sorted_elem = deque(sorted(count.items(), key=lambda item: item[1]))
    del count
    if len(sorted_elem) != 1:
        while len(sorted_elem) > 1:
            weight = sorted_elem[0][1] + sorted_elem[1][1]
            new_node = HuffmanEncoder(left=sorted_elem.popleft()[0],
                            right=sorted_elem.popleft()[0])
            for i, amount in enumerate(sorted_elem):
                if weight > amount[1]:
                    continue
                else:
                    sorted_elem.insert(i, (new_node, weight))
                    break
            else:
                sorted_elem.append((new_node, weight))
    else:
        weight = sorted_elem[0][1]
        new_node = HuffmanEncoder(left=sorted_elem.popleft()[0])
        sorted_elem.append((new_node, weight))
    return sorted_elem[0][0]


code_table = dict()


def huffman_encoding(tree, code=''):
    if not isinstance(tree, HuffmanEncoder):
        code_table[tree] = code
    else:
        huffman_encoding(tree.left, code=f'{code}0')
        huffman_encoding(tree.right, code=f'{code}1')


string = "beep boop beer!"

huffman_encoding(huffman_tree(string))
print(code_table)
for i in string:
    print(code_table[i], end=' ')
