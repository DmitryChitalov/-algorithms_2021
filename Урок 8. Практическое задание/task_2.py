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

    # если ставить валидацию только на проверку, то доработка в две строчки -
    # код просто не будет срабатывать и можно вывести сообщение об ошибке.
    # доработаем так, чтобы код сам раскидывал числа (вправо и влево)
    # при этом, при вводе числа, которе уже было в дереве просто ничего не произойдет

    def insert(self, new_node):
        if new_node < self.root:
            self.__insert_left__(new_node)
        elif new_node > self.root:
            self.__insert_right__(new_node)
        else:
            print('такое число уже вставлялось')
    # добавить левого потомка
    def __insert_left__(self, new_node):
        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            while True:
                if type(self.left_child) is BinaryTree:
                    self.left_child = self.left_child.root
                else:
                    break
            if new_node < self.left_child:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
            elif new_node > self.left_child:
                self.left_child = BinaryTree(self.left_child)
                self.left_child.__insert_right__(new_node)
            else:
                print('такое число уже вставлялось')

    # добавить правого потомка
    def __insert_right__(self, new_node):
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            while True:
                if type(self.right_child) is BinaryTree:
                    self.right_child = self.right_child.root
                else:
                    break
            if new_node > self.right_child:
            # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj

            elif new_node < self.right_child:
                self.right_child = BinaryTree(self.right_child)
                self.right_child.__insert_left__(new_node)
            else:
                print('такое число уже вставлялось')

    # метод доступа к правому потомку
    def get_right_child(self):
        while True:
            if type(self.right_child) is BinaryTree:
                self.right_child = self.right_child.root
            else:
                break
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        ind = 0
        while True:
            if type(self.left_child) is BinaryTree:
                self.left_child = self.left_child.root
                ind += 1
            else:
                break
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(8)
# print(r.get_root_val())
# print(r.get_left_child())
# print(r.get_right_child())
r.insert(5)
r.insert(12)
print(r.get_right_child())
print(r.get_left_child())
r.insert(35)
print(r.get_right_child())
r.insert(45)
print(r.get_right_child())
print(r.get_left_child())
print(r.get_root_val())
r.insert(40)
r.insert(6)
print(r.get_right_child())
print(r.get_left_child())
print(r.get_root_val())
