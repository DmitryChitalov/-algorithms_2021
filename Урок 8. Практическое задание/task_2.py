"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if new_node > self.root:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            print('New left node should be less than root')
        # если у узла есть левый потомок
        elif self.left_child:
            self.left_child = BinaryTree(new_node)
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if new_node < self.root:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            print('New left node should be higher than root')
        # если у узла есть правый потомок
        elif self.right_child:
            self.right_child = BinaryTree(new_node)
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

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


r1 = BinaryTree(10)
r1.insert_left(8)
r1.insert_right(11)
print('===========')
print(r1.get_left_child().get_root_val())
print(r1.get_right_child().get_root_val())
r1.get_left_child().insert_left(9)
r1.get_right_child().insert_right(9)

'''
===========
8
11
New left node should be less than root
New left node should be higher than root
'''