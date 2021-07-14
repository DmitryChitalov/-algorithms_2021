"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


# валидация значений узлов в соответствии с требованиями для бинарного дерева



class MyError (Exception):
    def __init__(self, txt):
        self.txt = txt


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
            if self.root < new_node:
                raise MyError(f"Левый потомок не может быть больше родителя")
            if self.left_child is None:
                self.left_child = BinaryTree(new_node)
            else:
                if self.left_child.get_root_val() < new_node:
                    tree_obj = BinaryTree(new_node)
                    tree_obj.left_child = self.left_child
                else:
                    raise MyError(f"Левый потомок существует, предлагаемый root меньше допустимого")
        except MyError as err:
            print(err)

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if self.root > new_node:
                raise MyError(f"Правый потомок не может быть меньше родителя")
            if self.right_child is None:
                self.right_child = BinaryTree(new_node)
            else:
                if self.right_child.get_root_val() < new_node:
                    tree_obj = BinaryTree(new_node)
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
                else:
                    raise MyError(f"Правый потомок существует, предлагаемый root меньше допустимого")
        except MyError as err:
            print(err)

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj=None):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
r.set_root_val(10)
print(r.get_left_child())
r.insert_left(7)
print(r.get_left_child())
r.insert_left(40)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
r.insert_left(45)
print(r.get_left_child())
r.insert_right(6)
print(r.get_right_child().get_root_val())

"""Пытался сочинить функцию для генерации полноценной строки, но понял, что сейчас это выше моих сил.
Возможно в другой раз."""
