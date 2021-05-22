"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.

***************************************************************************************

1. В структуру данных добавлена ссылка на родителя и метод его получения.
2. Убрана вставка левого/правого узла. Теперь новый элемент вставляется
в дерево автоматически определяя своё место.
3. Добавлен метод поиска узла в дереве.
4. Добавлен метод для получения высоты дерева.
5. Добавлена проверка узла на сбалансированность.
(По умолчанию проверяет узел из которого вызываетя, или ищет узел по значению)
"""


class BinaryTree:

    def __init__(self, root_obj, parent=None):
        self.parent = parent
        self.value = root_obj
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return f'Node[{self.value}]'

    # вставляем новый узел
    def insert_node(self, val):
        # если значение равно текущему ничего не меняем
        if val == self.value:
            self.value = val
        # если новое значение меньше значения текущего узла
        elif val < self.value:
            # вставляем значение в левое поддерево
            if not self.left_child:
                self.left_child = BinaryTree(val, self)
            else:
                self.left_child.insert_node(val)
        else:
            # иначе вставляем значение в правое поддерево
            if not self.right_child:
                self.right_child = BinaryTree(val, self)
            else:
                self.right_child.insert_node(val)

    # проверяем наличие узла в дереве
    # возвращаем узел, если он есть или None
    def find_node(self, val):
        if val == self.value:
            return self
        try:
            if val < self.value:
                return self.left_child.find_node(val)
            return self.right_child.find_node(val)
        except AttributeError:
            return

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def get_value(self):
        return self.value

    # получаем родителя
    def get_parent(self):
        return self.parent

    # проверяем наличие потомков
    def has_children(self):
        return self.left_child or self.right_child

    # получаем высоту дерева
    def get_height(self):
        left_height = self.left_child.get_height() if self.left_child else 0
        right_height = self.right_child.get_height() if self.right_child else 0
        return max(left_height, right_height) + 1

    # является ли узел сбалансированным
    def is_balanced(self, val=None):
        if val:
            node = self.find_node(val)
        else:
            node = self
        if node:
            left_height = node.left_child.get_height() if node.left_child else 0
            right_height = node.right_child.get_height() if node.right_child else 0
            return abs(left_height - right_height) <= 1
        raise ValueError('неверное значение узла')


if __name__ == '__main__':

    # заполняем дерево
    r = BinaryTree(8)
    r.insert_node(5)
    r.insert_node(3)
    r.insert_node(1)
    r.insert_node(15)
    r.insert_node(6)

    # Выводим на экран
    print(r)                                        # корень - Node[8]
    print(r.left_child, r.right_child)              # левого и правого потомка - Node[5] Node[15]
    print(r.find_node(1).get_parent())              # родителя для узла 1 - Node[3]
    print(r.find_node(15).get_left_child())         # левого потомка узла 15 - None
    print(r.get_height())                           # получаем высоту дерева - 4

    # проверяем сбалансированность
    print(r.is_balanced(15))                        # узла 15 - True
    print(r.get_right_child().is_balanced())        # правого потомка корня - True
    print(r.is_balanced())                          # корня - False
#    print(r.is_balanced(25))                        # вызовет ошибку
