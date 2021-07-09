"""
Задание 2.
Доработайте пример структуры "дерево",
рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).
Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""

class MyException(Exception):
    def __init__(self, text):
        self.text = text

    def __str__(self):
        return f"{self.text}"

class BinaryTree:
    # Добавил слоты для улучшения памяти...
    __slots__ = ("root", "left_child", "right_child")

    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # Добавил печать вссего дерева.
    def __str__(self):
        return "[%s, %s, %s]" % (self.left_child, str(self.root), self.right_child)

    def isEmpty(self):
        return self.left_child == self.right_child == self.root is None

    # Не стал делать отдельные методы вставки значений на лево и право.
    # Вставку значений, решил сделать, программно, что б пользователь просто,
    # указывал значение, а программа сама решит куда его нужно вставить...
    # Выполнен перехват ошибок по типу введеного значения.
    def insert(self, root):
        try:
            if self.isEmpty():
                self.root = root
                return
            elif root < self.root:
                if self.left_child is None:
                    self.left_child = BinaryTree(root)
                else:
                    tree_obj = BinaryTree(root)
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
            else:
                if self.right_child is None:
                    self.right_child = BinaryTree(root)
                else:
                    tree_obj = BinaryTree(root)
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
        except TypeError:
            print(f"В бинарном дереве, можно указывать только целые цифры,"
                  f"в качестве значения!")

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


a = BinaryTree(4)
a.insert(2)
a.insert(3)
a.insert(5)
a.insert(6)
a.insert(7)
a.insert(8)
a.insert("value")
print(a)
print(a.get_root_val())
print(a.get_left_child())
print(a.get_right_child())
