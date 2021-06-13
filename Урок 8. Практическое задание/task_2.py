"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class UserClass(Exception):
    def __init__(self, text):
        self.text = text


class BinaryTree:
    cnt = 1

    def __init__(self, root_obj, left_child=None, right_child=None):
        self.root = root_obj
        self.left_child = left_child
        self.right_child = right_child

    # левый потомок
    def insert_left(self, new_node):
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        try:
            if new_node >= self.root:
                raise UserClass("Потомок справа не может быть меньше корня!")
        except UserClass as err:
            print(err)
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj
            if self.left_child is None:
                self.left_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
            self.cnt += 1

    # Правый потомок
    def insert_right(self, new_node):
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        try:
            if new_node < self.root:
                raise UserClass("Потомок слева не может быть не больше корня!")
        except UserClass as err:
            print(err)
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj
            if self.right_child is None:
                self.right_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
            self.cnt += 1

    # доступ к правому потомку
    def get_right_child(self):
        return self.right_child

    # доступ к левому потомку
    def get_left_child(self):
        return self.left_child

    # установка корня
    def set_root_val(self, obj):
        self.root = obj

    # доступ к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(10)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(30)
r.insert_left(6)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(22)
r.insert_left(5)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(28)
print(r.get_right_child().get_root_val())
r.get_left_child().insert_right(8)
r.get_left_child().insert_right(33)
print(r.get_left_child().get_right_child().get_root_val())
r.get_left_child().get_right_child().insert_right(14)
r.get_left_child().get_right_child().insert_left(25)
print(r.get_left_child().get_right_child().get_right_child().get_root_val())
print(f"Всего узлов: {r.cnt}")
