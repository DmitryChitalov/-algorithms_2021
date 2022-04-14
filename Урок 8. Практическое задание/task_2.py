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

    def insert(self, new_node):
        try:
            if new_node > self.root:
                if self.right_child is not None:
                    if new_node < self.right_child.get_root_val():
                        tree_obj = BinaryTree(new_node)
                        tree_obj.right_child = self.right_child
                        self.right_child = tree_obj
                        print(f'Вставил {new_node} после {self.root}')
                    elif new_node > self.right_child.get_root_val():
                        if self.right_child.right_child is None:
                            self.right_child.right_child = BinaryTree(new_node)
                            print(f'Вставил {new_node} после {self.right_child.get_root_val()}')
                        else:
                            self.right_child.insert(new_node)
                    else:
                        print(f'Узел уже существует')
                else:
                    self.right_child = BinaryTree(new_node)
                    print(f'Вставил {new_node} после {self.root}!')
            elif new_node < self.root:
                if self.left_child is not None:
                    if new_node > self.left_child.get_root_val():
                        tree_obj = BinaryTree(new_node)
                        tree_obj.left_child = self.left_child
                        self.left_child = tree_obj
                        print(f'Вставил {new_node} после {self.root}')
                    elif new_node < self.left_child.get_root_val():
                        if self.left_child.left_child is None:
                            self.left_child.left_child = BinaryTree(new_node)
                            print(f'Вставил {new_node} после {self.left_child.get_root_val()}')
                        else:
                            self.left_child.insert(new_node)
                    else:
                        print(f'Узел уже существует')
                else:
                    self.left_child = BinaryTree(new_node)
                    print(f'Вставил {new_node} после {self.root}!')
            else:
                print(f'Узел уже существует')
        except TypeError as e:
            print(f'{type(new_node)} - недопустимый тип для ввода!')

    # добавить левого потомка
    def insert_left(self, new_node) -> object:
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
        if not self.right_child:
            return BinaryTree(None)
        return self.right_child

    # метод доступа к левому потомку
    def get_left_child(self):
        if not self.left_child:
            return BinaryTree(None)
        return self.left_child

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


print('Вывод в стартовой реализации: ')
r1 = BinaryTree(8)
print(r1.get_root_val())
print(r1.get_left_child())
r1.insert_left(40)
print(r1.get_left_child())
print(r1.get_left_child().get_root_val())
r1.insert_right(12)
print(r1.get_right_child())
print(r1.get_right_child().get_root_val())
r1.get_right_child().set_root_val(16)
print(r1.get_right_child().get_root_val())
r1.insert_left(15)
print(r1.get_left_child().get_root_val())
print(r1.get_left_child().get_left_child().get_root_val())

print('\nВывод в доработанной реализации: ')
r2 = BinaryTree(8)
print(r2.get_root_val())
print(r2.get_left_child().get_root_val())
print(r2.get_right_child().get_root_val())
r2.insert(40)
r2.insert(15)
r2.insert(50)
r2.insert(35)
print(r2.get_right_child().get_root_val())
print(r2.get_right_child().get_right_child().get_root_val())
print(r2.get_right_child().get_right_child().get_right_child().get_root_val())
print(r2.get_right_child().get_right_child().get_right_child().get_right_child().get_root_val())
r2.insert(4)
r2.insert(1)
r2.insert(5)
r2.insert(6)
print(r2.get_left_child().get_root_val())
print(r2.get_left_child().get_left_child().get_root_val())
print(r2.get_left_child().get_left_child().get_left_child().get_root_val())
print(r2.get_left_child().get_left_child().get_left_child().get_left_child().get_root_val())
r2.insert(6)
r2.insert(8)
r2.insert(40)
r2.insert('abab')


# Добавил универсальный инсерт слева и справа, который валидирует по значению
# (если больше вставляет справа, если меньше слева)
# Также теперь если попытаться получить значение несуществующего потомка слева или справа, то вернется None
# Значения, которые уже есть в дереве отбрасываются
