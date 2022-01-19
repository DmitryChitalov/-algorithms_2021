"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class TreeException(Exception):
    def __init__(self, txt: str):
        self.__what = txt

    def __str__(self):
        return self.__what


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
        flag = False
        if self.left_child == None:
            if self.right_child == None:
                if self.root > new_node:
                    # тогда узел просто вставляется в дерево
                    # формируется новое поддерево
                    self.left_child = BinaryTree(new_node)
                else:
                    raise TreeException("Потомок не может быть больше родителя")
            else:
                if self.right_child.root >= new_node:
                    self.left_child = BinaryTree(new_node)
                else:
                    raise TreeException("Потомок не может быть больше родителя")
        # если у узла есть левый потомок
        else:

            if self.right_child is None:
                if self.left_child.root > new_node:
                    flag = False
                else:
                    flag = True
            elif self.right_child.root < new_node:
                flag = True
            if flag:
                raise TreeException("Потомок не может быть больше родителя")
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

        print('Вставка прошла успешно')

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет левого потомка
        flag = False
        if self.right_child == None:
            if self.left_child == None:
                if self.root <= new_node:
                    # тогда узел просто вставляется в дерево
                    # формируется новое поддерево
                    self.right_child = BinaryTree(new_node)
                else:
                    raise TreeException("Потомок не может быть меньше родителя")
            else:
                if self.left_child.root <= new_node:
                    self.right_child = BinaryTree(new_node)
                else:
                    raise TreeException("Потомок не может быть меньше родителя")
        # если у узла есть левый потомок
        else:

            if self.left_child is None:
                if self.right_child.root <= new_node:
                    flag = False
                else:
                    flag = True
            elif self.left_child.root >= new_node:
                flag = True
            if flag:
                raise TreeException("Потомок не может быть меньше родителя")
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj

        print('Вставка прошла успешно')
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


r = BinaryTree(10)

r.insert_left(9)
r.insert_left(8)
r.insert_right(11)
r.insert_right(11)
r.insert_left(10)
r.insert_left(8)
r.insert_right(12)
r.insert_right(15)

"""
Я добавила класс исключений, который выбрасывает исключение при попытке
вставить неподходящий по иерархии элемент. Но в любом случае такая реализация 
создает ситуацию, при которой ветвь дерева заполняется не до конца, т.е при попытке
добавления элемента мы в успешном случае сразу создаем новую ветку, а не дозаполняем предыдущую
В идеальном случае я бы реализовала просто функцию insert, которая сама выбирает, куда ей вставить
элемент

"""