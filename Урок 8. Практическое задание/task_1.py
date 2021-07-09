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


class Node:
    def __init__(self, left=None, right=None):
        self.left_child = left
        self.right_child = right


class HuffmanTree:

    def __init__(self, orig_str):
        self.orig_str = orig_str
        self.__created_tree = None
        self.encoding_table = {}

    def __counter(self):
        frequency = Counter(self.orig_str)
        frequency_sort = deque(sorted(frequency.items(), key=lambda x: x[1]))
        return frequency_sort

    def __create_tree(self):
        frequency_sort = self.__counter()
        while len(frequency_sort) > 1:
            node_weight = frequency_sort[0][1] + frequency_sort[1][1]
            node = Node(frequency_sort.popleft()[0], frequency_sort.popleft()[0])
            for i, elem in enumerate(frequency_sort):
                if node_weight > elem[1]:
                    continue
                else:
                    frequency_sort.insert(i, (node, node_weight))
                    break
            else:
                frequency_sort.append((node, node_weight))
        self.created_tree = frequency_sort[0][0]

    def __create_code_table(self, tree, branch=''):
        if not isinstance(tree, Node):
            self.encoding_table[tree] = branch
        else:
            self.__create_code_table(tree.left_child, branch=f'{branch}0')
            self.__create_code_table(tree.right_child, branch=f'{branch}1')

    def encoding(self):
        self.__create_tree()
        self.__create_code_table(self.created_tree)
        encode_text = []
        for i in string:
            encode_text.append(self.encoding_table[i])
        return f'Вы получили зашифрованное сообщение {" ".join(encode_text)}'

    def decryption(self, text):
        decryption_string = ''
        self.__create_tree()
        self.__create_code_table(self.created_tree)
        text = str(text)
        symbols = text.split(' ')
        for sym in symbols:
            for key, val in self.encoding_table.items():
                if sym == val:
                    decryption_string = f'{decryption_string}{key}'
        return f'Сообщение расшифровано: {decryption_string}'


string = "beep boop beer!"
c = HuffmanTree(string)
print(c.encoding())
print(c.encoding_table)
print(c.decryption('00 11 11 101 010 00 011 011 101 010 00 11 11 1000 1001'))




