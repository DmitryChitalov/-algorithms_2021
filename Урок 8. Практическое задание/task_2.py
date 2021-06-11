"""
Задание 2.
Доработайте пример структуры "дерево",
рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).
Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""

class RootValueError(Exception):
    def __init__(self, text):
        self.txt = text

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
        # если у узла нет левого потомка
        try:
            if int(new_node) >= int(self.root):
                raise RootValueError('Значение левого узла больше корня')
        except RootValueError:
            return f'Значение левого узла больше корня'
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            try:
                if int(new_node) >= self.get_left_child().get_root_val():
                    raise RootValueError('Значение больше родительского узла')
            except RootValueError:
                return f'Значение больше родительского узла'
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        try:
            if int(new_node) <= int(self.root):
                raise RootValueError(f'Значение правого узла меньше корня')
        except RootValueError:
            return f'Значение правого узла меньше корня'
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            try:
                if int(new_node) <= self.get_right_child().get_root_val():
                    raise RootValueError(f'Значение меньше родительского узла')
            except RootValueError:
                return f'Значение меньше родительского узла'
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        if self.right_child is None:
            print(f'Правый узел отсутствует, при вызове будет выведено значение корня')
            return self
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        if self.left_child is None:
            print(f'Левый узел отсутствует, при вызове будет выведено значение корня')
            return self
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
print(r.get_left_child().get_root_val())
print(r.insert_left(40))
print(r.get_left_child())
print(r.get_left_child().get_root_val())
print(r.insert_left(7))
print(r.get_left_child())
print(r.get_left_child().get_root_val())
print(r.insert_right(7))
print(r.get_right_child())
print(r.insert_right(12))
print(r.insert_right(11))
print(r.get_right_child())
print(r.get_right_child().get_root_val())
print(r.get_right_child().set_root_val(16))
print(r.get_right_child().get_root_val())

