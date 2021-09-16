"""
Задание 2.
Доработайте пример структуры "дерево",
рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).
Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class MyError(Exception):
    def __init__(self, text):
        self.txt = text


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert(self, new_node):
        """
        Из двух функций сделали одну
        :param new_node:
        :return:
        """
        try:
            if new_node == self.root:
                raise MyError("Число не может быть равно корню дерева")
            if new_node < self.root:
                if self.left_child is None:
                    self.left_child = BinaryTree(new_node)
                else:
                    tree_obj = BinaryTree(new_node)
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
            elif new_node > self.root:
                if self.right_child is None:
                    self.right_child = BinaryTree(new_node)
                else:
                    tree_obj = BinaryTree(new_node)
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj

        except MyError as mr:
            print(mr)

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.root = obj

    def get_root_val(self):
        return self.root


try:
    r = BinaryTree(8)

    print(r.get_root_val())
    r.insert(5)
    r.insert(44)
    print(r.get_left_child().get_root_val())
    print(r.get_right_child().get_root_val())

except AttributeError:
    print("Введите корректное число")
except TypeError:
    print("Необходимо ввести число")
except NameError:
    print("Необходимо ввести число")
