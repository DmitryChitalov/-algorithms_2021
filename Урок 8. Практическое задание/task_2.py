"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""
'''
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


r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())
r.insert_left(40)
print(r.get_left_child())
print(r.get_left_child().get_root_val())
r.insert_right(12)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
'''

class BinaryTree:
    def __init__(self, root_obj):

        self.root = root_obj   # root***корень
        self.left_child = None  # left descendant***левый потомок
        self.right_child = None   # right descedant***правый потомок

    def insert_left(self, new_node):      # adding a left child***добавление левого потомка
        try:
            if self.root >= new_node:       # if the node has no left child***если у узла нет левого потомка
                if self.left_child == None:     # тогда узел просто вставляется в дерево, формируется новое поддерево
                    self.left_child = BinaryTree(new_node)
                else:                                        # если у узла есть левый потомок
                    tree_obj = BinaryTree(new_node)   # тогда вставляем новый узел
                    tree_obj.left_child = self.left_child   # и спускаем имеющегося потомка на один уровень ниже
                    self.left_child = tree_obj
            else:
                raise Exception('Insertion direction error***Ошибка направления вставки')
        except Exception as ex:
            print(ex)

    def insert_right(self, new_node):  # добавить правого потомка
        try:
            if self.root <= new_node:
                if self.right_child == None:    # если у узла нет правого потомка
                    self.right_child = BinaryTree(new_node)  # узел просто вставляется в дерево формируется новое поддерево
                else:                                       # если у узла есть правый потомок
                    tree_obj = BinaryTree(new_node)  # тогда вставляем новый узел
                    tree_obj.right_child = self.right_child  # и спускаем имеющегося потомка на один уровень ниже
                    self.right_child = tree_obj
            else:
                raise Exception('Insertion direction error***Ошибка направления вставки')
        except Exception as ex:
            print(ex)

    def get_right_child(self):   # метод доступа к правому потомку
        return self.right_child

    def get_left_child(self):    # метод доступа к левому потомку
        return self.left_child

    def set_root_val(self, obj):   # метод установки корня
        self.root = obj

    def get_root_val(self):   # метод доступа к корню
        return self.root


if __name__ == '__main__':
    r = BinaryTree(15)
    print(f'Root value***Значение корня: {r.get_root_val()}')
    print(f'Left child value***Значение левого потомка: {r.get_left_child()}')
    print(f'Right child value***Значение правого потомка: {r.get_right_child()}')
    print('!!' * 50)

    r.insert_right(10) # добавление правого потомка значение меньше корня,ошибку о неверном направлении вставки

    print('!!' * 50)

    r.insert_left(2)                                         # добавление левого потомка
    print(f'Left child value***Значение левого потомка: {r.get_left_child()}')
    print(f'The value of the root of the left child**Значение корня левого потомка: '
          f'{r.get_left_child().get_root_val()}')
    print('**' * 50)

    r.insert_left(6)                                       # добавление еще одного левого потомка
    print(f'Left child value***Значение левого потомка: {r.get_left_child()}')
    print(f'The value of the root of the left child***Значение корня левого потомка: '
          f'{r.get_left_child().get_root_val()}')
    print('!!' * 50)

    r.insert_left(42)          # добавление левого потомка больше корня,ошибка о неверном направлении вставки

    print('!!' * 50)

    r.insert_right(25)                                 # добавление правого потомка
    print(f'Right child value***Значение правого потомка: {r.get_right_child()}')
    print(f'The value of the root of the right child***Значение корня правого потомка:'
          f' {r.get_right_child().get_root_val()}')

    r.insert_right(27) # добавление правого потомка
    print(f'Right child value***Значение правого потомка: {r.get_right_child()}')
    print(f'The value of the root of the right child***Значение корня правого потомка: '
          f'{r.get_right_child().get_root_val()}')
    print('**' * 50)

    print(f'Left child value***Значение левого потомка: {r.get_left_child()}')
    print(f'The value of the root of the left child**Значение корня левого потомка: '
          f'{r.get_left_child().get_root_val()}')
    print('**' * 50)

    r.get_left_child().set_root_val(8)                   # установление корня левого потомка
    print(f'The value of the root of the left child***Значение корня левого потомка: '
          f'{r.get_left_child().get_root_val()}')

    '''
    C:\Users\79115\AppData\Local\Programs\Python\Python39\python.exe "C:/Users/79115/Desktop/2 Урок Алгоритмы/Урок 2. Коды примеров + Все домашки/Algorithm8.2.py"
Root value***Значение корня: 15
Left child value***Значение левого потомка: None
Right child value***Значение правого потомка: None
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Insertion direction error***Ошибка направления вставки
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Left child value***Значение левого потомка: <__main__.BinaryTree object at 0x000001E5E3105BE0>
The value of the root of the left child**Значение корня левого потомка: 2
****************************************************************************************************
Left child value***Значение левого потомка: <__main__.BinaryTree object at 0x000001E5E3105A00>
The value of the root of the left child***Значение корня левого потомка: 6
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Insertion direction error***Ошибка направления вставки
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
Right child value***Значение правого потомка: <__main__.BinaryTree object at 0x000001E5E3105940>
The value of the root of the right child***Значение корня правого потомка: 25
Right child value***Значение правого потомка: <__main__.BinaryTree object at 0x000001E5E31058E0>
The value of the root of the right child***Значение корня правого потомка: 27
****************************************************************************************************
Left child value***Значение левого потомка: <__main__.BinaryTree object at 0x000001E5E3105A00>
The value of the root of the left child**Значение корня левого потомка: 6
****************************************************************************************************
The value of the root of the left child***Значение корня левого потомка: 8

Process finished with exit code 0

    '''
