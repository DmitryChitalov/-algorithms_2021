"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""

"""
Не совсем понял как происходит добавление узлов, допустим есть схема
-----------корень----------------
----------/-----\----------------
-----узел1------узел2------------
----/-----\---------\------------
-узел3----узел4------узел5-------

чтобы дерево оставалось бинарным узел 4 должен быть больше узла1 и узла3, но меньше корня
в данном ООП при вставке insert_left значения вставляются слева... и понятно что так можно вставить
узел1 и узел3, а как при этом вставить узел4 ?
insert_right - как я понял вставляет значения направо и через него можно создать узел2 и узел5

Не осилил задачу... в основном из за того что поздно взялся, была идея переписать польностью код,
но времени на сдачу не остаётся поэтому сдаю как есть, а над решением буду ломать голову в перерыве между курсами
Спасибо за курс, очень надеюсь встретиться с вами в дальнейшем.
"""


class ValidationError(Exception):
    pass

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
            if new_node >= self.get_root_val():
                raise ValidationError()
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
        except ValidationError:
            print("Попытка вставить значение в неверный узел")

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if new_node < self.get_root_val():
                raise ValidationError()
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
        except ValidationError:
            print("Попытка вставить значение в неверный узел")

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
r.insert_left(9) # Попытка вставить значение в неверный узел
r.insert_left(4)
r.insert_left(2)
r.insert_left(1)
r.insert_right(7) # Попытка вставить значение в неверный узел
r.insert_right(12)
r.insert_right(16)
print(f'Верхний корень дерева = {r.get_root_val()}')



