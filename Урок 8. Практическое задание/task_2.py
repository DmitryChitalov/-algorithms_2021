"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        try:
            if self.root < new_node:
                raise OwnError(f"Левый потомок = {new_node} не может быть больше родителя = {self.root}")
            if self.left_child is None:
                print(f'Левая ветка отсутствует, лист {new_node} установлен')
                self.left_child = BinaryTree(new_node)
            else:
                if self.left_child.get_root_val() < new_node:
                    print(f'Левая ветка существует. Ее голова = {self.left_child} '
                          f'меньше {new_node}, поэтому вставляем выше')
                    tree_obj = BinaryTree(new_node)
                    tree_obj.left_child = self.left_child
                else:
                    raise OwnError(f"Левая ветка существует ее корень = {self.left_child.set_root_val()} "
                                   f"больше нашего  = {new_node}, - сюда не вставить")
        except OwnError as err:
            print(err)

    def insert_right(self, new_node):
        try:
            if self.root > new_node:
                raise OwnError(f"Левый потомок = {new_node} не может быть больше родителя = {self.root}")
            if self.right_child is None:
                print(f'Правая ветка отсутствует, лист {new_node} установлен')
                self.right_child = BinaryTree(new_node)
            else:
                if self.right_child.get_root_val() < new_node:
                    tree_obj = BinaryTree(new_node)
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
                else:
                    raise OwnError(f"Правая ветка существует ее корень = {self.right_child.get_root_val()} "
                                   f"больше нашего  = {new_node}, - сюда не вставить")
        except OwnError as err:
            print(err)

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj=None):
        self.root = obj

    def get_root_val(self):
        return self.root


r = BinaryTree(18)
print(r)
print(r.get_root_val())
print(r.get_left_child())
r.insert_right(140)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.insert_right(112)
r.get_right_child().set_root_val(112)
r.insert_right(140)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(116)
print(r.get_right_child().get_root_val())
print(r.get_right_child().get_right_child().get_root_val())
