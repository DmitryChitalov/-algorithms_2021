"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class BinaryTree:
    def __init__(self, root_obj: int):
        self.root = root_obj
        self.left_child = None
        self.right_child = None

    def __str__(self):
        return f'{self.root}'

    def insert_in_tree(self, new_node: int):
        # Добавляем валидацию данных и автоматическую вставку элементов

        # Если новый элемент меньше корня и нет левого потомка
        if (new_node < self.root) and (self.left_child is None):
            self.left_child = BinaryTree(new_node)

        # Если новый элемент меньше корня и есть левый потомок
        elif (new_node < self.root) and self.left_child:
            self.left_child.insert_in_tree(new_node)

        # Если новый элемент больше корня и нет правого потомка
        elif (new_node > self.root) and (self.right_child is None):
            self.right_child = BinaryTree(new_node)

        # Если новый элемент больше корня и есть правый потомок
        elif (new_node > self.root) and self.right_child:
            self.right_child.insert_in_tree(new_node)

        # В случае совпадения корня и нового значения
        else:
            print('Такое значение уже есть в дереве')

    # метод доступа к правому потомку
    @property
    def get_right_child(self):
        if self.right_child:
            return self.right_child
        else:
            return 'Правый потомок отсутствует'

    # метод доступа к левому потомку
    @property
    def get_left_child(self):
        if self.left_child:
            return self.left_child
        else:
            return 'Левый потомок отсутствует'

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    # метод печати всех элементов дерева, выводит левого потомка, затем родителя, затем правого потомка
    def print_tree(self):

        if self.left_child:
            self.left_child.print_tree()
        print(self.root)
        if self.right_child:
            self.right_child.print_tree()

    # Корень -> Левый потомок -> Правый потомок
    def tree_in_list(self, root):
        res = []
        if root:
            res.append(root.root)
            res = res + self.tree_in_list(root.left_child)
            res = res + self.tree_in_list(root.right_child)
        return res


r = BinaryTree(8)
r.insert_in_tree(7)
r.insert_in_tree(10)
r.insert_in_tree(12)

print(r.tree_in_list(r))

r.print_tree()