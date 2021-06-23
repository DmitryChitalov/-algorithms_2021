"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class RootError(Exception):
    def __init__(self, message):
        self.message = message


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
                raise RootError('Левый узел не может быть больше значения корня!')
        except RootError:
            print(f'Левый узел не может быть больше значения корня!')
            return
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            try:
                if int(new_node) >= self.get_left_child().get_root_val():
                    raise RootError('Левое значение не может быть больше родительского!')
            except RootError:
                print(f'Левое значение не может быть больше родительского!')
                return

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
                raise RootError('Правый узел не может быть меньше значения корня!')
        except RootError:
            print(f'Правый узел не может быть меньше значения корня!')
            return
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            try:
                if int(new_node) >= self.get_left_child().get_root_val():
                    raise RootError('Правое значение не может быть меньше родительского!')
            except RootError:
                print(f'Правое значение не может быть меньше родительского!')
                return
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


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(40)
print(r.get_left_child())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
r = BinaryTree(23)
print(f'Значение корня: {r.get_root_val()}')
print(f'Значение левого потомка: {r.get_left_child()}')
print(f'Значение правого потомка: {r.get_right_child()}')
r.insert_right(15)
r.insert_left(45)
print(f'Значение левого потомка: {r.get_left_child()}')
r.insert_left(6)
print(f'Значение корня левого потомка: {r.get_left_child().get_root_val()}')

r.insert_left(10)
print(f'Значение левого потомка: {r.get_left_child()}')
print(f'Значение корня левого потомка: {r.get_left_child().get_root_val()}')

r.insert_left(24)
r.insert_right(27)
print(f'Значение правого потомка: {r.get_right_child()}')
print(f'Значение корня правого потомка: {r.get_right_child().get_root_val()}')

r.insert_right(30)
print(f'Значение правого потомка: {r.get_right_child()}')
print(f'Значение корня правого потомка: {r.get_right_child().get_root_val()}')


print(f'Левый потомок: {r.get_left_child()}')
print(f'Значение корня левого потомка: {r.get_left_child().get_root_val()}')
