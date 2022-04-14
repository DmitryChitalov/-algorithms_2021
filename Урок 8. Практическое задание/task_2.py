"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class SemanticError(Exception):
    """ Добавил валидацию при инсерте справа и слева"""
    def __init__(self, txt):
        self.txt = txt


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
            if new_node > self.get_root_val():
                raise SemanticError(f'Левый потомок должен быть меньше родителя!(меньше {self.get_root_val()})')
        except SemanticError as se:
            print(se)
        else:
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
            if new_node < self.get_root_val():
                raise SemanticError(f'Правый потомок должен быть больше родителя!(больше {self.get_root_val()})')
        except SemanticError as se:
            print(se)
        else:
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


r1 = BinaryTree(10)
print(r1.get_root_val())
r1.insert_right(8)
print(r1.right_child)
r1.insert_right(20)
print(r1.right_child.get_root_val())
r1.insert_left(33)
print(r1.left_child)
r1.insert_right(15)
r2 = r1.right_child
print(f'r2:   {r2}')
print(r1.right_child.get_root_val())  # Вставили объект в уже существующую связь с потомком
print(r2.right_child.get_root_val())  # Проверим сместился ли бывший правый потомок
print(r2.left_child)
