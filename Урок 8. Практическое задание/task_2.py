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

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            if new_node >= self.root:
                raise ValueError
        except ValueError:
            print(f'Левый потомок "{new_node}" не может быть больше или равен корню "{self.root}"')
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
            if new_node <= self.root:
                raise ValueError
        except ValueError:
            print(f'Правый потомок "{new_node}" не может быть меньше или равен корню "{self.root}"')
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
        if self.right_child == None:
            return f'Правый узел отсутвует. Корень: {self.root}'
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        if self.left_child == None:
            return f'Левый узел отсутвует. Корень: {self.root}'
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)

print(r.get_root_val())  # 8
print(r.get_left_child())  # Левый узел отсутвует. Корень: 8
r.insert_left(40)  # Левый потомок "40" не может быть больше или равен корню "8"
print(r.get_left_child())  # Левый узел отсутвует. Корень: 8
r.insert_left(6)
print(r.get_left_child())  # <__main__.BinaryTree object at 0x000001E36C2E8F10>
print(r.get_left_child().get_root_val())  # 6
print(r.get_root_val())  # 8
r.insert_right(2)  # Правый потомок "2" не может быть меньше или равен корню "8"
r.insert_right(12)
print(r.get_right_child())  # <__main__.BinaryTree object at 0x000001D8A1808DF0>
print(r.get_right_child().get_root_val())  # 12
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())  # 16
r.insert_left(4)
print(r.get_left_child().get_root_val())  # 4
