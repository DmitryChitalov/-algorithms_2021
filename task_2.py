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
                raise ValueError
        except ValueError:
            print(f'Ошибка! Значение {new_node} больше корня {self.root}, необходимо вставлять в правую часть дереева')
            exit('выход')
        # если у узла нет левого потомка
        if self.left_child == None:
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
        try:
            if new_node < self.root:
                raise ValueError
        except ValueError:
            print(f'Ошибка! Значение {new_node} меньше корня {self.root}, необходимо вставлять в левую часть дереева')
            exit('выход')
        # если у узла нет правого потомка
        if self.right_child == None:
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


r = BinaryTree(18)
print('root: ',r.get_root_val())
#print(r.get_left_child())
r.insert_left(4)
#print(r.get_left_child())
print('tree-left: ', r.get_left_child().get_root_val())
r.insert_right(120)
#print(r.get_right_child())
print('tree-right: ',r.get_right_child().get_root_val())
r.get_right_child().set_root_val(1)
#print(r.get_right_child().get_root_val())
r.insert_left(3)
print('tree-left-left: ', r.get_left_child().get_root_val())
r.insert_left(4)
print('tree-left-right: ', r.get_left_child().get_root_val())
r.insert_right(140)
print('tree-right-right: ',r.get_right_child().get_root_val())
r.insert_right(100)
print('tree-right-left: ',r.get_right_child().get_root_val())
# r.insert_right(14)
# print('tree-right-right: ',r.get_right_child().get_root_val()) #error
r.insert_left(100)
print('tree-right-left: ',r.get_left_child().get_root_val()) #error
