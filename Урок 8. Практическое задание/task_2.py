"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class PositionOfTheTreeElementError(Exception):
    def __init__(self, text):
        self.txt = text


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.__root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            if new_node > self.__root:
                raise PositionOfTheTreeElementError('Ошибка вставки потомка:')
        except PositionOfTheTreeElementError as pos:
            print(f'{pos} вставляемое значение потомка - {new_node} должно быть меньше корня - {self.__root}')
            return
        # если у узла нет левого потомка
        if self.left_child is None:
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
        try:
            if new_node < self.__root:
                raise PositionOfTheTreeElementError('Ошибка вставки потомка:')
        except PositionOfTheTreeElementError as pos:
            print(f'{pos} вставляемое значение потомка - {new_node} должно быть больше корня - {self.__root}')
            return
        # если у узла нет правого потомка
        if self.right_child is None:
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
        self.__root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.__root


user_tree = BinaryTree(8)
print(user_tree.get_root_val())
user_tree.insert_left(8)
print(user_tree.get_left_child().get_root_val())

user_tree.insert_left(2)

print(user_tree.get_left_child().get_left_child().get_left_child())

user_tree.insert_right(16)
user_tree.get_right_child().set_root_val(4)
print(user_tree.get_right_child().get_root_val())

# Это довольно сырая реализация бинарного дерева, пользовательский код может вызвать ошибки. Можно обратиться
# к несуществующим узлам и запросить какой-либо метод, возникнет AttributeError - NoneType объект не имеет атрибутов.
# Кроме того метод установки корня также нуждается в доработке - проверок на вставляемое значение нет, а проверку
# сделать в такой реализации вряд ли получится, т.к. нет доступа к родителю.

# Сделана небольшая оптимизация по вставляемому значению для новых потомков.
