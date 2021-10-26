"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""
import random


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # Предлагаю сделать более умный insert.
    def insert(self, new_node):
        if self.root:
            if new_node < self.root:
                if self.left_child is None:
                    self.left_child = BinaryTree(new_node)
                else:
                    self.left_child.insert(new_node)
            elif new_node > self.root:
                if self.right_child is None:
                    self.right_child = BinaryTree(new_node)
                else:
                    self.right_child.insert(new_node)

        else:
            self.root = new_node

    # метод доступа к корню
    def _get_root_val(self):
        return self.root

    # метод доступа к правому потомку
    def get_right_child(self, root):

        if root == self.root:
            if self.right_child is None:
                print('Потомка нет')
            else:
                print(f'Узел {self.root}, правый потомок {self.right_child._get_root_val()}')
        else:
            try:
                if root > self.root:
                    self.right_child.get_right_child(root)
                else:
                    self.left_child.get_right_child(root)
            except AttributeError:
                print('Узел отсутствует')

    # метод доступа к левому потомку
    def get_left_child(self, root):
        if root == self.root:
            if self.left_child is None:
                print('Потомка нет')
            else:
                print(f'Узел {self.root}, левый потомок {self.left_child._get_root_val()}')
        else:
            try:
                if root > self.root:
                    self.right_child.get_left_child(root)
                else:
                    self.left_child.get_left_child(root)
            except AttributeError:
                print('Узел отсутствует')

    # Вывод дерева.
    def print_tree(self):
        if self.left_child:
            self.left_child.print_tree()

        print(self.root, end=" ")

        if self.right_child:
            self.right_child.print_tree()


x = BinaryTree(8)
x.insert(1)
x.insert(7)
x.insert(5)
x.insert(4)
x.insert(2)
x.insert(8)
x.insert(14)
x.insert(35)
x.insert(10)
x.insert(19)
x.insert(31)
x.insert(42)
x.print_tree()
print()
print()


for i in range(10):
    a = random.randint(1, 50)
    print(f'Поиск потомков узла {a}', end=': ')
    if i % 2 == 0:
        x.get_left_child(a)
    else:
        x.get_right_child(a)

"""
Решил упростить. Добавлен умный insert и вывод дерева.

1 2 4 5 7 8 10 14 19 31 35 42 

Поиск потомков узла 3: Узел отсутствует
Поиск потомков узла 23: Узел отсутствует
Поиск потомков узла 14: Узел 14, левый потомок 10
Поиск потомков узла 11: Узел отсутствует
Поиск потомков узла 10: Потомка нет
Поиск потомков узла 45: Узел отсутствует
Поиск потомков узла 3: Узел отсутствует
Поиск потомков узла 17: Узел отсутствует
Поиск потомков узла 2: Потомка нет
Поиск потомков узла 12: Узел отсутствует
"""