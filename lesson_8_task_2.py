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

        self.left_child = None
        self.right_child = None
        self.root = root_obj

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child is None and new_node < self.root:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        elif new_node < self.root:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj
        else:
            print(f' Невозможно вставить {new_node} в левый узел, значение подойдёт для правого узла')

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child is None and new_node >= self.root:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        elif new_node >= self.root:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj
        else:
            print(f' Невозможно вставить {new_node} в правый узел, значение подойдёт для левого узла')

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

    # напечатать дерево
    def PrintTree(self):
        if self.left_child:
            self.left_child.PrintTree()
        print(self.root),
        if self.right_child:
            self.right_child.PrintTree()


r = BinaryTree(8)
print(r.get_root_val())
r.insert_right(13)
r.insert_left(50)
r.insert_left(2)
r.insert_left(5)
r.insert_left(2)
r.insert_left(3)
print(r.get_left_child().get_root_val())
print(r.get_left_child())
r.insert_right(25)
r.insert_right(7)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
print('***' * 50)
r.PrintTree()

'''
Не смогла разобраться с моментом:
когда вставляется значение в левый узел впервые, оно меняется с корнем.
При послежующих вставках всё ок
'''