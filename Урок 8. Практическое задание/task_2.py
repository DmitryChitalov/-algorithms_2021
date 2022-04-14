
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
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            if self.right_child != None and self.left_child == None and self.left_child > self.right_child:
                raise print('err left')
            elif self.left_child == None:
                self.left_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        except:
            self.left_child = BinaryTree(new_node)
            self.left_child, self.right_child = self.right_child, self.left_child

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if self.right_child == None and self.left_child != None and self.left_child > self.right_child:
                raise print('err right')
            elif self.right_child == None:
                self.right_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
        except:
            self.right_child = BinaryTree(new_node)
            self.left_child, self.right_child = self.right_child, self.left_child

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


r = BinaryTree(8)
r.insert_left(40)
r.insert_right(12)
print('get left:', r.get_left_child().get_root_val())
print('get right:', r.get_right_child().get_root_val())
