"""Вот мой вариант оптимизации данной программы: добавление
try except в функции добавления правого и левого потомка,
для того чтобы избежать ошибку направления вставки"""
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
            if self.root >= new_node:
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
                raise Exception('Ошибка направления вставки')
        except Exception as ex:
            print(ex)

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if self.root <= new_node:
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
                raise Exception('Ошибка направления вставки')
        except Exception as ex:
            print(ex)

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


if __name__ == '__main__':
    r = BinaryTree(15)
    print(f'Корень: {r.get_root_val()}')
    print(f'Левый потомок: {r.get_left_child()}')
    print(f'Правый потомок: {r.get_right_child()}')
    print('=' * 100)

    r.insert_right(10)

    r.insert_left(2)
    print(f'Левый потомок: {r.get_left_child()}')
    print(f'Значение корня левого потомка: {r.get_left_child().get_root_val()}')
    print('=' * 100)

    r.insert_left(6)
    print(f'Левый потомок: {r.get_left_child()}')
    print(f'Значение корня левого потомка: {r.get_left_child().get_root_val()}')
    print('=' * 100)

    r.insert_left(42)

    r.insert_right(25)
    print(f': {r.get_right_child()}')
    print(f'Значение корня правого потомка: {r.get_right_child().get_root_val()}')

    r.insert_right(27)
    print(f'Правый потомок: {r.get_right_child()}')
    print(f'Значение корня правого потомка: {r.get_right_child().get_root_val()}')
    print('=' * 100)

    print(f'Левый потомок: {r.get_left_child()}')
    print(f'Значение корня левого потомка: {r.get_left_child().get_root_val()}')
    print('=' * 100)

    r.get_left_child().set_root_val(8)
    print(f'Значение корня левого потомка: {r.get_left_child().get_root_val()}')