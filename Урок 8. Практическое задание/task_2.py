"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class BinarySearchTree:
    def __init__(self, root):
        self.root = TreeNode(root)

    def insert(self, value):
        self._insert(value, self.root)

    def _insert(self, value, curr_node):
        if curr_node.node <= value:
            if curr_node.get_right_child( ):
                self._insert(value, curr_node.right_child)
            else:
                curr_node.right_child = TreeNode(value)
        else:
            if curr_node.get_left_child( ):
                self._insert(value, curr_node.left_child)
            else:
                curr_node.left_child = TreeNode(value)

    def find(self, value):
        return self._find_val(value, self.root)

    def _find_val(self, value, curr_node):
        if curr_node is None:
            return None
        else:
            if curr_node.node < value:
                return self._find_val(value, curr_node.right_child)
            elif curr_node.node > value:
                return self._find_val(value, curr_node.left_child)
            else:
                return curr_node

    @property
    def get_root(self):
        return self.root


class TreeNode:
    def __init__(self, val, left_child=None, right_child=None):
        self.node = val
        self.left_child = left_child
        self.right_child = right_child

    def has_both_children(self):
        return self.left_child and self.right_child

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def __str__(self):
        return f'{self.node}'


tree = BinarySearchTree(8)
tree.insert(10)
tree.insert(12)
tree.insert(6)
tree.insert(7)

print(tree.get_root)
print(tree.get_root.right_child.node)
print(tree.get_root.left_child.node)
print(tree.find(12))
print(tree.find(100))

tree.insert(100)
print(tree.find(100))