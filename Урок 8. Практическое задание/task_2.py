"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class NumberError(Exception):
    def __init__(self, text, num):
        self.txt = text
        self.n = num


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
            if self.root >= new_node:
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
            else:
                raise NumberError('Value error', new_node)
        except NumberError:
            print('Value error variable > node or root')


    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if self.root <= new_node:
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
            else:
                raise NumberError('Value error', new_node)
        except NumberError:
            print('Value error variable < node or root')


    # метод доступа к правому потомку
    def get_right_child(self):
        try:
            return self.right_child
        except AttributeError:
            print('No Attribute or AttributeError')

    # метод доступа к левому потомку
    def get_left_child(self):
        try:
            return self.left_child
        except AttributeError:
            print('No Attribute or AttributeError')

    # метод установки корня
    def set_root_val(self, obj):
        try:
            self.root = obj
        except AttributeError:
            print('Root error')

    # метод доступа к корню
    def get_root_val(self):
        try:
            return self.root
        except AttributeError:
            print('root error')


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


"""
Сделал как на уроке, но не понимаю, почему у меня после добавления exeptionов стала вываливаться ошибка.
Хотя при первичном запуске ее не было? Просьба подсказать!!!


Traceback (most recent call last):
  File "Урок 8. Практическое задание\task_2.py", line 107, in <module>
    print(r.get_left_child().get_root_val())
AttributeError: 'NoneType' object has no attribute 'get_root_val'
"""

