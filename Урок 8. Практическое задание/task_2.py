"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class Is_Valid_Tree(Exception):
    def __init__(self, message):
        self.message = message


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
        try:
            # добавил проверку через try - except
            if self.root > new_node:
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
            else:
                raise Is_Valid_Tree(f'Потомок слева не может находится выше чем корень!')
        except Is_Valid_Tree as e:
            print(e)

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            # добавил проверку через try - except
            if self.root < new_node:
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
            else:
                raise Is_Valid_Tree(f'Потомок справа не может находится выше чем корень!')
        except Is_Valid_Tree as e:
            print(e)

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


# Создаю бинарное дерево
r = BinaryTree(15)
# Получаю значение корня
print(r.get_root_val())
# Сейчас у дерева нет потомков
print(r.get_left_child())
# Вставляю потомка - все в порядке
r.insert_left(7)
# Вставляю потомка со значением больше, чем у рута - except Is_Valid_Tree
r.insert_left(16)
# Таким образом, у меня сейчас в работе один потомок
print(r.get_left_child())
# со значением 7
print(r.get_left_child().get_root_val())
# По правой стороне тоже самое
r.insert_right(16)
r.insert_right(7)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(17)
print(r.get_right_child().get_root_val())
