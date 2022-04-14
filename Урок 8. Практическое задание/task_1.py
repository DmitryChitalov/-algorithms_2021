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
    def __init__(self, string_in):
        self.string_in = str(string_in)
        self.code_table = dict()

    def huffman_tree(self):
        el_frequency = Counter(self.string_in)
        tree_compute = deque(sorted(el_frequency.items(), key=lambda item: item[1]))
        if len(tree_compute) != 1:
            while len(tree_compute) > 1:
                priority = tree_compute[0][1] + tree_compute[1][1]
                tree_node = {0: tree_compute.popleft()[0], 1: tree_compute.popleft()[0]}
                for index, arguments in enumerate(tree_compute):
                    if priority > arguments[1]:
                        continue
                    else:
                        tree_compute.insert(index, (tree_node, priority))
                        break
                else:
                    tree_compute.append((tree_node, priority))
        else:
            priority = tree_compute[0][1]
            tree_node = {0: tree_compute.popleft()[0], 1: None}
            tree_compute.append((tree_node, priority))
        return tree_compute[0][0]

    def huffman_code_table(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code_table[tree] = path
        else:
            self.huffman_code_table(tree[0], path=f'{path}0')
            self.huffman_code_table(tree[1], path=f'{path}1')
        return self.code_table

    def huffman_encoding(self):
        encoded_string = ''
        for i in self.string_in:
            encoded_string += self.code_table[i] + ' '
        return encoded_string

    def huffman_decoding(self):
        decoded_string = ''
        for item in self.huffman_encoding().split(' '):
            for key, value in self.code_table.items():
                if value == item:
                    decoded_string += key
        return decoded_string


a = HuffmanEncoder("beep boop beer!")
print(a.huffman_code_table(a.huffman_tree()))
print(a.huffman_encoding())
print(a.huffman_decoding())