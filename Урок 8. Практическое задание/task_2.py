"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class ChangeDirection(Exception):
    def __init__(self, new_node, root, branch):
        side_one, side_two, compare_sign = ['left', 'right', '>'] if branch == 'left' else ['right', 'left', '<=']
        self.msg = f'Значение {new_node} {compare_sign} {root} --> {side_one} заменен на {side_two}'


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
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # если новое значение больше значения узла и добавляется в левую сторону, то меняем направление на право
            # формируется новое поддерево
            try:
                if new_node >= self.root:
                    raise ChangeDirection(new_node, self.root, 'left')
            except ChangeDirection as err:
                print(err.msg)
                self.right_child = BinaryTree(new_node)
            else:
                self.left_child = BinaryTree(new_node)

        # если у узла есть левый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            try:
                if new_node >= self.root:
                    raise ChangeDirection(new_node, self.root, 'left')
            except ChangeDirection as err:
                print(err.msg)
                tree_obj.right_child = self.left_child
                self.left_child = tree_obj
            else:
                tree_obj.left_child = self.left_child
                self.left_child = tree_obj

    # добавить правого потомка
    def insert_right(self, new_node):
        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            try:
                if new_node < self.root:
                    raise ChangeDirection(new_node, self.root, 'right')
            except ChangeDirection as err:
                print(err.msg)
                self.left_child = BinaryTree(new_node)
            else:
                self.right_child = BinaryTree(new_node)
        # если у узла есть правый потомок
        else:
            # тогда вставляем новый узел
            tree_obj = BinaryTree(new_node)
            # и спускаем имеющегося потомка на один уровень ниже
            try:
                if new_node < self.root:
                    raise ChangeDirection(new_node, self.root, 'left')
            except ChangeDirection as err:
                print(err.msg)
                tree_obj.left_child = self.right_child
                self.right_child = tree_obj
            else:
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


# --- Проверка результатов:

# 1. Проверка валидации значений - 40 должно добавиться в правку ветку, а не в левую
r = BinaryTree(8)
print(r.get_root_val())
print(r.get_left_child())   # пока пустая ветка
r.insert_left(40)           # Значение 40 > 8 --> left заменен на right
print(r.get_right_child())   # <__main__.BinaryTree object at 0x0000018D37850EE0>
print(r.get_right_child().get_root_val())   # 40
del r


# ---- 2. Ручной вариант добавления данных в дерево
# Взят пример из задания для демонстрации вывода результата

r = BinaryTree(8)

# --- Пройдемся по левой части дерева
r.insert_left(1)
r.insert_left(2)
r.insert_left(4)

# 2 ---> 1 - 3
test_root = r.left_child.left_child
print('2 -- ', test_root.get_root_val())  # 2
test_root.insert_right(3)  # 3

# 4 ---> 6
test_root = r.left_child
print('4 -- ', test_root.get_root_val())  # 4
test_root.insert_right(6)  # 6
test_root.right_child.insert_right(7)
test_root.right_child.insert_left(5)

# --- Пройдемся по правой части дерева
r.insert_right(15)
r.insert_right(14)
r.insert_right(12)

# 2 ---> 1 - 3
test_root = r.right_child.right_child
print('14 -- ', test_root.get_root_val())  # 14
test_root.insert_left(13)  # 13

# 10 --- 9 - 11
test_root = r.right_child
print('12 -- ', test_root.get_root_val())  # 12
test_root.insert_left(10)  # 10
test_root.left_child.insert_right(11)
test_root.left_child.insert_left(9)
#  test_root.left_child.left_child.insert_left(6)

test_root = r.right_child.right_child.left_child
print('13 -- ', test_root.get_root_val())  # 9
test_root = r.right_child.left_child.left_child
print('9 -- ', test_root.get_root_val())  # 9


# ---- 3. Красивый вывод данных

# Создадм словарь для хранения данных
code_tree = dict()


def view_tree(tree, level=1):
    """
    Функция заполняет словарь данными из дерева по уровням
    :param tree:  дерево в виде созданного класса
    :param level: уровень
    """
    if tree is None:
        return None
    else:
        if code_tree.get(level) is None:
            code_tree[level] = [tree.get_root_val()]
        else:
            f = code_tree.get(level)
            f.append(tree.get_root_val())
        view_tree(tree.left_child, level + 1)
        view_tree(tree.right_child, level + 1)

# Заполним словарь


view_tree(r)

print(code_tree)  # выведем полученный словарь в одну строку


#  сделаем понятную визуально структуру дерева (упрощенный вариант вывода)
level_in_tree = max([i for i in code_tree]) - 1
max_num_val = 2**level_in_tree
for key, val in code_tree.items():
    g = '\t\t' * (max_num_val // len(val))
    print(f'{key})', '\t\t' * (max_num_val // len(val) // 2), g.join(map(str, val)))

"""
Получается вот такой результат, что удобно для проверки и добавления данных:

1) 								 8
2) 				 4								12
3) 		 2				6				10				14
4)  1		3		5		7		9		11		13		15
"""
