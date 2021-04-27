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

        # Проверяем, нет ли  нарушения в алгоритме построения бинарного дерева.
        # Для этого проверяем можем ли мы добавить новое знаение влево от узла
        if not (new_node < self.root):
            print(f'Вы добавляете значение {new_node} влево от значения узла {self.root}, но '
                  f'должны добавлять вправо!')
            return

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

        # Проверяем, нет ли нарушения в алгоритме построения бинарного дерева.
        # Для этого проверяем можем ли мы добавить новое значение вправо от узла
        if not (new_node > self.root):
            print(f'Вы добавляете значение {new_node} вправо от значения узла {self.root}, а '
                  f'должны добавлять влево.')
            return

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


r = BinaryTree(9)
print(f'root = {r.get_root_val()}')
r.insert_left(4)
print(f'(left <- root) = ({r.get_left_child().get_root_val()} <- {r.get_root_val()})')
r.insert_right(17)
print(f'(root -> right) = ({r.get_root_val()} -> {r.get_right_child().get_root_val()})')
r.get_left_child().insert_left(6)
r.get_left_child().insert_right(6)
print(f'(right <- left <- root) = ({r.get_left_child().get_right_child().get_root_val()} <- '
      f'{r.get_left_child().get_root_val()} <- {r.get_root_val()})')
