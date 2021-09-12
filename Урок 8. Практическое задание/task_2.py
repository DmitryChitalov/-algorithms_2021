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

    # добавить потомка
    def insert_child(self, new_node):
        # определим в какую из веток должен пойти потомок (левую или правую)
        if new_node < self.root:
            self.insert_left(new_node)
        elif new_node > self.root:
            self.insert_right(new_node)
        else:
            raise Exception('Нельзя добавить узел сам в себя!')

    # добавить левого потомка
    def insert_left(self, new_node):
        # если у узла нет левого потомка
        if self.left_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.left_child = BinaryTree(new_node)
        # если у узла есть левый потомок
        else:
            # если левый потомок меньше вставляемого узла
            if self.get_left_child().get_root_val() < new_node:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
            # если левый потомок больше вставляемого узла
            else:
                raise Exception(f'Нельзя добавить потомка {new_node} к узлу {self.root}, т.к. у него уже есть потомок '
                      f'{self.get_left_child().get_root_val()}, больший добавляемого!')

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child == None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # если правый потомок больше вставляемого узла
            if self.get_right_child().get_root_val() > new_node:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
            # если правый потомок меньше вставляемого узла
            else:
                raise Exception(f'Нельзя добавить потомка {new_node} к узлу {self.root}, т.к. у него уже есть потомок '
                      f'{self.get_right_child().get_root_val()}, меньший добавляемого!')

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


print('Создаем корень 8.')
r = BinaryTree(8)
print(f'Значение корня = {r.get_root_val()}')
print(f'Левый потомок = {r.get_left_child()}')
print(f'Правый потомок = {r.get_right_child()}')

print('Пробуем добавить потомка равного также 8.')
try:
    r.insert_child(8)
    print(r.get_left_child())
    print(r.get_left_child().get_root_val())
except Exception as e:
    print(e)
print(f'Левый потомок = {r.get_left_child()}')
print(f'Правый потомок = {r.get_right_child()}')
print('Потомок не добавился. Ошибка обработалась.')


print('Пробуем добавить потомка равного 4.')
try:
    r.insert_child(4)
    print(r.get_left_child())
    print(r.get_left_child().get_root_val())
except Exception as e:
    print(e)
print(f'Левый потомок = {r.get_left_child()}')
print(f'Правый потомок = {r.get_right_child()}')
print('Потомок успешно добавился слева. Ошибка не возникла.')


print('Пробуем добавить потомка равного 6.')
try:
    r.insert_child(6)
    print(r.get_left_child())
    print(r.get_left_child().get_root_val())
    print(r.get_left_child().get_left_child())
    print(r.get_left_child().get_left_child().get_root_val())
except Exception as e:
    print(e)
print(f'Левый потомок корня = {r.get_left_child()}')
print(f'Правый потомок корня = {r.get_right_child()}')
print('Потомок успешно добавился слева. Ошибка не возникла.')
print(f'Левый потомок левого потомка корня = {r.get_left_child().get_left_child().get_root_val()}')


print('Пробуем добавить потомка равного 5.')
try:
    r.insert_child(5)
    print(r.get_left_child())
    print(r.get_left_child().get_root_val())
except Exception as e:
    print(e)
print(f'Левый потомок корня = {r.get_left_child()}')
print(f'Правый потомок корня = {r.get_right_child()}')
print('Потомок не добавился. Ошибка обработалась.')
print(f'Левый потомок корня = {r.get_left_child().get_root_val()}')
print(f'Левый потомок левого потомка корня = {r.get_left_child().get_left_child().get_root_val()}')

print('Пробуем добавить потомка равного 12.')
try:
    r.insert_child(12)
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
except Exception as e:
    print(e)
print(f'Левый потомок = {r.get_left_child()}')
print(f'Правый потомок = {r.get_right_child()}')
print('Потомок успешно добавился справа. Ошибка не возникла.')

print('Пробуем добавить потомка равного 10.')
try:
    r.insert_child(10)
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
    print(r.get_right_child().get_right_child())
    print(r.get_right_child().get_right_child().get_root_val())
except Exception as e:
    print(e)
print(f'Левый потомок корня = {r.get_left_child()}')
print(f'Правый потомок корня = {r.get_right_child()}')
print('Потомок успешно добавился справа. Ошибка не возникла.')
print(f'Правый потомок правого потомка корня = {r.get_right_child().get_right_child().get_root_val()}')


print('Пробуем добавить потомка равного 11.')
try:
    r.insert_child(11)
    print(r.get_right_child())
    print(r.get_right_child().get_root_val())
except Exception as e:
    print(e)
print(f'Левый потомок корня = {r.get_left_child()}')
print(f'Правый потомок корня = {r.get_right_child()}')
print('Потомок не добавился. Ошибка обработалась.')
print(f'Левый потомок корня = {r.get_left_child().get_root_val()}')
print(f'Левый потомок левого потомка корня = {r.get_left_child().get_left_child().get_root_val()}')
print(f'Правый потомок корня = {r.get_right_child().get_root_val()}')
print(f'Правый потомок правого потомка корня = {r.get_right_child().get_right_child().get_root_val()}')

"""
Добавил в код анализ добавления новых потомков - автоматически определяется ветка, куда следует его добавить.
Добавил обработку ситуации, когда пытаются добавить потомка с тем же значением, что и у корня.
Добавил обработку ситуаций, когда пытаются добавить потомка не на свое место (например, 5 между 8 и 6)
Код программы намеренно сделал не самым оптимальным ради более наглядного вывода результата в консоль.
"""
