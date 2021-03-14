"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class MyError(Exception):
    def __init__(self, text):
        self.txt = text


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def insert_left(self, new_node):
        try:
            if new_node > self.root:
                raise MyError('Левый потомок не может быть больше корня')
        except MyError as mr:
            print(mr)
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    def insert_right(self, new_node):
        try:
            if new_node < self.root:
                raise MyError('Правый потомок не может быть меньше корня')
        except MyError as mr:
            print(mr)
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    def get_right_child(self):
        try:
            if self.right_child is None:
                raise MyError('Вы не ввели правого потомка')
            else:
                return self.right_child
        except MyError as mr:
            print(mr)

    def get_left_child(self):
        try:
            if self.left_child is None:
                raise MyError('Вы не ввели левого потомка')
            else:
                return self.left_child
        except MyError as mr:
            print(mr)

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        return self.root


r = BinaryTree(1222)
r.insert_right(1223)
r.insert_left(864)
print(r.get_left_child().get_root_val())
r.get_right_child().set_root_val(2938)
print(r.get_right_child().get_root_val())
r.get_left_child().set_root_val(1111)
print(r.get_left_child().get_root_val())
r.get_left_child().insert_right(1246)
print(r.get_left_child().get_right_child().get_root_val())
