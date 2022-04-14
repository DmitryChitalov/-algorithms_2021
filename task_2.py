"""
Задание 2.
Доработайте пример структуры "дерево",
рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).
Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""
class BranchError(Exception):
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
            if new_node >= self.root:
                raise BranchError(f'Значение {new_node} левого потомка больше значения корня {self.root}')
        except BranchError as err:
            print(err)
            return None
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            try:
                if new_node >= self.get_left_child().get_root_val():
                    raise BranchError(f'Значение {new_node} левого потомка больше родительского узла {self.get_left_child().get_root_val()}')
            except BranchError as err:
                print(err)
                return None
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        try:
            if new_node <= self.root:
                raise BranchError(f'Значение {new_node} правого потомка больше значения корня {self.root}')
        except BranchError as err:
            print(err)
            return None
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            try:
                if new_node <= self.get_right_child().get_root_val():
                    raise BranchError(f'Значение {new_node} правого потомка больше родительского узла {self.get_right_child().get_root_val()}')
            except BranchError as err:
                print(err)
                return None
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

    # метод доступа к правому потомку
    def get_right_child(self):
        if self.right_child is None:
            return self
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        if self.left_child is None:
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
r.insert_left(25)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_left(6)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
print(r.insert_right(7))
print(r.get_right_child())
print(r.insert_right(12))
print(r.insert_right(11))
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())