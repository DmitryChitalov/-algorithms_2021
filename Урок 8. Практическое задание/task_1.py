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
class tree:
    def __init__(self, root):
        self.root = root
        self.left = None
        self.right = None
"""

from collections import Counter, deque


class Tree:
    def __init__(self, int_str):
        self.int_str = int_str
        self.bin_code = dict()
        self.get_code(self.get_tree())

    def counter_str(self):
        return Counter(self.int_str)

    def sort_val(self):
        return deque(sorted(self.counter_str().items(), key=lambda item: item[1]))

    def get_tree(self):
        val = self.sort_val().copy()
        if len(val) != 1:
            while len(val) > 1:
                mass = val[0][1] + val[1][1]
                join_elem = {0: val.popleft()[0],
                             1: val.popleft()[0]}
                for i, el in enumerate(val):
                    if mass > el[1]:
                        continue
                    else:
                        val.insert(i, (join_elem, mass))
                        break
                else:
                    val.append((join_elem, mass))
        else:
            mass = val[0][1]
            join_elem = {0: val.popleft()[0], 1: None}
            val.append((join_elem, mass))
        return val[0][0]

    def get_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.bin_code[tree] = path
        else:
            self.get_code(tree[0], path=f'{path}0')
            self.get_code(tree[1], path=f'{path}1')

    def get_str_code(self):
        bin_str = ''
        for i in self.int_str:
            bin_str += self.bin_code[i]
        return bin_str


test_str = 'May the force be with you. Always!'
test_code = Tree(test_str)
print(f'Дерево:\n{test_code.get_tree()}')
print(f'\n')
print(f'Код:\n{test_code.bin_code}')
print(f'\n')
print(f'Бинарный код:\n{test_code.get_str_code()}')
