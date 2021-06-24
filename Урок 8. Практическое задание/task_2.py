"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""
# Доработал, проверил, можно играться, но чтоб это прикрутить к Хаффману надо знатно потрудиться


class OwnError (Exception):
    def __init__(self, txt):
        self.txt = txt


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
            if self.root < new_node:
                raise OwnError(f"Левый потомок = {new_node} не может быть больше родителя = {self.root}")
            # если у узла нет левого потомка

            if self.left_child == None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                print(f'Левая ветка отсутствует, лист {new_node} установлен')
                self.left_child = BinaryTree(new_node)
            # если у узла есть левый потомок
            else:
                if self.left_child.get_root_val() < new_node:
                    # тогда вставляем новый узел
                    print(f'Левая ветка существует. Ее голова = {self.left_child} '
                          f'меньше {new_node}, поэтому вставляем выше')
                    tree_obj = BinaryTree(new_node)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.left_child = self.left_child
                else:
                    raise OwnError(f"Левая ветка существует ее корень = {self.left_child.set_root_val()} "
                                   f"больше нашего  = {new_node}, - сюда не вставить")

        except OwnError as err:
            print(err)

    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            if self.root > new_node:
                raise OwnError(f"Левый потомок = {new_node} не может быть больше родителя = {self.root}")
            # если у узла нет правого потомка
            if self.right_child == None:
                print(f'Правая ветка отсутствует, лист {new_node} установлен')
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.right_child = BinaryTree(new_node)
            # если у узла есть правый потомок
            else:
                if self.right_child.get_root_val() < new_node:
                    # тогда вставляем новый узел
                    tree_obj = BinaryTree(new_node)
                    # и спускаем имеющегося потомка на один уровень ниже
                    tree_obj.right_child = self.right_child
                    self.right_child = tree_obj
                else:
                    raise OwnError(f"Правая ветка существует ее корень = {self.right_child.get_root_val()} "
                                   f"больше нашего  = {new_node}, - сюда не вставить")
        except OwnError as err:
            print(err)

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
print(r)
print(r.get_root_val())
print(r.get_left_child())
r.insert_right(40)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.insert_right(12)
r.get_right_child().set_root_val(12)
r.insert_right(40)
print(r.get_right_child())
print(r.get_right_child().get_root_val())
r.get_right_child().set_root_val(16)
print(r.get_right_child().get_root_val())
print(r.get_right_child().get_right_child().get_root_val())
