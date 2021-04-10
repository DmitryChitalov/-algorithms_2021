"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""

class Tree:
    """Класс Бинарное дерево"""
    def __init__(self, root_obj):
        """
        Конструктор принимает
        :param root_obj (int): корень дерева
        """

        self.root = root_obj
        self.left_child = None  # левый потомок
        self.right_child = None  # правый потомок

    def __str__(self):
        return str(self.root)

    def add_left(self, new_node):
        """Метод добавления левого потомка"""

        try:
            if self.root >= new_node:
                if self.left_child is None:
                    self.left_child = Tree(new_node)
                else:
                    # тогда вставляем новый узел
                    tree_obj = Tree(new_node)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
            else:
                raise Exception('Ошибка значения')
        except Exception as e:
            print(e)

    def add_right(self, new_node):
        """Метод добавления правого потомка"""
        try:
            if self.root <= new_node:
                if self.right_child is None:
                    self.right_child = Tree(new_node)
                else:
                    tree_obj = Tree(new_node)
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
            else:
                raise Exception('Ошибка значения')
        except Exception as e:
            print(e)

    def get_right_child(self):
        """Метод доступа к правому потомку"""
        try:
            return self.right_child
        except AttributeError:
            print('Ошибка доступа к атрибуту класса.')

    def get_left_child(self):
        """Метод доступа к левому потомку"""
        try:
            return self.left_child
        except AttributeError:
            print('Ошибка доступа к атрибуту класса.')

    def set_root_val(self, obj):
        """Метод установки корня"""
        self.root = obj

    def get_root_val(self):
        """Метод доступа к корню"""
        try:
            return self.root
        except AttributeError:
            print('Ошибка доступа к атрибуту класса.')


if __name__ == '__main__':
    r = Tree(10)
    print(r.get_root_val())
    print(r.get_left_child())
    r.add_left(44)
    r.add_left(5)
    print(r.get_left_child())
    print(r.get_left_child().get_root_val())
    r.add_right(18)
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
    r.get_right_child().set_root_val(14)
    print(r.get_right_child().get_root_val())