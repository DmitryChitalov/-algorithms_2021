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

    def check_val(self, new_left_val=None, new_right_val=None, new_root=None):
        '''
        функция проверки левого и правого значения на на то, чтобы они были меньше и
        больше корня соответственно
        '''
        if new_root is None:
            new_root = self.root
        result = False
        if new_right_val is None and new_left_val is not None and new_root > new_left_val:
            result = True
        if new_left_val is None and new_right_val is not None and new_root < new_right_val:
            result = True
        return result

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            if self.check_val(new_left_val=new_node):
                # проверяем на то, чтобы новое значение было меньше корня
                self.left_child = BinaryTree(new_node)
                return self.left_child
            return 'invalid left value'
        # если у узла есть левый потомок
        else:
            if self.check_val(new_left_val=self.left_child.get_root_val(), new_root=new_node) \
                    and self.check_val(new_left_val=new_node):
                # проверяем на то, чтобы новое значение было меньше текущего и будущего
                # корня с учетом вставки
                # и вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
                return self.left_child
            return 'invalid again left value'

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            if self.check_val(new_right_val=new_node):
                # проверяем на то, чтобы новое значение было больше корня
                self.right_child = BinaryTree(new_node)
                return self.right_child
            return 'invalid right value'
        # если у узла есть правый потомок
        else:
            if self.check_val(new_right_val=self.right_child.get_root_val(), new_root=new_node)\
                    and self.check_val(new_right_val=new_node):
                # проверяем на то, чтобы новое значение было больше текущего и будущего корня
                # с учетом вставки
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
                return self.right_child
            return 'invalid again right value'

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
print(f'--LEVEL 1 root = {r.get_root_val()}, '
      f'left = {r.get_left_child()}, '
      f'right = {r.get_right_child()}')
value = 9
print(f'insert {value} into left =', r.insert_left(value))
print(f'--LEVEL 1 root = {r.get_root_val()}, '
      f'left = {r.get_left_child()}, '
      f'right = {r.get_right_child()}')
value = 7
print(f'insert {value} into left =', r.insert_left(value))
print(f'--LEVEL 1 root = {r.get_root_val()}, '
      f'left = {r.get_left_child()}, '
      f'right = {r.get_right_child()}')
value = 7
print(f'insert {value} into right =', r.insert_right(value))
print(f'--LEVEL 1 root = {r.get_root_val()}, '
      f'left = {r.get_left_child()}, '
      f'right = {r.get_right_child()}')
value = 9
print(f'insert {value} into right =', r.insert_right(value))
print(f'--LEVEL 1 root = {r.get_root_val()}, '
      f'left = {r.get_left_child()}, '
      f'right = {r.get_right_child()}')
print("")
print(
    f'--LEVEL 1 root = {r.get_root_val()}, '
    f'left = {r.get_left_child().get_root_val()}, '
    f'right = {r.get_right_child().get_root_val()}')
print("")
r_2_left = r.get_left_child()
print(
    f'--LEVEL 2 root = {r_2_left.get_root_val()},'
    f' left = {r_2_left.get_left_child()}, '
    f'right = {r_2_left.get_right_child()}')
value = 3
print(f'insert {value} into left =', r_2_left.insert_left(value))
print(
    f'--LEVEL 2 root = {r_2_left.get_root_val()}, '
    f'left = {r_2_left.get_left_child()}, '
    f'right = {r_2_left.get_right_child()}')
print(
    f'--LEVEL 2 root = {r_2_left.get_root_val()}, '
    f'left = {r_2_left.get_left_child().get_root_val()}, '
    f'right = {r_2_left.get_right_child()}')
value = 2
print(f'insert {value} into left again =', r_2_left.insert_left(value))
print(
    f'--LEVEL 2 root = {r_2_left.get_root_val()}, '
    f'left = {r_2_left.get_left_child()}, '
    f'right = {r_2_left.get_right_child()}')
print(
    f'--LEVEL 2 root = {r_2_left.get_root_val()}, '
    f'left = {r_2_left.get_left_child().get_root_val()}, '
    f'right = {r_2_left.get_right_child()}')
value = 7
print(f'insert {value} into left again =', r_2_left.insert_left(value))
print(
    f'--LEVEL 2 root = {r_2_left.get_root_val()}, '
    f'left = {r_2_left.get_left_child().get_root_val()}, '
    f'right = {r_2_left.get_right_child()}')
print(
    f'--LEVEL 2 root = {r_2_left.get_root_val()}, '
    f'left = {r_2_left.get_left_child().get_root_val()}, '
    f'right = {r_2_left.get_right_child()}')
value = 5
print(f'insert {value} into left again =', r_2_left.insert_left(value))
print(
    f'--LEVEL 2 root = {r_2_left.get_root_val()}, '
    f'left = {r_2_left.get_left_child().get_root_val()}, '
    f'right = {r_2_left.get_right_child()}')
print("")
print(
    f'--LEVEL 3 root = {r_2_left.get_left_child().get_root_val()}, '
    f'left = {r_2_left.get_left_child().get_left_child().get_root_val()}, '
    f'right = {r_2_left.get_right_child()}')
