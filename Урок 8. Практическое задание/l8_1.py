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

    def insert_number(self, new_node):
        if new_node < self.root:
            if self.left_child:
                if new_node < self.left_child.root:
                    self.left_child.insert_number(new_node)
                elif new_node > self.left_child.root:
                    new_tree = BinaryTree(new_node)
                    new_tree.left_child = self.left_child
                    self.left_child = new_tree
            else:
                self.left_child = BinaryTree(new_node)

        elif new_node > self.root:
            if self.right_child:
                if new_node > self.right_child.root:
                    self.right_child.insert_number(new_node)
                elif new_node < self.right_child.root:
                    new_tree = BinaryTree(new_node)
                    new_tree.right_child = self.right_child
                    self.right_child = new_tree
            else:
                self.right_child = BinaryTree(new_node)

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
r.insert_number(20)
r.insert_number(3)
r.insert_number(15)
r.insert_number(5)
