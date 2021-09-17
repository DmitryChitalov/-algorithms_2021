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


def haffman_tree(str_obj):
    count_str = list(Counter.most_common(Counter(str_obj)))
    count_str.reverse()
    try:
        while count_str[1]:
            count_str[0] = (Tree(count_str[0][0], count_str[1][0]), count_str[0][1] + count_str[1][1])
            count_str.pop(1)
            for i in range(1, len(count_str)):
                if count_str[0][1] > count_str[i][1]:
                    continue
                else:
                    count_str.insert(i, count_str[0])
                    count_str.pop(0)
                    break
            else:
                count_str.append(count_str[0])
                count_str.pop(0)
    except:
        return count_str[0][0]


code_table = {}


def haffman_code(tree, path=''):
    if type(tree.get_left()) != Tree and type(tree.get_right()) != HaffmanTree:
        code_table[tree.get_left()] = f'{path}0'
        code_table[tree.get_right()] = f'{path}1'
    elif type(tree.get_left()) != Tree:
        code_table[tree.get_left()] = f'{path}0'
        haffman_code(tree.get_right(), path=f'{path}1')
    elif type(tree.get_right()) != Tree:
        code_table[tree.get_right()] = f'{path}1'
        haffman_code(tree.get_left(), path=f'{path}0')
    else:
        haffman_code(tree.get_left(), path=f'{path}0')
        haffman_code(tree.get_right(), path=f'{path}1')


class Tree():
    def __init__(self, left_child, right_child):
        self.root = '.'
        self.left_child = left_child
        self.right_child = right_child

    def get_root(self):
        return self.root

    def get_left(self):
        return self.left_child

    def get_right(self):
        return self.right_child


test_string = 'beep boop beer!'
haffman_code(haffman_tree(test_string))

print(code_table)

for el in test_string:
    print(code_table[el], end=' ')
print()

# Отказ от дека, добавление класса дерева, конечные элементы (зашифрованные символы)
# не являются экземплярами класса дерева, на этом построен принцип проверок в функции кодировки 