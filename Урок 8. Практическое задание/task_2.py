"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class BiTree(Exception):
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

    # добавить левого потомка
    def insert_left(self, node):
        try:
            if node >= self.root:
                raise BiTree("Потомок больше или равен root")
        except BiTree as rt_b:
            print(rt_b)
        else:
            # если у узла нет левого потомка
            if self.left_child is None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(node)

            # если у узла есть левый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if new_node < self.root:
                raise BiTree("Потомок меньше root")
        except BiTree as rt_b:
            print(rt_b)
        else:
            # если у узла нет правого потомка
            if self.right_child is None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.right_child = BinaryTree(new_node)
            # если у узла есть правый потомок
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


root_b = BinaryTree(8)
print(root_b.get_root_val())
print(root_b.get_left_child())
root_b.insert_left(5)
root_b.insert_left(8)
print(root_b.get_left_child())
print(root_b.get_left_child().get_root_val())
root_b.insert_right(6)
root_b.insert_right(11)
print(root_b.get_right_child())
print(root_b.get_right_child().get_root_val())
root_b.get_right_child().set_root_val(16)
print(root_b.get_right_child().get_root_val())
