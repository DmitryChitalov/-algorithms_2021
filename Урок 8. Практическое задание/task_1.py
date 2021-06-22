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


class HuffmanCoding:
    def __init__(self, string):
        self.string = str(string)
        self.cd_table = {}

    def get_count(self):
        return Counter(self.string)

    def sort_count(self):
        return deque(sorted(self.get_count().items(), key=lambda ls: ls[1]))

    def build_tree(self):
        tree = self.sort_count()
        if len(tree) != 1:
            while len(tree) > 1:
                weight = tree[0][1] + tree[1][1]
                new_elem = {0: tree.popleft()[0], 1: tree.popleft()[0]}
                for i, elem in enumerate(tree):
                    if weight > elem[1]:
                        continue
                    else:
                        tree.insert(i, (new_elem, weight))
                        break
                else:
                    tree.append((new_elem, weight))
        else:
            weight = tree[0][1]
            new_elem = {0: tree.popleft()[0], 1: None}
            tree.append((new_elem, weight))
        return tree[0][0]

    def huffman_code(self, tree, path=''):
        if isinstance(tree, dict):
            self.huffman_code(tree[0], path=f'{path}0')
            self.huffman_code(tree[1], path=f'{path}1')
        else:
            self.cd_table[tree] = path
        return self.cd_table

    def huffman_encoding(self):
        self.huffman_code(self.build_tree())
        return ' '.join(self.cd_table[i] for i in self.string)


test_string = input('Введите строку для кодирования: ')
print('Ваша строка', test_string)
print('Закодированная строка: ', HuffmanCoding(test_string).huffman_encoding())
