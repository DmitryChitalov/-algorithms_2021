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

    def insert(self, new_node):
        """Добавление потомка
        (автоопределение в какую сторону определить значение без валидации)"""
        if new_node < self.root:
            self.insert_left(new_node)
        else:
            self.insert_right(new_node)

    # добавить левого потомка
    def insert_left(self, new_node):
        if new_node < self.root:
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
        else:
            print("Значение больше корня, используйте insert_right()")

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node > self.root:
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
        else:
            print("Значение меньше корня, используйте insert_left()")

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

    def show_node(self):
        """Вывести узел"""
        left = 'None' if self.left_child is None else str(self.left_child.get_root_val())
        right = 'None' if self.right_child is None else str(self.right_child.get_root_val())
        return f'{" " * len(left)}{self.root}\n' \
               f'{" " * (len(left) - 1)}/{" " * len(str(self.root))}\\\n'\
               f'{left}{" " * len(str(self.root))}{right}'


r = BinaryTree(8)
r.insert_left(158)
# Значение больше корня, используйте insert_right()
r.insert_right(3)
# Значение меньше корня, используйте insert_left()
r.insert(15)
print(r.show_node())
#     8
#    / \
# None 15
r.insert(3)
print(r.show_node())
#  8
# / \
# 3 15
r.left_child.insert(10)
print(r.left_child.show_node())
#     3
#    / \
# None 10
