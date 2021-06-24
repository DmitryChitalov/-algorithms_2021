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
    __slots__ = ('left_branch', 'right_branch', 'value')

    def __init__(self, first_val, second_val):
        self.left_branch = first_val
        self.right_branch = second_val
        self.value = (first_val.value if isinstance(first_val, Node) else first_val[1]) + (
            second_val.value if isinstance(second_val, Node) else second_val[1])


class HaffmanTree:
    __slots__ = ('base_str', 'coded_symb', 'sort_tumple')

    def __init__(self, user_str):
        self.base_str = user_str
        self.coded_symb = {}
        self.code_str(self.haff_tree())

    def haff_tree(self):
        frequence = Counter(self.base_str)
        self.sort_tumple = sorted(frequence.items(), key=lambda x: x[1])
        del frequence
        while len(self.sort_tumple) > 1:
            node = Node(self.sort_tumple.pop(0), self.sort_tumple.pop(0))
            for ind, item in enumerate(self.sort_tumple):
                if node.value < item[1] or node.value == item[1]:
                    self.sort_tumple.insert(ind, (node, node.value))
                    break
            else:
                self.sort_tumple.append((node, node.value))
        return self.sort_tumple[0][0]

    def code_str(self, tree, code=''):
        if not isinstance(tree, Node):
            self.coded_symb[tree] = code

        else:
            self.code_str(tree=tree.left_branch[0], code=f'{code}0')
            self.code_str(tree=tree.right_branch[0], code=f'{code}1')

    def __str__(self):
        return f'{" ".join([self.coded_symb[char] for char in self.base_str])}'


user_str = "beep boop beer!"
code_str = HaffmanTree(user_str)
print(code_str)
