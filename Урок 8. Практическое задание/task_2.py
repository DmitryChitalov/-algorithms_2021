"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class BinaryTree:
    __slots__ = ["root", "left_child", "right_child"]

    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def get_right_child(self):  # метод доступа вправо
        return self.right_child

    def get_left_child(self):  # метод доступа влево
        return self.left_child

    def set_root_val(self, obj):  # корень
        self.root = obj

    def get_root_val(self):  # метод доступа к корню
        return self.root

    def insert_left(self, new_node):
        if new_node > self.root:
            print(f'{new_node} больше корня и будет добавлен вправо')
            self.insert_right(new_node)
        else:
            if self.left_child is None:
                self.left_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj

    def insert_right(self, new_node):
        if new_node < self.root:
            print(f'{new_node} меньше корня и будет добавлен влево')
            self.insert_left(new_node)
        else:
            if self.right_child is None:
                self.right_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj


tree = BinaryTree(8)

print(tree.get_root_val())
print(tree.get_left_child())
tree.insert_left(40)
print(tree.get_left_child())
print(tree.get_right_child())
print(tree.get_right_child().get_root_val())
tree.insert_right(6)
print(tree.get_right_child())

del tree

