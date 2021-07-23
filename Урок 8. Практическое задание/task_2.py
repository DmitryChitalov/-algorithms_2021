"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class BinaryTree:
    def __init__(self, root_obj, parent=None):
        self.parent = parent   # добавим предка чтобы можно было подняться вверх по дереву
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка - сделаем приватным
    def _insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node, parent=self)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node, parent=self)
            # и спускаем имеющегося потомка на один уровень ниже
            if self.left_child.get_root_val() >= new_node:
                tree_obj.right_child = self.left_child
            else:
                tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка - сделаем тоже приватным
    def _insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node, parent=self)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node, parent=self)
            # и спускаем имеющегося потомка на один уровень ниже
            if self.right_child.get_root_val() >= new_node:
                tree_obj.right_child = self.right_child
            else:
                tree_obj.left_child = self.right_child
            self.right_child = tree_obj

    # добавить потомка с автоматическим определением верной стороны
    def insert(self, new_node: int):
        if not isinstance(new_node, int):
            print('Type error!')
            return None
        if new_node > self.root:
            self._insert_right(new_node)
        elif new_node < self.root:
            self._insert_left(new_node)
        else:
            print('')

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

    # метод определения узел или лист
    def is_node(self):
        if self.left_child is None and self.right_child is None:
            return False
        else:
            return True

    # метод нахождения уровня данного дерева в иерархии начиная с нуля у корня
    def get_tier(self, tier=0):
        if self.parent is None:
            return tier
        else:
            return self.parent.get_tier(tier + 1)

    # метод нахождения дерева-предка
    def get_parent(self):
        if self.parent is None:
            return None
        else:
            return id(self.parent)

    # метод выводит корень и потомков
    def show(self):
        print('ID:', id(self))
        print('Tier:', self.get_tier())
        print('Root:', self.get_root_val())
        if isinstance(self.get_left_child(), BinaryTree):
            print('Left child:', 'root:', self.get_left_child().get_root_val(), 'ID:', id(self.get_left_child()))
        else:
            print('Left child:', self.get_left_child())
        if isinstance(self.get_right_child(), BinaryTree):
            print('Right child:', 'root:', self.get_right_child().get_root_val(), 'ID:', id(self.get_right_child()))
        else:
            print('Right child:', self.get_right_child())
        print('Parent:', self.get_parent())
        print()


root_tree = BinaryTree(24)
root_tree.show()

root_tree.insert(10)
root_tree.show()
root_tree.get_left_child().show()

root_tree.insert(10)
root_tree.show()
root_tree.get_left_child().show()
root_tree.get_left_child().get_right_child().show()