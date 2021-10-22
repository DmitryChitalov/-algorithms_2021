"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class MyRaise(Exception):
    def __init__(self, text):
        self.text = text


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        try:
            if new_node > self.root:
                print("число не может быть вставленно так как больше корня и будет вставленно в правую часть.")
                BinaryTree.insert_right(self, new_node)
            elif self.left_child is None:
                self.left_child = BinaryTree(new_node)
            elif new_node < self.left_child.get_root_val():
                raise MyRaise(f'Ошибка: число {new_node} не может быть вставленно выше вершины так'
                              f' как меньше текущей вершины {self.left_child.get_root_val()}')
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        except MyRaise as i:
            print(i)

    def insert_right(self, new_node):
        try:
            if new_node < self.root:
                print("число не может быть вставленно так как больше корня и будет вставленно в левую часть.")
                self.right_child = BinaryTree.insert_left(self, new_node)
            elif self.right_child is None:
                self.right_child = BinaryTree(new_node)
            elif new_node < self.right_child.get_root_val():
                raise MyRaise(f'Ошибка: число {new_node} не может быть вставленно выше вершины так'
                              f' как меньше текущей вершины {self.right_child.get_root_val()}')
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
        except MyRaise as i:
            print(i)

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


r = BinaryTree(8)
print(r.get_root_val())
r.insert_left(6)
r.insert_left(7)
r.insert_left(15)
r.insert_left(6)
r.insert_right(14)
r.insert_right(16)
r.insert_right(14)
r.insert_left(60)
r.insert_right(14)
