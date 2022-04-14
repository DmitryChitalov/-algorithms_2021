"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


# В качестве улучшения была введен новый метод insert_value класса BinaryTree вместо старых методов
# insert_left и insert_right. Новый метод выполняет проверку нового значения и на ее основани
# создает новый узел или вызывает функцию insert_value у потомка.

# еще одно улучшение это создание класса исключения для предотвращения root меньше или больше правого потомка,
# если таковые имеются. Исключение используется в методе set_root_val

class WrongRootException(Exception):
    def __init__(self, left=True):
        if left:
            self.message = 'Введенное значение меньше левого потомка'
        else:
            self.message = 'Введенное значение больше правого потомка'

    def __str__(self):
        return str(self.message)


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить потомка
    def insert_value(self, new_node):
        if new_node > self.root:
            if self.right_child:
                if new_node > self.right_child.root:
                    self.right_child.insert_value(new_node)
                elif new_node < self.right_child.root:  # если значение находится посередине, то создаем новый узел
                    new_tree = BinaryTree(new_node)     # и переназначаем потомка
                    new_tree.right_child = self.right_child
                    self.right_child = new_tree
            else:
                self.right_child = BinaryTree(new_node)
        elif new_node < self.root:
            if self.left_child:
                if new_node < self.left_child.root:
                    self.left_child.insert_value(new_node)
                elif new_node > self.left_child.root:
                    new_tree = BinaryTree(new_node)
                    new_tree.left_child = self.left_child
                    self.left_child = new_tree
            else:
                self.left_child = BinaryTree(new_node)
        else:
            print('Введенное значение равно root, новых потомков не создано.')

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        if self.left_child and obj <= self.left_child.root:
            raise WrongRootException()
        elif self.right_child and obj > self.right_child.root:
            raise WrongRootException(left=False)
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root

    def __repr__(self):
        return f'Бинарное дерево: ' \
               f'Root: {self.root}; Left: {self.left_child}; Right: {self.right_child}\n'


# Создаем дерево
r = BinaryTree(8)
print('Root value: ', r.get_root_val())

# Вставляем значение больше 8, новый потомок должен быть только справа
r.insert_value(12)
print('Правый потомок:', r.right_child)
print('Левый потомок:', r.left_child)

# Теперь вставляем значение между r.root и r.right_value
r.insert_value(10)
print('Новый правый потомок нашего дерева', r.right_child)
print('Правый потомок правого потомка:')
print(r.right_child.right_child)

# Вставим левого потомка:
r.insert_value(6)
print(r)

# Попробуем поменять root значение на значение больше правого потомка:
r.set_root_val(100)
