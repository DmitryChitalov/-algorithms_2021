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


class Binary:

    def __init__(self, lin):
        self.lin = Counter(lin).items()

    def sorting_list(self, lin):
        return deque(sorted(lin, key=lambda x: x[1]))

    def bin_tree(self):
        while len(self.lin) > 1:
            self.lin = self.sorting_list(self.lin)
            wei = self.lin[0][1] + self.lin[1][1]
            unity = {0: self.lin.popleft()[0], 1: self.lin.popleft()[0]}
            self.lin.append((unity, wei))
        self.lin = self.lin[0][0]
        return self.lin

    def bin_code(self):
        if not isinstance(self.lin, dict):
            return "Сюда слишком рано"
        self.table = {}
        self.bin_cod(self.lin)
        return self.table

    def bin_cod(self, lin, path=''):
        if not isinstance(lin, dict):
            self.table[lin] = path
        else:
            self.bin_cod(lin[0], f'{path}0')
            self.bin_cod(lin[1], f'{path}1')


bit = Binary("asgsagsdagwd asdsgerayhfhsjfs aaaaaaa ddddd ")
print(bit.bin_tree())
print(bit.bin_code())
