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


class BinaryTree:
    def __init__(self, root_obj='root', weight=0):
        # корень
        self.root = root_obj
        self.weight = weight
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def get_full_tree(self, path='', code_table={}):
        if isinstance(self.left_child, BinaryTree):
            self.left_child.get_full_tree(f'{path}0', code_table)
        else:
            code_table[self.left_child] = f'{path}0'
        if isinstance(self.right_child, BinaryTree):
            self.right_child.get_full_tree(f'{path}1', code_table)
        else:
            code_table[self.right_child] = f'{path}1'
        return code_table


def get_tree(left, right):
    tree = BinaryTree(weight=left[1]+right[1])
    tree.left_child = left[0]
    tree.right_child = right[0]
    return tree


s = input("Введите строку: ")  #"beep boop beer!"
print(f'Строка для кодирования: {s}')
count = Counter(s)
freq_list = sorted(count.items(), key=lambda x: x[1], reverse=True)
print(f'частотный словарь {freq_list}')
while len(freq_list) > 1:
    min_1 = freq_list.pop()
    min_2 = freq_list.pop()
    tree = get_tree(min_1, min_2)
    min_union = (tree, tree.weight)
    freq_list.append(min_union)
    freq_list = sorted(freq_list, key=lambda x: x[1], reverse=True)

code_table = freq_list[0][0].get_full_tree()
print(f'Таблица кодов {code_table}')
print('Шифровка: ', " ".join(list(map(lambda x: code_table[x], s))))
