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

    # добавить левого потомка
    def insert_left(self, new_node):
        if new_node >= self.root:  # Проверка корректности добавления потомка
            return print('Вставка значения не произведена. Левый потомок должен быть меньше значения корня.')
        # если у узла нет левого потомка
        if self.left_child is None:  # С None лучше сравнивать через is
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # Тогда, если наибольшее значение текущего левого потомка меньше вставляемого значения, вставляем новый узел
            # как предка справа. Если наименьшее значение текущего левого потомка >= вставляемого значения,
            # вставляем новый узел как предка слева. Если же не выполняется ничего из вышеперечисленного, то вставляемое
            # значение на данный уровень корректно вставить не удастся. Ругаемся.
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            if new_node > self.left_child.max_in_self():
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
            elif new_node <= self.left_child.min_in_self():
                tree_obj.right_child = self.left_child
                self.left_child = tree_obj
            else:
                print('Введенное значение находится между значениями в поддереве. Вставка не возможна.')

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node < self.root:  # Проверка корректности добавления потомка
            return print('Вставка значения не произведена. Правый потомок должен быть не меньше значения корня.')
        # если у узла нет правого потомка
        if self.right_child is None:  # С None лучше сравнивать через is
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # Тогда, если наибольшее значение текущего правого потомка меньше вставляемого значения, вставляем новый
            # узел как предка справа. Если наименьшее значение текущего правого потомка >= вставляемого значения,
            # вставляем новый узел как предка слева. Если же не выполняется ничего из вышеперечисленного, то вставляемое
            # значение на данный уровень корректно вставить не удастся. Ругаемся.
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            # tree_obj.right_child = self.right_child
            # self.right_child = tree_obj
            if new_node > self.right_child.max_in_self():
                tree_obj.left_child = self.right_child
                self.right_child = tree_obj
            elif new_node <= self.right_child.min_in_self():
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
            else:
                print('Введенное значение находится между значениями в поддереве. Вставка не возможна.')

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
        if self.left_child and self.left_child.max_in_self() >= obj or self.right_child and \
                self.right_child.min_in_self() < obj:
            print('Введенное значение не корректно. Вы должны ввести значение, большее всех значений в левом поддереве'
                  ' и не меньшее всех значений в правом.')
        else:
            self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        try:
            return self.root
        except AttributeError:
            print('Ошибка доступа к атрибуту класса.')

    def min_in_self(self):
        while type(self.left_child) is BinaryTree:
            return self.left_child.min_in_self()
        return self.root

    def max_in_self(self):
        while type(self.right_child) is BinaryTree:
            return self.right_child.min_in_self()
        return self.root


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(40)
r.insert_left(4)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
print('Наименьшее значение в дереве:', r.min_in_self())  # Поиск наименьшего значения в дереве
print('Наибольшее значение в дереве:', r.max_in_self())  # Поиск Наибольшего значения в дереве

print('В левое поддерево добавим листья 2 и 6.')
r.left_child.insert_left(2)
r.left_child.insert_right(6)
print('Наименьшее значение в левом поддереве:', r.left_child.min_in_self())
print('Наибольшее значение в левом поддереве:', r.left_child.max_in_self())
print('Пробуем вставить некорректное значение слева.')
r.insert_left(5)  # Пробуем вставить некорректное значение.
print('Вставим значение 7, большее максимума в левом поддереве.')
r.insert_left(7)
print('Вставленное значение, большее прежних левых:', r.left_child.root)
print(f'Его левая ветка: {r.left_child.left_child}, ее корень - {r.left_child.left_child.root}')
print(f'Его правая ветка: {r.left_child.right_child}')
print('Вставим значение 0, меньшее минимума в левом поддереве.')
r.insert_left(0)
print('Вставленное значение, меньшее прежних левых:', r.left_child.root)
print(f'Его левая ветка: {r.left_child.left_child}')
print(f'Его правая ветка: {r.left_child.right_child}, ее корень - {r.left_child.right_child.root}')

print('В правое поддерево добавим листья 14 и 18.')
r.right_child.insert_left(14)
r.right_child.insert_right(18)
print('Наименьшее значение в правом поддереве:', r.right_child.min_in_self())
print('Наибольшее значение в правом поддереве:', r.right_child.max_in_self())
print('Пробуем вставить некорректное значение справа.')
r.insert_right(15)
print('Вставим значение 20, большее максимума в правом поддереве.')
r.insert_right(20)
print('Вставленное значение, большее прежних правых:', r.right_child.root)
print(f'Его левая ветка: {r.right_child.left_child}, ее корень - {r.right_child.left_child.root}')
print(f'Его правая ветка: {r.right_child.right_child}')
print('Вставим значение 12, меньшее минимума в правом поддереве.')
r.insert_right(12)
print('Вставленное значение, меньшее прежних левых:', r.right_child.root)
print(f'Его левая ветка: {r.right_child.left_child}')
print(f'Его правая ветка: {r.right_child.right_child}, ее корень - {r.right_child.right_child.root}')

print('Меняем значение корня на валидное:')
print(f'Было: Корень: {r.root}. Левый потомок: {r.left_child}. Правый потомок: {r.right_child}')
r.set_root_val(9)
print(f'Стало: Корень: {r.root}. Левый потомок: {r.left_child}. Правый потомок: {r.right_child}')

print('Меняем значение корня на не валидное:')
print(f'Было: Корень: {r.root}. Левый потомок: {r.left_child}. Правый потомок: {r.right_child}')
r.set_root_val(13)
print(f'Стало: Корень: {r.root}. Левый потомок: {r.left_child}. Правый потомок: {r.right_child}')

'''
При вставке производится валидация значений узлов. Не даем вставить плохие значения.
Произведена проверка корректности изменения значения корня (set_root_val). Он должен быть больше всех в левом поддереве
и не меньше всех в правом.
'''
