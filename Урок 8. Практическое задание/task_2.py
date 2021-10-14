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

    def __str__(self):
        return str(self.root)

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            # если у узла нет левого потомка
            if self.root >= new_node:
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
                raise Exception('Неверное значение (значение больше корня не может быть вставлено в левое поддерево!)')
        except Exception as error:
            print(error)

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            # если у узла нет правого потомка
            if self.root <= new_node:
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
                raise Exception('Неверное значение (значение меньше корня не может быть вставлено в правое поддерево!)')
        except Exception as error:
            print(error)

    # метод доступа к правому потомку
    def get_right_child(self):
        try:
            return self.right_child
        except AttributeError:
            print('Ошибка доступа')

    # метод доступа к левому потомку
    def get_left_child(self):
        try:
            return self.left_child
        except AttributeError:
            print('Ошибка доступа')

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        try:
            return self.root
        except AttributeError:
            print('Ошибка доступа')


r = BinaryTree(8)

print(f'Значение корня: {r.get_root_val()}')
print(f'Левый потомок: {r.get_left_child()}')
r.insert_left(10)
r.insert_left(1)
print(f'Левый потомок: {r.get_left_child()}')
print(f'Левый потомок: {r.get_left_child()}')
r.insert_right(12)
r.insert_right(2)
r.insert_right(13)
print(f'Правый потомок: {r.get_right_child()}')
print(f'Правый потомок: {r.get_right_child().get_root_val()}')
r.get_right_child().set_root_val(20)
print(f'Правый потомок: {r.get_right_child()}')


'''
Сложная тема для понимания, пару дней разбирался, что именно и как работает, доработал по примеру.
Пример task_2_2 очень интересен, построение графа наглядно отображает понимание структуры.
'''
