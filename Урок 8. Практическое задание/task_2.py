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
        try:
            if self.root <= new_node:  # В левую часть больше предка значение не поставить.
                raise ValueError
        except ValueError:
            print(f'The entered value is greater than or equal the root value!')
            return
        # если у узла нет левого потомка
        if self.left_child is None:
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
            if self.root >= new_node:  # В правую часть меньше предка значение не поставить.
                raise ValueError
        except ValueError:
            print(f'The entered value is less than or equal to the root value!')
            return
        # если у узла нет правого потомка
        if self.right_child is None:
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
        # try:  # При вызове этого метода к узлу равному None выдаёт ошибку AttributeError. Исправить не смог.
        #     self.root
        # except AttributeError:
        #     print('Attribute does not exist!')
        #     return
        return self.root


origin = BinaryTree(8)  # start (level 0)

# print(origin.get_left_child().get_root_val()) # Вызывает ошибку AttributeError.
origin.insert_left(4)  # left level 1
origin.get_left_child().insert_left(2)  # left level 2
origin.get_left_child().insert_right(6)

origin.insert_right(12)  # right level 1
origin.get_right_child().insert_left(10)  # right level 2
origin.get_right_child().insert_right(14)

origin.get_left_child().get_left_child().insert_left(1)  # left level 3
origin.get_left_child().get_left_child().insert_right(3)
origin.get_left_child().get_right_child().insert_left(5)
origin.get_left_child().get_right_child().insert_right(7)

origin.get_right_child().get_left_child().insert_left(9)  # right level 3
origin.get_right_child().get_left_child().insert_right(11)
origin.get_right_child().get_right_child().insert_left(13)
origin.get_right_child().get_right_child().insert_right(15)

"""
print(f'{origin.get_root_val()}\n'
      f'{origin.get_left_child()}\n')

print(f'{origin.get_left_child().get_root_val()}\n'
      f'{origin.get_left_child().get_left_child().get_root_val()}\n'
      f'{origin.get_left_child().get_right_child().get_root_val()}\n')

print(f'{origin.get_right_child().get_root_val()}\n'
      f'{origin.get_right_child().get_left_child().get_root_val()}\n'
      f'{origin.get_right_child().get_right_child().get_root_val()}\n')

print(f'{origin.get_left_child().get_left_child().get_root_val()}\n'
      f'{origin.get_left_child().get_left_child().get_left_child().get_root_val()}\n'
      f'{origin.get_left_child().get_left_child().get_right_child().get_root_val()}\n'
      f'{origin.get_left_child().get_right_child().get_root_val()}\n'
      f'{origin.get_left_child().get_right_child().get_left_child().get_root_val()}\n'
      f'{origin.get_left_child().get_right_child().get_right_child().get_root_val()}\n')

print(f'{origin.get_right_child().get_left_child().get_root_val()}\n'
      f'{origin.get_right_child().get_left_child().get_left_child().get_root_val()}\n'
      f'{origin.get_right_child().get_left_child().get_right_child().get_root_val()}\n'
      f'{origin.get_right_child().get_right_child().get_root_val()}\n'
      f'{origin.get_right_child().get_right_child().get_left_child().get_root_val()}\n'
      f'{origin.get_right_child().get_right_child().get_right_child().get_root_val()}\n')
"""

start = origin.get_root_val()

l1 = origin.get_left_child().get_root_val()
r1 = origin.get_right_child().get_root_val()

l2_1 = origin.get_left_child().get_left_child().get_root_val()
l2_2 = origin.get_left_child().get_right_child().get_root_val()
r2_1 = origin.get_right_child().get_left_child().get_root_val()
r2_2 = origin.get_right_child().get_right_child().get_root_val()

l3_1 = origin.get_left_child().get_left_child().get_left_child().get_root_val()
l3_2 = origin.get_left_child().get_left_child().get_right_child().get_root_val()
l3_3 = origin.get_left_child().get_right_child().get_left_child().get_root_val()
l3_4 = origin.get_left_child().get_right_child().get_right_child().get_root_val()
r3_1 = origin.get_right_child().get_left_child().get_left_child().get_root_val()
r3_2 = origin.get_right_child().get_left_child().get_right_child().get_root_val()
r3_3 = origin.get_right_child().get_right_child().get_left_child().get_root_val()
r3_4 = origin.get_right_child().get_right_child().get_right_child().get_root_val()

print(f'0.                              {start}\n'
      f'1.              {l1}                              {r1}\n'
      f'2.        {l2_1}           {l2_2}                  {r2_1}          {r2_2}\n'
      f'3.      {l3_1}   {l3_2}       {l3_3}   {l3_4}              {r3_1}   {r3_2}      {r3_3}  {r3_4}\n')
