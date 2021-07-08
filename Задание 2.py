"""
Задание 2. (1:31:50 вебинара)
Доработайте пример структуры "дерево",
рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).
Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""

# ЗАДАЧА: Доработать дерево, добавив ВАЛИДАЦИЮ (Проверка чего либо, заданным условиям)
import sys

class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None

    def __str__(self):
        return str(self.root)

    # добавить левого потомка
    def insert_left(self, new_node):
        try:
            """
            Валидация значений узлов в соответствии с требованиями для бинарного дерева:
            Любое значение МЕНЬШЕ значения узла становится левым ребенком или ребенком левого ребенка.
            """
            if self.root >= new_node:
                # если у узла нет левого потомка990-з
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
            else:
                raise Exception('Ошибка значения') # Вызов исключение -  инструкция raise
        except Exception as e: # Исключения из базового класса Exception
            print(e)

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            """
            Любое значение больше или равное значению узла становится правым ребенком или ребенком правого ребенка.
            """
            if self.root <= new_node:
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
            else:
                raise Exception('Ошибка значения')
        except Exception as e:
            print(e)

    # метод доступа к правому потомку
    def get_right_child(self):
        try:
            return self.right_child
        except AttributeError:
            print('Ошибка доступа к атрибуту класса.')

    # метод доступа к левому потомку
    def get_left_child(self):
        try:
            return self.left_child
        except AttributeError:
            print('Ошибка доступа к атрибуту класса.')

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        try:
            return self.root
        except AttributeError:
            print('Ошибка доступа к атрибуту класса.')



r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(65)
r.insert_left(7)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())