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
            if new_node > self.root:
                raise ValueError('Нарушающие требования бинарного дерева!')
        except ValueError as e:
            print(f'{e}\n'
                  f'Левый узел >{new_node}< больше корня >{self.root}<!')
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if new_node < self.root:
                raise ValueError('Нарушающие требования бинарного дерева!')
        except ValueError as e:
            print(f'{e}\n'
                  f'Правый узел >{new_node}< меньше корня >{self.root}<!')
        if self.right_child is None:
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
                raise Exception('Введите правого потомка')
            else:
                return self.right_child
        except Exception as e:
            print(e)

    # метод доступа к левому потомку
    def get_left_child(self):
        try:
            if self.left_child is None:
                raise Exception('Введите левого потомка')
            else:
                return self.left_child
        except Exception as e:
            print(e)

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
r.insert_left(4)
print(r.get_left_child())
# r.insert_left(40)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
# r.insert_right(1)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
