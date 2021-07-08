"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class BinaryTreeChildChecker(Exception):
    def __init__(self, txt):
        self.txt = txt


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        while True:
            try:
                if self.left_child == None and new_node < self.root:
                    self.left_child = BinaryTree(new_node)
                elif new_node < self.root:
                    tree_obj = BinaryTree(new_node)
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
                else:
                    raise BinaryTreeChildChecker("*** Ошибка! Левый потомок должен быть меньше родителя ***")
            except (ValueError, BinaryTreeChildChecker) as err:
                print(err)
                new_node = int(input(f'Введите число меньше {self.root}: '))
            else:
                break

    def insert_right(self, new_node):
        while True:
            try:
                if self.right_child == None and new_node > self.root:
                    self.right_child = BinaryTree(new_node)
                elif new_node > self.root:
                    tree_obj = BinaryTree(new_node)
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
                else:
                    raise BinaryTreeChildChecker("*** Ошибка! Правый потомок должен быть больше родителя ***")
            except (ValueError, BinaryTreeChildChecker) as err:
                print(err)
                new_node = int(input(f'Введите число больше {self.root}: '))
            else:
                break

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(40)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(6)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
