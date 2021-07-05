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
Для моего уровня знаний (первая четверть GB) задача является
сложной(непостижимой) для самостоятельной реализации. Поэтому
разбирался на примере. Использовал подход ООП из одного примера реализации
алгоритма Хаффмана с сайта https://russianblogs.com/, разумеется
с моими доработками. Данный пример очень близок к моему пониманию,
а следовательно и к освоению материала"""

from collections import Counter


# class Phrase:
#     __init__(self, arr):
#     self.arr = arr


phrase = input('Input the phrase to coding:')
friq_arr = Counter(phrase)

class Node:
    def __init__(self, data=None, value=None):
        self.data = data
        self.value = value
        self.left = None
        self.right = None
    
class Tree:
    def __init__(self, char_weight):
        self.char_dict = {}
        self.leaf = [Node(k,v) for k, v in char_weight.items()]
        while len(self.leaf) != 1:
            self.leaf.sort(key=lambda node:node.value, reverse=True)
            n = Node(value=(self.leaf[-1].value + self.leaf[-2].value))
            n.left = self.leaf.pop(-1)
            n.right = self.leaf.pop(-1)
            self.leaf.append(n)
        self.root = self.leaf[0]
        self.buffer = list(range(10))
    def gen(self, tree, length):
        node = tree
        if not node:
            return
        elif node.data:
            print(node.data + ' ==> ', end='')
            for i in range(length):
                print(self.buffer[i], end='')
            print('')
            temp_val = ''.join(self.buffer[:length])
            self.char_dict.setdefault(node.data, temp_val)
            return
        self.buffer[length] = '0'
        self.gen(node.left, length + 1)
        self.buffer[length] = '1'
        self.gen(node.right, length + 1)
    def get_cod(self):
        self.gen(self.root, 0)

print('')
print(phrase)
tree = Tree(friq_arr)
tree.get_cod()
print('')
for i in phrase:
    print(tree.char_dict[i], end=' ')