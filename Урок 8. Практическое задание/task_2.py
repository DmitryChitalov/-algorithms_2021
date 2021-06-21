"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

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
                raise ValueError("Ошибка\n")
        except ValueError as error:
            print(f"{error} Левый потомок {new_node} больше родителя {self.root}.")
        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if new_node < self.root:
                raise ValueError("Ошибка\n")
        except ValueError as error:
            print(f"{error} Правый потомок {new_node} меньше ролителя {self.root}.")
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
    @property
    def get_right_child(self):
        try:
            if self.right_child is None:
                raise Exception("Введите правого потомка")
            else:
                return self.right_child
        except Exception as error:
            print(f"{error}")

    # метод доступа к левому потомку
    @property
    def get_left_child(self):
        try:
            if self.left_child is None:
                raise Exception("Введите левого потомка")
            else:
                return self.left_child
        except Exception as error:
            print(f"{error}")

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    @property
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val)
r.insert_left(4)
print(r.get_left_child)
print(r.get_left_child.get_root_val)
r.insert_right(9)
print(r.get_right_child)
print(r.get_right_child.get_root_val)
r.get_right_child.set_root_val(12)
print(r.get_right_child.get_root_val)
