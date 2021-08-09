"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""

class IncorrectValueError(Exception):
    pass


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        if new_node <= self.root:
            if self.left_child == None:
                self.left_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        else:
            raise IncorrectValueError("Невозможно ввести значение!"
                                       " Значение левого потомка должно быть меньше или равно значению предка!")

    def insert_right(self, new_node):
        if new_node >= self.root:
            if self.right_child == None:
                self.right_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
        else:
            raise IncorrectValueError("Невозможно ввести значение!"
                                       " Значение правого потомка должно быть больше или рано значению предка!")

    def get_right_child(self):
        if self.right_child != None:
            return self.right_child
        else:
            raise IncorrectValueError("Невозможно получить значение! Значения правого потомка не существует!")

    def get_left_child(self):
        if self.left_child != None:
            return self.left_child
        else:
            raise IncorrectValueError("Невозможно получить значение! Значения левого потомка не существует!")

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        return self.root

# Не знаю, на сколько эффективны эти изменения, но повторять как в примере не особо хотелось
r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(40)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())