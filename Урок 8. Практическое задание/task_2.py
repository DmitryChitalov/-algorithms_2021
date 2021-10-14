"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class BinaryTree:
    def __init__(self, root_obj, data=''):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None
        # сохраняем какую-то информацию в узле
        self.data = data

    def __str__(self):
        return f'(R{self.root} ' \
               f'L{self.left_child if self.left_child else "*"} ' \
               f'R{self.right_child if self.right_child else "*"})'

    def insert_element(self, new_root, new_node, data=''):
        tmp=new_root
        if new_node == new_root.root:
            raise Exception(f'Узел с номером {new_node} существует')
            exit(1)
        # если новый элемент меньше значения корня
        elif new_node < new_root.root:
            # check for not None
            if new_root.left_child:
                # jump into child left...
                tmp = self.insert_element(new_root.left_child, new_node, data)
            else:
                # otherwise we achieved last position and can insert new_node and return new_node
                tmp = self.insert_left(new_root, new_node, data)
        else:  # значит новый элемент больше чем значение корня
            # check for not None
            if new_root.right_child:
                # jump into child if necessary
                tmp = self.insert_element(new_root.right_child, new_node, data)
            else:
                # or insert new_node and return new_node object
                tmp = self.insert_right(new_root, new_node, data)
        return tmp

    # добавить левого потомка
    def insert_left(self, new_root, new_node, data=''):
        # если у узла нет левого потомка
        if new_root.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            new_root.left_child = BinaryTree(new_node, data)
        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node, data)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.left_child = new_root.left_child
            new_root.left_child = tree_obj
        # print(f'new_node {new_node} get_root_val {new_root.get_left_child().get_root_val()}')
        return new_root.left_child

    # добавить правого потомка
    def insert_right(self, new_root, new_node, data=''):
        # если у узла нет правого потомка
        if new_root.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            new_root.right_child = BinaryTree(new_node, data)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node, data)
            # и спускаем имеющегося потомка на один уровень ниже
            tree_obj.right_child = new_root.right_child
            new_root.right_child = tree_obj
        # print(f'new_node {new_node} get_root_val {new_root.get_right_child().get_root_val()}')
        return new_root.right_child

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

    def get_node_data(self, root):
        pass

r = BinaryTree(8)
# print(r.get_root_val())
# print(r.get_left_child())
# r.insert_left(40)
# print(r.get_left_child())
# print(r.get_left_child().get_root_val())
# r.insert_right(12)
# print(r.get_right_child())
# print(r.get_right_child().get_root_val())
# r.get_right_child().set_root_val(16)
# print(r.get_right_child().get_root_val())
print(r)
r.insert_element(r, 6)
print(r)
r.insert_element(r, 100)
print(r)
r.insert_element(r, 7)
print(r)
# r.insert_element(r,7) # вознкает ошибка
r.insert_element(r, 1)
print(r)
r.insert_element(r, 50)
print(r)
r.insert_element(r, 25, 'SEPTEMBER')
print(r)
a = r.insert_element(r, 200)
print(a)
print(a.get_root_val())
print(r)


'''
Выводы:
1. Бинарное дерево несложный, и весьма эффективный инструмент для работы с уникальными данными
например индексы
2. Оптимимзация выполнена:
- создан унифицированный метод для вставки в двоичное дерево нового элемента в правильное место.
- код подготвлен для создания метода вытаскивания из дерева данных заданного элемента
-- метода проверки наличия элемента в бинарном дереве.


(R8 L* R*)
(R8 L(R6 L* R*) R*)
(R8 L(R6 L* R*) R(R100 L* R*))
(R8 L(R6 L* R(R7 L* R*)) R(R100 L* R*))
(R8 L(R6 L(R1 L* R*) R(R7 L* R*)) R(R100 L* R*))
(R8 L(R6 L(R1 L* R*) R(R7 L* R*)) R(R100 L(R50 L* R*) R*))
(R8 L(R6 L(R1 L* R*) R(R7 L* R*)) R(R100 L(R50 L(R25 L* R*) R*) R*))
(R200 L* R*)
200
(R8 L(R6 L(R1 L* R*) R(R7 L* R*)) R(R100 L(R50 L(R25 L* R*) R*) R(R200 L* R*)))'''
