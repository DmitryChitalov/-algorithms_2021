"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""

class EmptyChild(Exception):
    def __init__(self, text):
        self.txt = text


class ErrInsertTree(EmptyChild):
    pass


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
            if new_node >= self.root:
                raise ErrInsertTree("Потомок больше или равен root")
        except ErrInsertTree as e:
            print(e)
        else:
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
            if new_node <= self.root:
                raise ErrInsertTree("Потомок меньше или равен root")
        except ErrInsertTree as e:
            print(e)
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
        try:
            if self.right_child is None:
                raise EmptyChild('Нет потомков справа.')
            return self.right_child
        except EmptyChild as e:
            print(e)

    # метод доступа к левому потомку
    def get_left_child(self):
        try:
            if self.left_child is None:
                raise EmptyChild('Нет потомков слева.')
            return self.left_child
        except EmptyChild as e:
            print(e)

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
r.get_left_child()  # -> Нет потомков слева.
r.get_right_child()  # -> Нет потомков слева.
r.insert_left(40)  # -> Потомок больше или равен root
r.insert_right(1)  # -> Потомок меньше или равен root
r.insert_left(7)
r.insert_right(10)
print(r.get_left_child())
print(r.get_left_child().get_root_val())  # -> 7
print(r.get_right_child())
print(r.get_right_child().get_root_val())  # -> 10
r.insert_right(15)
print(r.get_right_child().get_right_child().get_root_val())  # -> 10


"""
8
Нет потомков слева.
Нет потомков справа.
Потомок больше или равен root
Потомок меньше или равен root
<__main__.BinaryTree object at 0x000001E49AC2EF70>
7
<__main__.BinaryTree object at 0x000001E49AC2ED30>
10
10
"""