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

# Тут все просто, надо просто объединить обе вставки и добавить сравнения

    def insert_new(self, new_node):
        if new_node < self.root and self.left_child:
            if new_node < self.left_child.root:
                self.left_child.insert_new(new_node)
            else:
                new_ins = BinaryTree(new_node)
                new_ins.left_child = self.left_child
                self.left_child = new_ins
        elif new_node < self.root and not self.left_child:
            self.left_child = BinaryTree(new_node)

        else:
            if not self.right_child:
                self.right_child = BinaryTree(new_node)
            else:
                if new_node < self.right_child.root:
                    new_ins = BinaryTree(new_node)
                    new_ins.right_child = self.right_child
                    self.right_child = new_ins
                else:
                    self.right_child.insert_new(new_node)

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
r.insert_new(40)
r.insert_new(12)
r.insert_new(16)
r.insert_new(13)
r.insert_new(100)
r.insert_new(1)
r.insert_new(4)
r.insert_new(3)
r.insert_new(7)
r.insert_new(121)
print(r.root)
print(f'###########Правые##############')
print(r.get_right_child())
print(r.get_right_child().get_root_val())
print(r.get_right_child().get_right_child().get_root_val())
print(f'###########Левые##############')
print(r.get_left_child())
print(r.get_left_child().get_root_val())
print(r.get_left_child().get_left_child().get_root_val())

"""
8
###########Правые##############
<__main__.BinaryTree object at 0x00000265E430F5B0>
12
13
###########Левые##############
<__main__.BinaryTree object at 0x00000265E430F850>
7
4
"""
