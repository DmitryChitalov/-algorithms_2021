"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

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

    def __contains__(self, item) -> bool:
        if self.find(item) is not None:
            return True

        return False

    def find(self, item):
        def find_in_tree(tree: BinaryTree, node):
            if node == tree.root:
                return None, tree
            if node > tree.root and tree.right_child is not None:
                if node == tree.right_child.root:
                    return tree.root, tree.right_child
                else:
                    return find_in_tree(tree.right_child, node)
            elif node < tree.root and tree.left_child is not None:
                if node == tree.left_child.root:
                    return tree.root, tree.left_child
                else:
                    return find_in_tree(tree.left_child, node)
            else:
                return None

        return find_in_tree(self, item)

    # добавить левого потомка
    def insert_left(self, new_node):
        if new_node > self.root:
            self.insert_right(new_node)
            return
        if new_node == self.root:
            return
        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            if new_node == self.left_child.root:
                return
            # тогда вставляем новый узел
            elif new_node > self.left_child.root:
                self.left_child.insert_right(new_node)
            else:
                self.left_child.insert_left(new_node)
            # tree_obj = BinaryTree(new_node)
            # # и спускаем имеющегося потомка на один уровень ниже
            # tree_obj.left_child = self.left_child
            # self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node < self.root:
            self.insert_left(new_node)
            return
        if new_node == self.root:
            return
        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            if new_node == self.right_child.root:
                return
            elif new_node > self.right_child.root:
                self.right_child.insert_right(new_node)
            else:
                self.right_child.insert_left(new_node)
            # # тогда вставляем новый узел
            # tree_obj = BinaryTree(new_node)
            # # и спускаем имеющегося потомка на один уровень ниже
            # tree_obj.right_child = self.right_child
            # self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child if self.right_child is not None else None

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child if self.left_child is not None else None

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root if self.root is not None else None


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(40)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
