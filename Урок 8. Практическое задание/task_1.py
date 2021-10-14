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


def generate(node, code=''):
    if not node:
        return
    elif node.name is not None:
        print(f'Кодировка символа "{node.name}" по Хаффману: {code}\n')
        return
    generate(node.left, code + '0')
    generate(node.right, code + '1')


class Node:
    def __init__(self, name=None, value=None):
        self.name = name
        self.value = value
        self.left = None
        self.right = None


class HuffmanTree:
    def __init__(self, s):
        count = Counter(s)
        print(count)
        branch = deque([Node(k, v) for k, v in count.items()])
        while len(branch) > 1:
            n = Node(value=(branch[-1].value + branch[-2].value))
            n.left = branch.pop()
            n.right = branch.pop()
            for i in range(len(branch)):
                if n.value < branch[i].value:
                    continue
                else:
                    branch.insert(i, n)
                    break
            else:
                branch.append(n)
        self.root = branch[0]

    def gen_code(self):
        generate(self.root)


obj_1 = HuffmanTree("beep boop beer!")
obj_1.gen_code()
obj_2 = HuffmanTree('111112222333445')
obj_2.gen_code()
