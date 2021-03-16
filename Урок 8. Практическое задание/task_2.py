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
        # если у узла нет левого потомка
        if self.left_child is None and self.root > new_node:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        elif self.left_child is not None and self.left_child < new_node:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj
        else:
            print('Нельзя, чтобы значение левого ребенка было больше, чем значение родителя!')

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child is None and self.root <= new_node:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        elif self.right_child is not None and self.right_child > new_node:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj
        else:
            print('Нельзя, чтобы значение правого ребенка было меньше, чем значение родителя!')

    # метод доступа к правому потомку
    def get_right_child(self):
        if self.right_child is not None:
            return self.right_child
        else:
            print('У данного узла нет правого ребенка!')

    # метод доступа к левому потомку
    def get_left_child(self):
        if self.left_child is not None:
            return self.left_child
        else:
            print('У данного узла нет левого ребенка!')

    # метод установки корня
    # def set_root_val(self, obj):    # Учитывая, что у нас можно создавать узел с детьми через объект, Я бы вообще
    #    self.root = obj              # убрал этот метод, так как настраивать валидацию для него проблематично

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    # Какое никакое, но отображение
    def __str__(self):
        return (f'({self.root}: {self.left_child if self.left_child is not None else ""}'
                f' {self.right_child if self.right_child is not None else ""})')


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(40)
print(r.get_left_child())
r.insert_right(12)
print(r.get_right_child().get_root_val())
# r.get_right_child().set_root_val(16)

print('-' * 200)

r.insert_left(4)
r.left_child.insert_left(2)
r.left_child.insert_right(6)
print(r)

'''
Здесь добавил валидацию в методах по добавлению ребенка и немного
подкорректировал отображение дерева и узлов
'''
