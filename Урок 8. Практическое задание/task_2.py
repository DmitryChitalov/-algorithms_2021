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

    # Сделал вставку элемента с рекурсией, чтобы программа сам определяла куда ставить потомка
    def insert_node(self, new_node):
        # Если новый потомок меньше, вставляем влево
        if new_node < self.root:
            # если у узла нет левого потомка
            if self.left_child is None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(new_node)
            # если у узла есть левый потомок, определяем выше новый должен быть или ниже
            else:
                if new_node > self.left_child.get_root_val():
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(new_node)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.left_child = self.left_child
                    self.left_child = tree_obj
                elif new_node < self.left_child.get_root_val():
                    # То рекурсией ставим нового вниз
                    self.left_child.insert_node(new_node)
        # Если потомок больше соответственно вправо
        elif new_node > self.root:
            # если у узла нет правого потомка
            if self.right_child is None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.right_child = BinaryTree(new_node)
            # если у узла есть правый потомок, снова определяем где стоять новому
            else:
                if new_node < self.right_child.get_root_val():
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(new_node)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
                elif new_node > self.right_child.get_root_val():
                    # Соответственно вставляем нового ниже рекурсионно
                    self.right_child.insert_node(new_node)

    # метод доступа к правому потомку
    def get_right_child(self):
        try:
            if self.right_child is None:
                raise Exception("Нет правого потомка")
            else:
                return self.right_child
        except Exception as error:
            print(f"{error}")

    # метод доступа к левому потомку
    def get_left_child(self):
        try:
            if self.left_child is None:
                raise Exception("Нет левого потомка")
            else:
                return self.left_child
        except Exception as error:
            print(f"{error}")

    # метод установки корня
    def set_root_val(self, obj):
        self.root = obj

    # метод доступа к корню
    def get_root_val(self):
        return self.root


r = BinaryTree(40)
print(r.get_root_val())  # 40
r.insert_node(20)
r.insert_node(10)
print(r.get_left_child().get_root_val())  # 20
print(r.get_left_child().get_left_child().get_root_val())  # 15
r.insert_node(70)
r.insert_node(83)
r.insert_node(50)
print(r.get_right_child().get_root_val())  # 50
print(r.get_right_child().get_right_child().get_root_val())  # 70
print(r.get_right_child().get_right_child().get_right_child().get_root_val())  # 83
"""
Не знаю насколько это хорошо, но как видно из результатов моя универсальная вставка в дерево вполне работает.
Единственное, если мы хотим в левого потомка вставить правого, или наоборот это придется делать более точечно (ибо
алгоритм работает как бы по вертикали), например:
"""
r.get_right_child().insert_node(45)
print(r.get_right_child().get_left_child().get_root_val())  # 45
