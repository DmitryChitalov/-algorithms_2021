"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""
class ErrorInputNode(Exception):
    pass


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
        try:
            if new_node >= self.root:
                raise ErrorInputNode
            if self.left_child is None:
                # узел добавляется и формируется новое поддерево
                self.left_child = BinaryTree(new_node)
                # если узел имеет левый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # двигаем текущего потомка на уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        except ErrorInputNode:
            print('Левый потомок должен быть меньше чем корень')

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child is None:
            # узел добавляется и формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # двигаем текущего потомка на уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj
        try:
            if new_node <= self.root:
                raise ErrorInputNode
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
        except ErrorInputNode:
            print('Правый потомок должен быть больше чем корень')

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

if __name__ == "__main__":
    # Инициализируем дерево
    r = BinaryTree(8)
    # выводим корень текущего дерева
    print(r.get_root_val())
    # выводим левую и правую ветви - они пока пустые
    print(r.get_left_child())
    print(r.get_right_child())
    # вставляем значение 40 в левую ветвь - получаем исключение
    r.insert_left(40)
    # вставляем значение 5 в левую ветвь
    r.insert_left(5)
    print(r.get_left_child())
    # выводим значение левой ветви
    print(r.get_left_child().get_root_val())
    # Вставляем значение 7 в правую ветвь - получаем исключение
    r.insert_right(7)
    print(r.get_right_child())
    # выводим значение правой ветви
    print(r.get_right_child().get_root_val())
    # Вставляем значение 16 в правую ветвь
    r.get_right_child().set_root_val(16)
    # выводим значение правой ветви
    print(r.get_right_child().get_root_val())
    r.get_right_child().set_root_val(20)
    print(r.get_right_child().get_root_val())

"""
Проверил как работает валидация при вставке значения: меньше чем корень слева, больше чем корень справа
"""