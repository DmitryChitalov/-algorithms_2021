"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

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
            if self.left_child is None and self.root > new_node:
                self.left_child = BinaryTree(new_node)
            elif self.root < new_node:
                raise ValueError('left child should be less than right!')
            else:
                self.left_child.insert(new_node)
        except ValueError as e:
            print(f'Error: {e}')

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if self.right_child is None and self.root < new_node:
                self.right_child = BinaryTree(new_node)
            elif self.root > new_node:
                raise ValueError('left child should be less than right!')
            else:
                self.right_child.insert(new_node)
        except ValueError as e:
            print(f'Error: {e}')

    def insert(self, new_node):
        if new_node < self.root:
            if self.left_child is None:
                self.left_child = BinaryTree(new_node)
            else:
                self.left_child.insert(new_node)
        elif new_node > self.root:
            if self.right_child is None:
                self.right_child = BinaryTree(new_node)
            else:
                self.right_child.insert(new_node)
        else:
            print('value already exists')

    # метод доступа к правому потомку
    def get_right_child(self):
        try:
            if self.right_child is None:
                raise AttributeError('!')
            else:
                return self.right_child, self.right_child.root
        except AttributeError as e:
            print(f'Node doesnt exists: {e}')

    # метод доступа к левому потомку
    def get_left_child(self):
        try:
            if self.left_child is None:
                raise AttributeError('!')
            else:
                return self.left_child, self.left_child.root
        except AttributeError as e:
            print(f'Node doesnt exists: {e}')

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        try:
            if self.left_root is None:
                raise AttributeError('!')
            else:
                return self.root
        except AttributeError as e:
            print(f'Node doesnt exists: {e}')


"""
Добавил метод автоматический метод вставки insert и валидацию значений узлов.
Если узел уже существует и валидация проходит успешно, вызывается insert для потомка"""

r = BinaryTree(8)
r.insert_left(10)
r.insert_left(5)
print(r.get_left_child())
r.insert_left(6)
print(r.left_child.get_right_child())
r.insert(1)
print(r.left_child.get_left_child())

