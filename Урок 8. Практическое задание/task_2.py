"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева).

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""
class Reiteration(Exception):
    pass


class BinaryTree:
    def __init__(self, root_obj):
        # корень
        self.root = root_obj
        # левый потомок
        self.le = None
        # правый потомок
        self.ri = None

    def insert(self, new_node):
        # при попытке добавить число, которое уже присутствует в дереве, выпадает ошибка
        if self.root == new_node:
            raise Reiteration('Корень уже присутствует в дереве')
        # если число меньше текущего корня, то отправляем его в левую ветвь
        if self.root > new_node:
            # если левого потомка нет, то вставляем это число на его место
            if self.le == None:
                self.le = BinaryTree(new_node)
            else:
                # если потомок есть, передаем ему число для вставки рекурсией
                return self.le.insert(new_node)
        # если потомок больше текущего корня, то отправляем его в правую ветвь
        if self.root < new_node:
            # если правого потомка нет, то вставляем это число на его место
            if self.ri == None:
                self.ri = BinaryTree(new_node)
            # иначе передаем число правому потомку для сравнения, и вставки
            else:
                return self.ri.insert(new_node)

    # метод доступа к правому потомку
    def get_right_child(self):
        return self.ri

    # метод доступа к левому потомку
    def get_left_child(self):
        return self.le

    # метод доступа к корню
    def get_root_val(self):
        return self.root


a = BinaryTree(20)
a.insert(10)
a.insert(21)
a.insert(15)
a.insert(17)
a.insert(18)
a.insert(13)
print(a.le.root)

my_dict = {}


def rect(a, my_dict):
    if isinstance(a, BinaryTree):
        my_dict[a.root] = []
        if a.le:
            my_dict[a.root] += [f'левый потомок: {a.le.root}']
        if a.ri:
            my_dict[a.root] += [f'правый потомок: {a.ri.root}']
        rect(a.le, my_dict)
        rect(a.ri, my_dict)
    return my_dict
print(my_dict)
[print(f'{i}: {my_dict[i]}') for i in rect(a, my_dict)]


"""
В этом задании я изменил способ добавления элементов в дерево, теперь пользователь не выбирает, в правую или
левую ветку добавить элемент, это происходит автоматически, исключая вощможные ошибки при построениеи.
При попытке добавить уже имеющиеся в дереве число будет отправлена ошибка с сообщением. Для удобной визуализации
дерева создана функция rect(a, my_dict).
"""
