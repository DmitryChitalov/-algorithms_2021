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


from collections import Counter


class Node:
    def __init__(self, left, right):
        self.left = left
        self.right = right
        self.value = left[1] + right[1]

    def __getitem__(self, item):
        result = [0, self.value]
        return result[item]


class HuffmanCode:
    def __init__(self, some_string):
        self.base_string = some_string
        self.table = sorted([(x, y) for x, y in Counter(self.base_string).items()], key=lambda x: x[1])
        self.tree = self.table[:]
        self.tree_is_created = False

    def __str__(self):
        if self.tree_is_created:
            code_table = {}

            def get_code(node, current=''):
                if node.left.__class__.__name__ == 'Node':
                    get_code(node.left, f'{current}0')
                else:
                    code_table[node.left[0]] = f'{current}0'
                if node.right.__class__.__name__ == 'Node':
                    get_code(node.right, f'{current}1')
                else:
                    code_table[node.right[0]] = f'{current}1'

            get_code(self.tree[0])
            return str(code_table)
        else:
            return 'дерево не создано!'

    def create_tree(self):
        while len(self.tree) > 2:
            self.insert_node(Node(self.tree.pop(0), self.tree.pop(0)))
        if len(self.tree) == 2:
            self.tree.append(Node(self.tree.pop(0), self.tree.pop(0)))
        self.tree_is_created = True

    def insert_node(self, node):
        c = 1
        if node.value <= self.tree[0][1]:
            self.tree.insert(0, node)
        elif node.value > self.tree[-1][1]:
            self.tree.append(node)
        else:
            for i in range(len(self.tree) - 1):
                if self.tree[i][1] < node.value <= self.tree[i + 1][1]:
                    self.tree.insert(i + 1, node)


huffman = HuffmanCode("beep boop beer!")
print(huffman)
print(f'таблица символов: {huffman.table}')

huffman.create_tree() # создаем дерево

print(f'дерево: {huffman.tree}')
print(huffman)