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

    # data access method
    def get_root_data(self):
        return self.data

    def is_node_inside(self, idx_node, start_root):
        '''
        Находим объект корневго узла, по индексу
        :param idx_node:
        :param start_root:
        :return: кортеж (флагпоиска, объект Binarytree), если не нашли, то (False, None)
        '''
        if idx_node < start_root.root  and start_root.get_left_child():
            return self.is_node_inside(idx_node, start_root.get_left_child())
        elif idx_node > start_root.root and start_root.get_right_child():
            return self.is_node_inside(idx_node, start_root.get_right_child())
        else:
            if idx_node == start_root.get_root_val():
                return True, start_root
            else:
                return False, None

    def is_node_exists(self, node):
        '''
        Возвращаем True если узел с таким номером существует. Можно использовать при
        создании новых узлов, когда не знаем есть ли очередной номер в дереве.
        :param node:
        :return:
        '''
        return self.is_node_inside(node, self)[0]

    def get_node_data(self, idx_node):
        '''
        Получить атрибут data
        :param idx_node:
        :return:
        '''
        found, obj = self.is_node_inside(idx_node, self)
        return obj.data if found else None

    def set_node_data(self, idx_node, data=''):
        '''
        Меняем атрибут data узла
        :param idx_node:
        :param data:
        :return: Узел куда вставляем, или None если узел не найден
        '''
        found, obj = self.is_node_inside(idx_node, self)
        if found:
            obj.data = data
        return obj if found else None

r = BinaryTree(8)
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
print(r)
print('*****************************')
print(r.is_node_exists(8))
print(r.is_node_exists(1))
print(r.is_node_exists(100))
print(r.is_node_exists(40))
print(r.get_node_data(25))
r.set_node_data(25, 'OCTOBER')
print(r.get_node_data(25))

'''
Выводы:
1. Бинарное дерево несложный, и весьма эффективный инструмент для работы с уникальными данными
например индексы
2. Оптимимзация выполнена:
- создан унифицированный метод для вставки в двоичное дерево нового элемента в правильное место.
- добавлен атрибут узла data
- добавлены методы получения значения узла по индексу и изменения атрибута data узла
- удалить ненужные методы не получилось.
3. реализация мне кажется корявенькой. видимо надо потренироваться на написании лакончиного кода ООП
4. метод insert_element сочетает в себе ООП и функциональное программирование в части рекурсии.
как этого избежать не додумался.
5. для визуализации дерева переписан метод __str__
6. вызывает исключение в методе insert_element в случае, дублирования индекса.

В листинге:
- последовательное создание дерева


(R8 L* R*)
(R8 L(R6 L* R*) R*)
(R8 L(R6 L* R*) R(R100 L* R*))
(R8 L(R6 L* R(R7 L* R*)) R(R100 L* R*))
(R8 L(R6 L(R1 L* R*) R(R7 L* R*)) R(R100 L* R*))
(R8 L(R6 L(R1 L* R*) R(R7 L* R*)) R(R100 L(R50 L* R*) R*))
(R8 L(R6 L(R1 L* R*) R(R7 L* R*)) R(R100 L(R50 L(R25 L* R*) R*) R*))
(R8 L(R6 L(R1 L* R*) R(R7 L* R*)) R(R100 L(R50 L(R25 L* R*) R*) R(R200 L* R*)))
*****************************
True
True
True
False
SEPTEMBER
OCTOBER
'''
