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
        try:
            if new_node > self.root:
                raise ValueError("Ошибочка с данными Value\n")
        except ValueError as _error:
            print(f"{_error} Левый потомок {new_node} по значению >(больше) корня {self.root}. Надо исправить!")
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if new_node < self.root:
                raise ValueError("Ошибочка с данными Value\n")
        except ValueError as _error:
            print(f"{_error} Правый потомок {new_node} по значению <(меньше) корня {self.root}. Надо исправить!")
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    @property
    def get_right_child(self):
        try:
            if self.right_child is None:
                raise Exception("Просьба внести прав. потомка")
            else:
                return self.right_child
        except Exception as _error:
            print(f"{_error}")

    @property
    def get_left_child(self):
        try:
            if self.left_child is None:
                raise Exception("Просьба внести лев. потомка")
            else:
                return self.left_child
        except Exception as _error:
            print(f"{_error}")

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    @property
    def get_root_val(self):
        return self.root

    @property
    def get_maxheight(self):
        right_maxheight = self.right_child.get_maxheight if self.right_child else 0
        left_maxheight = self.left_child.get_maxheight if self.left_child else 0
        return max(left_maxheight, right_maxheight) + 1

r = BinaryTree(8)
print(r.get_root_val)
print(r.get_left_child)
r.insert_left(5)
print(r.get_left_child)
print(r.get_left_child.get_root_val)
r.insert_right(14)
print(r.get_right_child)
print(r.get_right_child.get_root_val)
r.get_right_child.set_root_val(16)
print(r.get_right_child.get_root_val)
