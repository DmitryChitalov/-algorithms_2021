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

        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        # обработка ошибки значения, если ввео больше или равен корню, закрытие программы
        try:
            if self.root <= new_node:  # В левую часть больше предка значение не поставить.
                raise ValueError
        except ValueError:
            print(f'Введенное значение {new_node} больше или равно значения корня {self.root}! ')
            exit()
            # без exit() выскакивает:
            #
            # Traceback (most recent call last):
            #  File "D:\Repos\algRep\-algorithms_2021\Урок 8. Практическое задание\task_2.py", line 91, in <module>
            #    print(r.get_left_child().get_root_val())
            #  AttributeError: 'NoneType' object has no attribute 'get_root_val
            #  решить ошибку не смог, так и не понял, где обработку вставить.. ни в set_root_val(self, obj)
            #  ни в def get_root_val(self): не помогло.
            #
            return
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    def insert_right(self, new_node):
        # как в левом
        try:
            if self.root >= new_node:  # В правую часть меньше предка значение не поставить.
                raise ValueError
        except ValueError:
            print(f'Введенное значение {new_node} меньше или равно корню {self.root}!')
            exit()
            return
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            tree_obj = BinaryTree(new_node)
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

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


r = BinaryTree(7)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(7)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
