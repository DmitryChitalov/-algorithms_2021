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
from collections import Counter, deque, OrderedDict


class HaffmanTree:
    __slots__ = ('res_code', 'trans_list', 'list_tree')

    def __init__(self, s):
        self.res_code = {}
        self.trans_list = Counter(s)
        self.list_tree = deque(sorted(self.trans_list.items(), key=lambda val: val[1]))

    def binary_tree(self):
        if len(self.list_tree) != 1:
            while len(self.list_tree) > 1:
                weight = self.list_tree[0][1] + self.list_tree[1][1]
                trans_dict = {0: self.list_tree.popleft()[0],
                              1: self.list_tree.popleft()[0]}
                for i, value in enumerate(self.list_tree):
                    if weight > value[1]:
                        continue
                    else:
                        self.list_tree.insert(i, (trans_dict, weight))
                        break
                else:
                    self.list_tree.append((trans_dict, weight))
        else:
            trans_dict = {0: self.list_tree[0][0]}
            return trans_dict
        return self.list_tree[0][0]

    def haffman_result(self, tree, path=""):
        if not isinstance(tree, dict):
            self.res_code[tree] = path
        else:
            self.haffman_result(tree[0], '%s0' % (path))
            self.haffman_result(tree[1], '%s1' % (path))

    def table_code(self):
        for i in self.res_code.items():
            yield i


s = "beep boop beer!"
# start = HaffmanTree(s)
# tree = start.binary_tree()
# print(tree)
# start.haffman_result(tree)
# print(start.res_code)
# # print(list(start.table_code()))
# for value in start.table_code():
#     print(*value)







class HaffmanTreeTwo:
    __slots__ = ('trans_dict', 'res_list')

    def __init__(self, s):
        self.trans_dict = OrderedDict()
        for i in s:
            if i not in self.trans_dict.keys():
                self.trans_dict[i] = 1
            else:
                self.trans_dict[i] += 1
        self.res_list = sorted(self.trans_dict.items(), key=lambda val: val[1])

    def binary_tree(self):
        while len(self.res_list) > 1:
            weight = self.res_list[0][1] + self.res_list[1][1]
            trans_dict = {0: self.res_list.pop(0)[0], 1: self.res_list.pop(0)[0]}
            for i, value in enumerate(self.res_list):
                if weight > value[1]:
                    continue
                else:
                    self.res_list.insert(i, (trans_dict, weight))
                    break
            else:
                self.res_list.append((trans_dict, weight))
        return self.res_list[0][0]

    def haffman_code(self, tree, path=""):
        if not isinstance(tree, dict):
            self.trans_dict[tree] = path
        else:
            self.haffman_code(tree[0], '%s0'%(path))
            self.haffman_code(tree[1], '%s1'%(path))

    def table_code(self):
        for value in self.trans_dict.items():
            yield value


start = HaffmanTreeTwo(s)
tree = start.binary_tree()
print(tree)
start.haffman_code(tree)
for i in start.table_code():
    print(*i)