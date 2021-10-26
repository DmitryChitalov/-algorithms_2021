"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class BinaryTree:
    __slots__ = ('root', 'left_child', 'right_child')

    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        if self.root < new_node:
            raise ValueError('You entered the wrong number, for the left branch, the root of this tree - %d' % (self.root))
        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            if self.left_child.get_root_val() > new_node:
                """ Это пригодится когда я буду делать волидацию для set_root_val()
                """
                raise ValueError(f'You entered a number less than the previous one {self.left_child.get_root_val()}')
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        if self.root > new_node:
            raise ValueError('You entered the wrong number, for the right branch, the root of this tree - %d' % (self.root))
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            if self.right_child.get_root_val() < new_node:
                """ Это пригодится когда я буду делать волидацию для set_root_val()
                """
                raise ValueError(f'You entered a number greater than the previous one {self.right_child.get_root_val()}')
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
        if self.left_child.get_root_val() < obj and self.right_child.get_root_val() > obj:
            self.root = obj
        else:
            raise ValueError(f'The root can be a number between {self.left_child.get_root_val() } - {self.right_child.get_root_val() }')

    # метод доступа к корню
    def get_root_val(self):
        return self.root


if __name__ == '__main__':
    try:
        r = BinaryTree(8)
        print(r.get_root_val())
        r.insert_left(5)
        print(r.get_left_child())
        print(r.get_left_child().get_root_val())
        r.insert_left(7)
        print(r.get_left_child().get_root_val())
        r.insert_right(15)
        print(r.get_right_child())
        print(r.get_right_child().get_root_val())
        r.insert_right(12)
        print(r.get_right_child().get_root_val())
        r.set_root_val(16)
        print(r.get_root_val())
    except ValueError as err:
        print(err)