"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

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
        # если у узла нет левого потомка
        if self.left_child is None:
            if new_node >= self.get_root_val():
                raise ValueError('Левый потомок должен быть меньше родительского узла!')
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            if new_node >= self.get_root_val() or new_node < self.get_left_child().get_root_val():
                print('Значение родительского узла:', self.get_root_val())
                raise ValueError('Левый потомок должен быть меньше родительского узла!')
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child is None:
            if new_node < self.get_root_val():
                raise ValueError('Правый потомок должен быть больше родительского узла или равен ему!')
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            if new_node < self.get_root_val() or new_node > self.get_right_child().get_root_val():
                print('Значение родительского узла:', self.get_root_val())
                raise ValueError('Правый потомок должен быть больше родительского узла или равен ему!')
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
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


'''r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(4)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())'''

answer = input('Введите корень бинарного дерева: ')
r = BinaryTree(int(answer))
while answer != '#':
    answer = input('Выберите действие: \nДля ввода левого узла нажмите "l", \nдля ввода правого '
                   'узла нажмите "r", \nдля выхода нажмите "#": ')

    if answer == 'l':
        try:
            val = int(input('Введите значение: '))
            r.insert_left(val)
        except ValueError:
            print('Значение левого потомка должно быть меньше значения родительского узла '
                  '\nи больше следующего левого потомка!\n')
        else:
            print(r.get_left_child())
            print('Успешно')

    elif answer == 'r':
        try:
            val = input('Введите значение: ')
            r.insert_right(int(val))
        except ValueError:
            print('Значение правого потомка должно быть больше значения родительского узла или равно ему '
                  '\nи меньше значения следующего правого потомка!\n')
        else:
            print(r.get_right_child())
            print('Успешно')

print('Программа завершена')


"""
Новая версия программы проверяет вводимые данные на соответствие правилам построения бинарного дерева.
Она не только сравнивает потомка со значением родительского узла, но и с введенным ранее дочерним потомком, 
который должен стать потомком нового узла.
Реализован клиентский код для проверки правильности работы программы с данной доработкой.

"""
