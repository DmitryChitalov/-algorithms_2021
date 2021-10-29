"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""

from accessify import protected


class BinaryTree:
    def __init__(self, root_obj):
    def __init__(self, root_obj, path='root'):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None
        # путь
        self.path = path

    # добавить потомка
    def insert_child(self, root_obj, path='root'):
        # разделяем от корня на левую или правую ветки
        if root_obj >= self.root:
            self.insert_right(root_obj, path)
        else:
            self.insert_left(root_obj, path)

    # добавить левого потомка
    def insert_left(self, new_node):
    @protected
    def insert_left(self, new_node, path):
        # если у узла нет левого потомка
        if self.left_child == None:
        path = f'{path}-l'
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
            self.left_child = BinaryTree(new_node, path=path)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = self.left_child
            self.left_child = tree_obj
            old_node = self.get_left_child()
            # большие или равные идут направо
            if new_node >= old_node.root:
                old_node.insert_right(new_node, path)
            else:  # остальные налево
                old_node.insert_left(new_node, path)
    # добавить правого потомка
    def insert_right(self, new_node):
    @protected
    def insert_right(self, new_node, path):
        path = f'{path}-r'
        # если у узла нет правого потомка
        if self.right_child == None:
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
            self.right_child = BinaryTree(new_node, path=path)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = self.right_child
            self.right_child = tree_obj
            old_node = self.get_right_child()
            # большие или равные идут направо
            if new_node >= old_node.root:
                old_node.insert_right(new_node, path)
            else:  # остальные налево
                old_node.insert_left(new_node, path)

    # метод доступа к правому потомку
    def get_right_child(self):
@@ -65,15 +84,51 @@ def set_root_val(self, obj):
    def get_root_val(self):
        return self.root

    def __str__(self):
        return f'{self.path}: {self.root}'

    # поиск элемента по значению
    def find_el(self, node):
        try:
            if node == self.root:
                print(self)
            elif node >= self.root:
                new_self = self.get_right_child()
                new_self.find_el(node)
            else:
                new_self = self.get_left_child()
                new_self.find_el(node)
        except AttributeError:
            print(f'Значение {node} отсутствует')


r = BinaryTree(8)
r = BinaryTree(10)
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
r.insert_child(40)
print(f'{r.get_right_child()}')
r.insert_child(3)
print(f'{r.get_left_child()}')
r.insert_child(5)
print(f'{r.get_left_child().get_right_child()}')
r.insert_child(15)
print(f'{r.get_right_child().get_left_child()}')
r.insert_child(45)
print(f'{r.get_right_child().get_right_child()}')
r.insert_child(12)
r.insert_child(30)
print(f'{r.get_right_child().get_left_child().get_right_child()}')
print(f'{r.get_right_child().get_left_child().get_left_child()}')
r.insert_child(41)
print(f'{r.get_right_child().get_right_child().get_left_child()}')
r.insert_child(31)
print(f'{r.get_right_child().get_left_child().get_right_child().get_right_child()}')
r.find_el(12)
r.find_el(7)


"""
Оптимизация заключается в предоставлении пользователю добавление методом insert_child, который определяет ветвь 
самостоятельно и вызывает рекурсивно методы insert_right и insert_left и они определяют место в дереве. 
Атрибут path создан для проверки правильности построения узлов и просмотра пути размещения узла.
"""