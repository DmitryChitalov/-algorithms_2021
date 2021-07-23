"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class PathError(Exception):
    def __str__(self):
        return "Для установки данного потомка размер значения не соответствует размеру корня или потомка.\n" \
               "Также проверьте тип (int?)."


class TreeValueError(Exception):
    def __str__(self):
        return "В данном бинарном дереве используются только значения типа int."


class BinaryTree:
    def __init__(self, root_obj):
        try:
            self.root = root_obj
            if type(root_obj) != int:
                raise TreeValueError
        except TreeValueError as error:
            print(error, 'Отмена установки корня.')
            return
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        try:
            if type(new_node) != int or new_node >= self.root:
                raise PathError
        except PathError as error:
            print(error, 'Отмена установки левого потомка.')
            return
        if self.left_child == None:
            self.left_child = BinaryTree(new_node)
        else:
            try:
                if new_node <= self.right_child.root:
                    raise PathError
            except PathError as error:
                print(error, 'Отмена установки левого потомка.')
                return
            tree_obj = BinaryTree(new_node)
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    def insert_right(self, new_node):
        try:
            if type(new_node) != int or new_node <= self.root:
                raise PathError
        except PathError as error:
            print(error, 'Отмена установки правого потомка.')
            return
        if self.right_child == None:
            self.right_child = BinaryTree(new_node)
        else:
            try:
                if new_node >= self.right_child.root:
                    raise PathError
            except PathError as error:
                print(error, 'Отмена установки правого потомка.')
                return
            tree_obj = BinaryTree(new_node)
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        try:
            if type(obj) != int:
                raise TreeValueError
        except TreeValueError as error:
            print(error, 'Отмена установки корня.')
            return
        self.root = obj

    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())  # 8
print(r.get_left_child())  # None
r.insert_left(4)
print(r.get_left_child())  # <__main__.BinaryTree object at 0x0000000000529640>
print(r.get_left_child().get_root_val())  # 4
r.insert_right(12)
print(r.get_right_child())  # <__main__.BinaryTree object at 0x0000000001E8E250>
print(r.get_right_child().get_root_val())  # 12
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())  # 16

# Установим правого потомка со сдвигом предыдущего
r.insert_right(15)
print(r.get_right_child().get_right_child())  # <__main__.BinaryTree object at 0x000000000258E250>
print(r.get_right_child().get_root_val())  # 15
# Проверим сдвиг предыдущего правого потомка
print(r.get_right_child().get_right_child().get_root_val())  # 16

# # Проверка валидаций:

# Попытка установки невалидного корня
# r2 = BinaryTree('d')      # В данном бинарном дереве используются только значения типа int. Отмена установки корня.

# Попытка установки правого потомка со значением меньшим, чем у корня
# r.insert_right(7)         # Для установки данного потомка размер значения не соответствует размеру корня или потомка.
#                           # Также проверьте тип (int?). Отмена установки правого потомка.

# Попытка установки правого потомка (со сдвигом вниз существующего) со значением большим, чем у существующего
# r.insert_right(17)        # Для установки данного потомка размер значения не соответствует размеру корня или потомка.
#                           # Также проверьте тип (int?). Отмена установки правого потомка.

# Попытка установки невалидного левого потомка
# r.insert_left('d')        # Для установки данного потомка размер значения не соответствует размеру корня или потомка.
#                           # Также проверьте тип (int?). Отмена установки левого потомка.
