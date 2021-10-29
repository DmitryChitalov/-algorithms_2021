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

    # Мой метод, чтобы программа сама определила куда нужно вставить новое значение и также проверила тип
    def insert(self, new_node):
        try:
            if type(new_node) is not int and type(new_node) is not float:
                raise ValueError(f"{new_node} - you must enter a number")
        except ValueError as err:
            print(err)
        else:

            if new_node > self.root or new_node == self.root:
                self.insert_right(new_node)
            else:
                self.insert_left(new_node)

    # Метод для работы принт
    def __str__(self):
        return str(self.root)

    # мой метод чтобы притновать дерево
    def Print_Tree(self):
        if self.left_child:
            self.left_child.Print_Tree()
        print(self.root, end=' ')
        if self.right_child:
            self.right_child.Print_Tree()


# r = BinaryTree(8)
# print(r.get_root_val())
# print(r.get_left_child())
# r.insert_left(40)
# print(r.get_left_child())
# print(r.get_left_child().get_root_val())
# r.insert_right(12)
# print(r.get_right_child())
# print(r.get_right_child().get_root_val())
# r.get_right_child().set_root_val(16)
# print(r.get_right_child().get_root_val())
r = BinaryTree(8)
r.insert('im not a number')
r.insert(5)
r.insert(6)
r.insert(10)
r.insert(2)
r.insert(9)
r.Print_Tree()
# r.insert(20)
# r.insert(1)
# r.insert(0)
# r.insert(40)
# r.Print_Tree()
