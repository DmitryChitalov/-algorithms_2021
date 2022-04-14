"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class BinaryTreeInsertError(Exception):
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
        self.validate_insert(new_node, is_left_child=True)
        try:
            # если у узла нет левого потомка
            if self.left_child is None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(new_node)
            # если у узла есть левый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровеньr ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        except BinaryTreeInsertError as e:
            print(e)

    # добавить правого потомка
    def insert_right(self, new_node):
        self.validate_insert(new_node)
        try:
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
        except BinaryTreeInsertError as e:
            print(e)

    def auto_insert_node(self, node):
        if node < self.get_root_val():
            self.insert_left(node)
        else:
            self.insert_right(node)

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

    def validate_insert(self, node, is_left_child=False):
        if is_left_child:
            if node >= self.get_root_val():
                raise BinaryTreeInsertError('Вы пытаетесь в узел слева вставить неверное значение')
        else:
            if node < self.get_root_val():
                raise BinaryTreeInsertError('Вы пытаетесь в узел справа вставить неверное значение')


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(7)
r.insert_right(8)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
r.auto_insert_node(19)
r.auto_insert_node(2)
print(r.get_left_child().get_root_val())
print(r.get_right_child().get_root_val())
r.insert_right(1)
