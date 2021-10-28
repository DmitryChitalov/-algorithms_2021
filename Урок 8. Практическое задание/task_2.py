"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class BinaryTree:
    def __init__(self, root_obj):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return str(self.root)

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

    def insert(self, new_node):
        try:
            if type(new_node) is not int and type(new_node) is not float:
                raise ValueError(f"{new_node} - не число")
        except ValueError as err:
            print(err)
        else:

            # Проверка больше ли новый объект чем корень
            if new_node > self.root or new_node == self.root:
                # Если правовго потомка еще нет, то вставляется новвый узел
                if self.right_child is None:
                    self.right_child = BinaryTree(new_node)
                # Если потомок есть, то вставляем его в узел, а имеющего спускаем вниз
                else:
                    tree_obj = BinaryTree(new_node)
                    if self.right_child.root < new_node:
                        tree_obj.left_child = self.right_child
                    else:
                        tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
            else:
                if self.left_child is None:
                    self.left_child = BinaryTree(new_node)
                else:
                    tree_obj = BinaryTree(new_node)
                    if self.left_child.root < new_node:
                        tree_obj.left_child = self.left_child
                    else:
                        tree_obj.right_child = self.left_child
                    self.left_child = tree_obj


r = BinaryTree(8)
r.insert(7)
r.insert(12)
r.insert(13)
r.insert(3.25)
r.insert(2)
r.insert(5)
r.insert('hello')
r.left_child.insert(6)

print(r.get_root_val())
# Левый и правый потомки от 8
# --> 5
# --> 13
print(r.get_left_child())
print(r.get_right_child())

# --> 2
# --> 6
print(r.get_left_child().get_left_child())
print(r.get_left_child().get_right_child())

# -->12
# None
print(r.get_right_child().get_left_child())
print(r.get_right_child().get_right_child())

# --> 3.25
# --> 7
print(r.get_left_child().get_left_child().get_right_child())
print(r.get_left_child().get_left_child().get_right_child().get_right_child())
