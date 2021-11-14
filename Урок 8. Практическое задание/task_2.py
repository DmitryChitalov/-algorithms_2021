"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class UserRaise(Exception):
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
            # если у узла нет левого потомка
            if self.left_child == None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(new_node)

            elif new_node > self.left_child.get_root_val():
                raise UserRaise(f'Внимание: {new_node} не может быть вставленно, так'
                                f' как больше текущей вершины - {self.left_child.get_root_val()}')

            # если у узла есть левый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj

        except UserRaise as error:
            print(error)

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            # если у узла нет правого потомка
            if self.right_child == None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.right_child = BinaryTree(new_node)
            # если у узла есть правый потомок

            elif new_node < self.right_child.get_root_val():
                raise UserRaise(f'Внимание: {new_node} не может быть вставленно, так'
                                f' как меньше текущей вершины - {self.right_child.get_root_val()}')

            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj

        except UserRaise as error:
            print(error)

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


r = BinaryTree(15)
print("значение корня - ", r.get_root_val())
print(r.get_left_child())
r.insert_left(12)    # добавим значение левого потомка
r.insert_left(18)    # не добавиться - больше предыдущего
print(r.get_left_child())
print("значение левого потомка - ", r.get_left_child().get_root_val())
r.insert_right(17)    # добавим значение правого потомка
r.insert_right(10)    # не добавиться - меньше предыдущего
print(r.get_right_child())
print("значение левого потомка - ", r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)    # вставка правого потомка (предыдущий сдвинется вниз)
print(r.get_right_child().get_root_val())
