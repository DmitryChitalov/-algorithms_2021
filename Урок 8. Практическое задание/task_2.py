"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class TreeValueError(Exception):
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

        if int(new_node) >= int(self.root):
            raise TreeValueError('Значение левого узла больше корня')

        if self.left_child == None:
            # если у узла нет левого потомка
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:

            if int(new_node) >= self.get_left_child().get_root_val():
                raise TreeValueError('Значение больше родительского узла')

            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):

        if int(new_node) <= int(self.root):
            raise TreeValueError(f'Значение правого узла меньше корня')

        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:

            if int(new_node) <= self.get_right_child().get_root_val():
                raise TreeValueError(f'Значение меньше родительского узла')

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
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())

'''
вывод
    Traceback (most recent call last):
      File "D:\-algorithms_2021\Урок 8. Практическое задание\task_2.py", line 94, in <module>
        r.insert_left(40)
      File "D:\-algorithms_2021\Урок 8. Практическое задание\task_2.py", line 32, in insert_left
        raise TreeValueError('Значение левого узла больше корня')
    __main__.TreeValueError: Значение левого узла больше корня
    8
    None
'''
