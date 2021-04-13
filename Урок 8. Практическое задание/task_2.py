"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""

from random import randint

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
        if self.root < new_node or self._is_correct_tree(self.left_child, new_node, True) == False:
            print(f'Нарушение правила построения бинарного дерева. '
                  f'Попытка вставить {new_node} слева от {self.root}')
            self.display()
            return
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
        if self.root > new_node or self._is_correct_tree(self.right_child, new_node, False) == False:
            print(f'Нарушение правила построения бинарного дерева. '
                  f'Попытка вставить {new_node} справа от {self.root}')
            self.display()
            return
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
        if self.left_child is not None:
            if self.left_child.root > obj:
                print(f'Нарушение правила построения бинарного дерева. '
                      f'Попытка установить значение узла ({obj}) меньше левого потомка ({self.left_child.root})')
                self.display()
                return
        if self.right_child is not None:
            if self.right_child.root < obj:
                print(f'Нарушение правила построения бинарного дерева. '
                      f'Попытка установить значение узла ({obj}) больше правого потомка ({self.right_child.root})')
                self.display()
                return
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    def _is_correct_tree(self, obj, value, is_more):
        if obj is None:
            return True
        if is_more and value < obj.root or is_more == False and value > obj.root:
            return False
        else:
            return (self._is_correct_tree(obj.left_child, value, True) and
                    self._is_correct_tree(obj.right_child, value, False))

    def insert_auto(self, new_node):
        if self.root == new_node:
            return
        elif self.root < new_node:
            if self.right_child is None:
                self.right_child = BinaryTree(new_node)
            else:
                self.right_child.insert_auto(new_node)
        else: # self.root > new_node
            if self.left_child is None:
                self.left_child = BinaryTree(new_node)
            else:
                self.left_child.insert_auto(new_node)

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right_child is None and self.left_child is None:
            line = '%s' % self.root
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right_child is None:
            lines, n, p, x = self.left_child._display_aux()
            s = '%s' % self.root
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left_child is None:
            lines, n, p, x = self.right_child._display_aux()
            s = '%s' % self.root
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left_child._display_aux()
        right, m, q, y = self.right_child._display_aux()
        s = '%s' % self.root
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2



r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(40)
r.insert_left(6)
r.insert_left(5)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())


r.insert_left(60)
r.insert_right(80)
r.insert_right(15)
r.insert_left(7)
r.right_child.insert_left(12)
r.right_child.insert_left(13)
# система не может учесть более высокий уровень и валидацию можно "обмануть", обращаяясь к вложенному классу.
r.left_child.insert_right(17)
print('Итоговое представление бинарного дерева:')
r.display()

# Это можно обойти, реализуя алгоритм автоматической вставки, через обращение к корню (insert_auto)
b = BinaryTree(50)
for _ in range(50):
    b.insert_auto(randint(0, 100))
print('Итоговое представление бинарного дерева, заполненного автоматически:')
b.display()

