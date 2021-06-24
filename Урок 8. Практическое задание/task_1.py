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
from collections import OrderedDict


class OwnError (Exception):
    def __init__(self, txt):
        self.txt = txt


class BinaryTree:
    def __init__(self, root_obj='root', weight=0):
        # корень
        self.root = root_obj
        self.weight = weight
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node, path):

        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            print(f'Левая ветка у {self.get_root_val()} отсутствует, элемент {new_node} установлен его код {path}')
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            if self.left_child.get_root_val() < new_node:
                # тогда вставляем новый узел
                print(f'Левая ветка существует. Ее голова = {self.left_child} '
                      f'меньше {new_node}, поэтому вставляем выше')
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
            else:
                self.left_child.insert_auto(new_node, path)



    # добавить правого потомка
    def insert_right(self, new_node, path):
        # если у узла нет правого потомка
        if self.right_child == None:
            print(f'Правая ветка у {self.get_root_val()} отсутствует, элемент {new_node} установлен его код {path}')
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            if self.right_child.get_root_val() <= new_node:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
            else:
                self.right_child.insert_auto(new_node, path)


    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    def get_root_weight(self):
        return self.weight

    def set_root_weight(self, weight):
        self.root = weight


    def insert_auto(self, element, path=''):
        if not self or element.weight < self.get_root_weight():
            self.insert_left(element, f'{path}0')
        else:
            self.insert_right(element, f'{path}1')

    def get_tree(self, path='', code_table={}):

        if not (self.left_child or self.right_child):
            print('тупик')
            code_table[self.get_root_val()] = path
            print(path, code_table)
        else:
            code_table[self.get_root_val()] = path
            if self.left_child:
                print('ушли налево')
                self.left_child.get_tree(f'{path}0', code_table)
            if self.right_child:
                print('ушли направо')
                self.right_child.get_tree(f'{path}1', code_table)
        return code_table




s = "beep boop beer!"
count = Counter(s)
freq_list = sorted(count.items(), key=lambda x: x[1], reverse=True)
haffman_tree = BinaryTree()
# while len(freq_list) > 1:
min_1 = freq_list.pop()
min_2 = freq_list.pop()
haffman_tree.set_root_weight(min_1[1] + min_2[1])
haffman_tree.insert_auto(min_1[0])
haffman_tree.insert_right(min_2[0])
min_union = (haffman_tree, haffman_tree.weight)
freq_list.append(min_union)
freq_list = sorted(count.items(), key=lambda x: x[1], reverse=True)
# haffman_tree = BinaryTree(0)
# for item, value in count.items():
#
#
print(freq_list)

