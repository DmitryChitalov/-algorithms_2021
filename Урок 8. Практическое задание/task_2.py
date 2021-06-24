"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class TreeRuleError(Exception):
    def __init__(self, text):
        self.text = text


class BinaryTree:
    __slots__ = ('root', 'left_child', 'right_child')
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        if new_node > self.root:
            raise TreeRuleError(f'Потомок слева не может быть больше корня! {new_node} > {self.root}')
        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            if new_node < self.left_child:
                raise TreeRuleError(f'Невозможно добавить слева узел с потомком больше, чем корень узла'
                                    f' {new_node} > {self.left_child}')
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node < self.root:
            raise TreeRuleError(f'Потомок справа должен быть больше корня! {new_node} < {self.root}')
        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            if new_node < self.right_child:
                raise TreeRuleError(f'Невозможно добавить справа узел с потомком меньше, чем корень узла'
                                    f'{new_node} < {self.right_child}')

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
        if self.right_child is not None:
            if obj > self.right_child.get_root_val():
                raise TreeRuleError(f'Корень не может быть больше потомка справа: '
                                    f'{obj} > {self.right_child.get_root_val()}')
        if self.left_child is not None:
            if obj < self.left_child.get_root_val():
                raise TreeRuleError(f'Корень не может быть меньше потомка слева: '
                                    f'{obj} < {self.left_child.get_root_val()}')
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root



r = BinaryTree(25)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(12)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(40)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().insert_right(50)
r.get_right_child().insert_left(30)
r.get_right_child().set_root_val(42)
print(r.get_right_child().get_root_val())
