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
        # если у узла нет левого потомка
        if self.root >= new_node:
            if self.left_child == None:
                self.left_child = BinaryTree(new_node)
            else:
            # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child_child = tree_obj
        else:
            print ('Ошибка ввода. Левый потомок должен быть меньше предка')


    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.root <= new_node:
            if self.right_child == None:
                self.right_child = BinaryTree(new_node)
            else:
                tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
        else:
            print ('Ошибка ввода. Правый потомок должен быть больше предка')

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
print(f'корень {r.get_root_val()}')
print(f'левый потомок {r.get_left_child()}')
r.insert_left(10)
print(f'левый потомок {r.get_left_child()}')
r.insert_left(6)
print(f'левый потомок {r.get_left_child()}')
print(f'корень левого потомка {r.get_left_child().get_root_val()}')
r.insert_right(12)
print(f'правый потомок {r.get_right_child()}')
print(f'корень правого потомка {r.get_right_child().get_root_val()}')
r.get_right_child().set_root_val(16)
print(f'корень правого потомка {r.get_right_child().get_root_val()}')


"""
Добавил проверку правильности ввода: в левый потом только числа, меньше или равные текущему корню, в правый - 
только больше или равные текущему корню. 

Писал в личку вопрос по получению значения корня ниже, чтобы вставить новый потомок либо влево, либо вправно,
но разобрался. Понял, что подобная проверка будет лишней.
"""