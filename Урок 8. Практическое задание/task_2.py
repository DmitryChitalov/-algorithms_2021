"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


class ValueTooSmallError(Exception):
    """Вызывается, когда входное значение мало"""
    pass


class ValueTooLargeError(Exception):
    """Вызывается, когда входное значение велико"""
    pass


class ValueNotInRange(Exception):
    """Вызывается, когда значение не входит в диапазон"""
    pass


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.left_child = None
        # правый потомок
        self.right_child = None
        # Задаем пределы для левого и правого потомков
        self.left_max_limiter = root_obj
        self.left_min_limiter = None
        self.right_max_limiter = None
        self.right_min_limiter = root_obj

    # добавить левого потомка
    def insert_left(self, new_node):
        if new_node > self.root:
            raise ValueTooLargeError
        tree_obj = BinaryTree(new_node)
        tree_obj.left_min_limiter = self.left_min_limiter
        tree_obj.right_max_limiter = self.root
        # если у узла нет левого потомка
        if self.left_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            if (tree_obj.left_min_limiter is None and new_node <= tree_obj.left_max_limiter) or \
                    (tree_obj.left_min_limiter <= new_node <= tree_obj.left_max_limiter):
                self.left_child = tree_obj
            else:
                raise ValueNotInRange
        # если у узла есть левый потомок
        else:
            tree_obj_2 = BinaryTree(self.left_child)
            # и спускаем имеющегося потомка на один уровень ниже с проверкой, соответствует ли он требованиям
            if self.left_child.root <= new_node and \
                    ((tree_obj.left_min_limiter is None and self.left_child.root <= tree_obj.left_max_limiter) or
                     (tree_obj.left_min_limiter <= self.root <= tree_obj.left_max_limiter)):
                tree_obj_2.left_min_limiter = tree_obj.left_min_limiter
                tree_obj_2.right_max_limiter = tree_obj.root
                tree_obj.left_child = tree_obj_2
            # если старый левый потомок будет больше нового, то он должен стать правым потомком нового
            elif tree_obj.right_min_limiter <= self.left_child.root <= tree_obj.right_max_limiter:
                tree_obj_2.left_min_limiter = tree_obj.root
                tree_obj_2.right_max_limiter = tree_obj.right_max_limiter
                tree_obj.right_child = tree_obj_2
            else:
                raise ValueNotInRange
            self.left_child = tree_obj
            self.left_min_limiter = tree_obj.root

    # добавить правого потомка
    def insert_right(self, new_node):
        if new_node < self.root:
            raise ValueTooSmallError
        tree_obj = BinaryTree(new_node)
        tree_obj.left_min_limiter = self.root
        tree_obj.right_max_limiter = self.right_max_limiter
        # если у узла нет правого потомка
        if self.right_child is None:
            # тогда узел просто вставляется в дерево
            # формируется новое поддерево
            if (tree_obj.right_max_limiter is None and new_node >= tree_obj.left_min_limiter) or \
                    (tree_obj.left_min_limiter <= new_node <= tree_obj.left_max_limiter):
                self.right_child = BinaryTree(new_node)
            else:
                raise ValueNotInRange
        # если у узла есть правый потомок
        else:
            tree_obj_2 = BinaryTree(self.right_child)
            if self.right_child.root >= new_node and \
                    ((tree_obj.right_max_limiter is None and self.right_child.root >= tree_obj.left_min_limiter) or
                     (tree_obj.left_min_limiter <= self.right_child.root <= tree_obj.left_max_limiter)):
                tree_obj_2.left_min_limiter = tree_obj.root
                tree_obj_2.right_max_limiter = tree_obj.right_max_limiter
                tree_obj.right_child = tree_obj_2
            # если старый правый потомок будет меньше нового, то он должен стать левым потомком нового
            elif tree_obj.left_min_limiter <= self.right_child.root <= tree_obj.left_max_limiter:
                tree_obj_2.left_min_limiter = tree_obj.left_min_limiter
                tree_obj_2.right_max_limiter = tree_obj.root
                tree_obj.left_child = tree_obj_2
            else:
                raise ValueNotInRange
            self.right_child = tree_obj
            self.right_max_limiter = tree_obj.root

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


try:
    r = BinaryTree(8)
    r.insert_left(4)
    print(r.get_left_child())
    print(r.get_left_child().get_root_val())
    r.insert_right(12)
    r.insert_right(7)   # тут вызывается ошибка ValueTooSmallError
    r.insert_left(9)    # тут вызывается ошибка ValueTooLargeError
except ValueTooSmallError:
    print("Внимание, число слишком маленькое")
except ValueTooLargeError:
    print("Внимание, число слишком большое")
except ValueNotInRange:
    print("Число не входит в требуемый диапазон")

"""
Добавил лимитеры для правого и левого значения. Минимальный правый и максимальный левый всегда равны корню.
Остальные меняются в зависимости от вводимых условий. Не смог придумать как избежать изменения корня на недопустимое 
значение. Не хватило времени (работа, чтоб ее) и, вероятнее всего, знаний. Классы ошибок сделал для галочки, в теории 
ValueNotInRange излишняя, так как с учетом прочих условий будет сложно вызвать ее.
"""