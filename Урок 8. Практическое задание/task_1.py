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


class HuffmanAlg:
    def __init__(self, string_arg):
        self.string = string_arg
        self.tree = self.get_tree()
        self.code_dict = dict()
        self.get_symbols_code(self.tree)
        self.code = self.get_code()

    def get_tree(self):
        tree = deque(sorted(Counter(self.string).items(), key=lambda item: item[1]))
        if len(tree) == 0:
            return None
        elif len(tree) == 1:
            return deque([({0: tree[0][0], 1: None}, tree[0][1])])[0][0]
        while len(tree) > 1:
            weight = tree[0][1] + tree[1][1]
            new_item = {0: tree[0][0], 1: tree[1][0]}
            for i, node in enumerate(tree):
                if weight > node[1]:
                    continue
                else:
                    tree.insert(i, (new_item, weight))
                    tree.popleft()
                    tree.popleft()
                    break
            else:
                tree.append((new_item, weight))
                tree.popleft()
                tree.popleft()
        return tree[0][0]

    def get_symbols_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.code_dict[tree] = path
        else:
            self.get_symbols_code(tree[0], path=f'{path}0')
            self.get_symbols_code(tree[1], path=f'{path}1')

    def get_code(self):
        code = ''
        for i in self.string:
            code = f"{code}{self.code_dict[i]}"
        return code


h_1 = HuffmanAlg('aa')
h_2 = HuffmanAlg('beep boop beer!')

print(h_1.code)
print(h_2.code)


'''
00
0011111010100001101110101000111110001001
'''
