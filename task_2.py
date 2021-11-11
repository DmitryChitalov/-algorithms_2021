"""
Задание 2.
Доработайте пример структуры "дерево",
рассмотренный на уроке.
Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).
Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""
class MyRaise(Exception):
    def __init__(self, text):
        self.text = text



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
            # если у узла нет левого потомка
            if self.left_child == None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.left_child = BinaryTree(new_node)

            elif new_node > self.left_child.get_root_val():
                raise MyRaise(f'Ошибка: число {new_node} не может быть вставленно так'
                              f' как больше текущей вершины {self.left_child.get_root_val()}')

            # если у узла есть левый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj
        except MyRaise as i:
            print(i)


    # добавить правого потомка
    def insert_right(self, new_node):
        try:
            # если у узла нет левого потомка
            if self.right_child == None:
                # тогда узел просто вставляется в дерево
                # формируется новое поддерево
                self.right_child = BinaryTree(new_node)

            elif new_node < self.right_child.get_root_val():
                raise MyRaise(f'Ошибка: число {new_node} не может быть вставленно так'
                              f' как меньше текущей вершины {self.right_child.get_root_val()}')

            # если у узла есть правый потомок
            else:
                # тогда вставляем новый узел
                tree_obj = BinaryTree(new_node)
                # и спускаем имеющегося потомка на один уровень ниже
                tree_obj.right_child = self.right_child
                self.right_child = tree_obj
        except MyRaise as i:
            print(i)


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


r = BinaryTree(20)
"""
В левой части дерева числа добавляются по убыванию
В правой части дерева числа добавляются по возрастанию
"""
print(f'значение корня равно {r.get_root_val()}') # показываю какой корень

print("Работа с левой частью дерева")

print(r.get_left_child())  # показываю что слева пусто
r.insert_left(6) # добавляю
print(f'значение после добавления {r.get_left_child().get_root_val()}')  # показываю что слева
r.insert_left(10) # не могу добавить тк больше ранее добавленного
r.insert_left(5) # могу добавить
print(f'значение после добавления {r.get_left_child().get_root_val()}')

print()

print("Работа с правой частью дерева")

print(r.get_right_child()) # показываю что справа пусто
r.insert_right(22) # добавляю
print(f'значение после добавления {r.get_right_child().get_root_val()}') # показываю значение
r.insert_right(30) # добавляю еще
r.insert_right(25) # не могу добавить
r.get_right_child().set_root_val(16) # меняю корень справа на данное число
print(f'значение после замены корня {r.get_right_child().get_root_val()}')
r.insert_right(25) # не могу добавить
print(f'значение после добавления {r.get_right_child().get_root_val()}')
