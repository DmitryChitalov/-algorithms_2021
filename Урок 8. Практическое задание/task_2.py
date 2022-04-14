"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class NodeValueError(Exception):
    def __init__(self, body):
        self.body = body


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
                raise NodeValueError('Ошибка: значение левого узла больше значения корня.')
        except NodeValueError:
            return 'Ошибка: значение левого узла больше значения корня.'
        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            try:
                if new_node >= self.get_left_child().get_root_val():
                    raise NodeValueError('Ошибка: значение левого узла больше значения родительского узла.')
            except NodeValueError:
                return 'Ошибка: значение левого узла больше значения родительского узла.'
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if new_node <= self.root:
                raise NodeValueError('Ошибка: значение правого узла меньше значения корня.')
        except NodeValueError:
            return 'Ошибка: значение правого узла меньше значения корня.'
        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            try:
                if new_node <= self.get_right_child().get_root_val():
                    raise NodeValueError('Ошибка: значение правого узла меньше значения родительского узла.')
            except NodeValueError:
                return 'Ошибка: значение правого узла меньше значения родительского узла.'
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


bin_tree = BinaryTree(8)
print(bin_tree.get_root_val())
print(bin_tree.get_left_child())
bin_tree.insert_left(4)
print(bin_tree.get_left_child().get_root_val())
print(bin_tree.insert_left(40))
print(bin_tree.get_left_child())
print(bin_tree.get_left_child().get_root_val())
bin_tree.insert_right(12)
print(bin_tree.insert_left(7))
print(bin_tree.get_left_child())
print(bin_tree.get_left_child().get_root_val())
print(bin_tree.insert_right(7))
print(bin_tree.get_right_child())
print(bin_tree.insert_right(12))
print(bin_tree.insert_right(11))
print(bin_tree.get_right_child())
print(bin_tree.get_right_child().get_root_val())
bin_tree.get_right_child().set_root_val(16)
print(bin_tree.get_right_child().set_root_val(16))
print(bin_tree.get_right_child().get_root_val())