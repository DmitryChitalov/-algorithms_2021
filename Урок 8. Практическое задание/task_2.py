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

    def insert_func(self, new_node):
        if new_node < self.root:
            if self.left_child is None:
                self.left_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.left_child = self.left_child
                self.left_child.insert_func(tree_obj)
        else:
            if self.right_child is None:
                self.right_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
                tree_obj.right_child = self.right_child
                self.right_child.insert_func(tree_obj)

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

    def print_tree(self):
        if self.left_child:
            self.left_child.print_tree()
        print(self.root),
        if self.right_child:
            self.right_child.print_tree()


r = BinaryTree(8)
r.insert_func(6)
print(r.get_root_val())
print(r.get_left_child())
#r.insert_left(40)
r.insert_func(12)
r.insert_func(4)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
#r.insert_right(12)
r.insert_func(40)
r.insert_func(18)
r.insert_func(10)
print(r.get_right_child())
# print(r.get_right_child().get_root_val())
# r.get_right_child().set_root_val(16)
# print(r.get_right_child().get_root_val())
r.left_child.print_tree()
r.right_child.print_tree()
# print(r.print_tree())

# Ошибка следующая:
# Traceback (most recent call last):
#   File "C:\Users\zekto\PycharmProjects\Lesson_8\task_2.py", line 69, in <module>
#     r.insert_func(4)
#   File "C:\Users\zekto\PycharmProjects\Lesson_8\task_2.py", line 28, in insert_func
#     self.left_child.insert_func(tree_obj)
#   File "C:\Users\zekto\PycharmProjects\Lesson_8\task_2.py", line 22, in insert_func
#     if new_node < self.root:
# TypeError: '<' not supported between instances of 'BinaryTree' and 'int'
# Я предполагал, что self.root вернёт значение root, в данном случае 8, и далее будет производиться сравнение
# меньше корня, в левую ветвь, меньше левого листа, значит записывается значение ниже "листа"
