"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class Node:
    def __init__(self, root_obj):
        # корень
        self.root_obj = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def insert_node(self, root, element):
        if self.root is None:
            self.root = Node(element)
        else:
            if root is None:
                root = Node(element)
            elif root.root_obj < element:
                root.right_child = self.insert_node(root.right_child, element)
            elif root.root_obj > element:
                root.left_child = self.insert_node(root.left_child, element)
        return root

    def print_tree(self, root):
        if root is not None:
            print(root.root_obj)
            if root.left_child is not None:
                self.print_tree(root.left_child)
            if root.right_child is not None:
                self.print_tree(root.right_child)


b_tree = BinaryTree()
b_tree.insert_node(b_tree.root, 20)
b_tree.insert_node(b_tree.root, 25)
b_tree.insert_node(b_tree.root, 2)
b_tree.insert_node(b_tree.root, 3)
b_tree.insert_node(b_tree.root, 22)
b_tree.insert_node(b_tree.root, 23)
b_tree.insert_node(b_tree.root, 12)
b_tree.insert_node(b_tree.root, 4)
b_tree.insert_node(b_tree.root, 18)
b_tree.insert_node(b_tree.root, 17)
b_tree.insert_node(b_tree.root, 50)
b_tree.insert_node(b_tree.root, 1)
b_tree.insert_node(b_tree.root, 9)
b_tree.print_tree(b_tree.root)
