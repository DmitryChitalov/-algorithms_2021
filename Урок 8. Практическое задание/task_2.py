"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class BinaryTreeInsertErr(Exception):
    def __init__(self, text):
        self.text = text


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
            if new_node < self.root:
                # если у узла нет левого потомка
                if self.left_child == None:
                    # тогда узел просто вставляется в дерево
                    # формируется новое поддерево
                    self.left_child = BinaryTree(new_node)
                # если у узла есть левый потомок
                else:
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(new_node)
                    # и спускаем имеющегося потомка на один уровень ниже,
                    # первоначально, сравнив его значение  со значением нового узла, чтобы определить, каким,
                    # правым или левым child нового узла он должен стать для соблюдения семантики дерева.
                    if self.left_child <= new_node:
                        tree_obj.left_child = self.left_child
                    else:
                        tree_obj.right_child = self.left_child
                    self.left_child = tree_obj
            else:
                raise BinaryTreeInsertErr('Ошибка вставки нового узла! Значение потомка больше значения корня!'
                      ' Вы не можете вставить его слева от корня!')
        except BinaryTreeInsertErr as err:
            print(err)


    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if new_node > self.root:
                # если у узла нет правого потомка
                if self.right_child == None:
                    # тогда узел просто вставляется в дерево
                    # формируется новое поддерево
                    self.right_child = BinaryTree(new_node)
                else:
                    # если у узла есть правый потомок
                    # тогда вставляем новый узел
                    # и спускаем имеющегося потомка на один уровень ниже
                    # первоначально, сравнив его значение  со значением нового узла, чтобы определить, каким,
                    # правым или левым child нового узла он должен стать для соблюдения семантики дерева.
                    tree_obj = BinaryTree(new_node)
                    if self.right_child < new_node:
                        tree_obj.left_child = self.right_child
                    else:
                        tree_obj.right_child = self.right_child

                    self.right_child = tree_obj
            else:
                raise BinaryTreeInsertErr('Ошибка вставки нового узла! Значение потомка меньше значения корня!'
                                              ' Вы не можете вставить его справа от корня!')
        except BinaryTreeInsertErr as err:
            print(err)



    # метод доступа к правому потомку
    #
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child


    # метод установки корня
    # если есть дочерние узлы/узел, сравниваю с их значениями новое значение корня, чтобы был соблюден принцип бинарного дерева,
    # и если необходимо, меняю значения дочерних узлов:
    def set_root_val(self, obj):
        self.root = obj
        if self.left_child is not None and obj < self.left_child:
                self.right_child = self.left_child
                self.left_child = None
        elif self.right_child is not None and obj > self.right_child:
                self.left_child = self.right_child
                self.right_child = None
        return self.left_child, self.root, self.right_child


    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(40)
r.insert_left(20)
r.insert_left(4)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(7)
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
