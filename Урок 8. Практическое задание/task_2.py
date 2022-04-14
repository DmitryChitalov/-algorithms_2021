"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного
 дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на
клиентском коде.
"""


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def is_empty(self):
        return self.root == self.left_child == self.right_child is None

    # логичнее добавлять не влево и право самостоятельно, а делать это
    # програмно, т.е. при указании значения код должен сам анализировать и
    # вставлять значение в левого и правого потомка.
    def insert(self, root):
        try:
            if self.is_empty():
                self.root = root
                return
            elif root < self.root:
                if self.left_child is None:
                    self.left_child = BinaryTree(root)
                else:
                    tree_obj = BinaryTree(root)
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
            else:
                if self.right_child is None:
                    self.right_child = BinaryTree(root)
                else:
                    tree_obj = BinaryTree(root)
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
        except TypeError:   # Перехват ошибок по типу вводимого значения
            print('В данном бинароном дереве можно использовать только '
                  'целочисленные значения при вводе!!!')

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

    # печать всего дерева
    def __str__(self):
        return '[%s, %s, %s]' % (self.left_child, str(self.root),
                                 self.right_child)


my_tree = BinaryTree(8)
my_tree.insert(4)
my_tree.insert(15)
my_tree.insert(6)
my_tree.insert(9)
my_tree.insert(12)
my_tree.insert(7)
my_tree.insert(10)
my_tree.insert(1)
my_tree.insert("value")
print(my_tree.get_root_val())
print(my_tree.get_left_child())
print(my_tree.get_right_child())
print(my_tree)
