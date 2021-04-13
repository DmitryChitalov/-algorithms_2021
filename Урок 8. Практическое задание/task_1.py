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

import string, random
from collections import Counter, deque


def generate_random_string(length):
    """Генератор рандомной строки"""
    letters = string.ascii_lowercase
    rand_string = ''.join(random.choice(letters) for i in range(length))
    return rand_string


class Huffman:
    code_table = dict()

    def __init__(self, string):
        self.string = string
        count = Counter(self.string)
        tree = deque(sorted(count.items(), key=lambda item: item[1]))
        if len(tree) != 1:
            while len(tree) > 1:
                weight = tree[0][1] + tree[1][1]
                comb = {0: tree.popleft()[0],
                        1: tree.popleft()[0]}
                for i, _count in enumerate(tree):
                    if weight > _count[1]:
                        continue
                    else:
                        tree.insert(i, (comb, weight))
                        break
                else:
                    tree.append((comb, weight))
        else:
            weight = tree[0][1]
            comb = {0: tree.popleft()[0], 1: None}
            tree.append((comb, weight))
        self.ready_tree = tree[0][0]

    def __haffman_code(self, tree, path=''):

        if not isinstance(tree, dict):
            self.code_table[tree] = path
        else:
            self.__haffman_code(tree[0], path=f'{path}0')
            self.__haffman_code(tree[1], path=f'{path}1')

    def get_tree(self):
        return self.ready_tree

    def tree_encode(self):
        self.__haffman_code(self.ready_tree)
        return self.code_table


s = generate_random_string(15)
print(f'Строка: \n{s}\n')

huf = Huffman(s)

print(f'Дерево: \n{huf.get_tree()}\n')
print(f'Коды символов: \n{huf.tree_encode()}\n')

for i in s:
    print(huf.tree_encode()[i], end=' ')