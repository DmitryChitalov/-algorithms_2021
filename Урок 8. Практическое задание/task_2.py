"""
Задание 2.

Доработайте пример структуры "дерево",
рассмотренный на уроке.

Предложите варианты доработки и оптимизации
(например, валидация значений узлов в соответствии с требованиями для бинарного дерева)

Поработайте с доработанной структурой, позапускайте на реальных данных - на клиентском коде.
"""


# своё исключение для левого ребёнка
class ErrorLeft(Exception):
    def __init__(self, text):
        self.text = text


# своё исключение для правого ребёнка
class ErrorRight(Exception):
    def __init__(self, text):
        self.text = text


# создаём бинарное дерево
class BinaryWood:
    def __init__(self, base_ent):
        self.base = base_ent  # корень
        self.left_kid = 'empty'  # левый ребёнок
        self.right_kid = 'empty'  # правый ребёнок

    # добавить левого потомка
    def paste_left(self, new_knot):
        if self.left_kid == 'empty':
            if new_knot > self.base:
                raise ErrorLeft('Левый ребёнок должен быть меньше корня!')
            else:
                self.left_kid = BinaryWood(new_knot)
        else:
            if new_knot > self.base:
                raise ErrorLeft('Левый ребёнок должен быть меньше корня!')
            else:
                wood_ent = BinaryWood(new_knot)
                wood_ent.left_kid = self.left_kid
                self.left_kid = wood_ent

    # добавить правого ребёнка
    def paste_right(self, new_knot):
        if self.right_kid == 'empty':
            if new_knot < self.base:
                raise ErrorRight('Правый ребёнок должен быть больше корня!')
            else:
                self.right_kid = BinaryWood(new_knot)
        else:
            if new_knot < self.base:
                raise ErrorRight('Правый ребёнок должен быть больше корня!')
            else:
                wood_ent = BinaryWood(new_knot)
                wood_ent.right_kid = self.right_kid
                self.right_kid = wood_ent

    # метод доступа к правому потомку
    def take_right_kid(self):
        return self.right_kid

    # метод доступа к левому ребёнку
    def take_left_kid(self):
        return self.left_kid

    # метод установки корня
    def install_base(self, ent):
        self.base = ent

    # метод доступа к корню
    def take_base(self):
        return self.base


w = BinaryWood(12)
print(w.take_base())

print(w.take_left_kid())
w.paste_left(13)
print(w.take_left_kid())
print(w.take_left_kid().take_base())

'''
Манипуляции выше вызовут данную ошибку так как левый потомок должен быть меньше корня,
а в данном случае он больше.

raise Error_left('Левый ребёнок должен быть меньше корня!')
__main__.Error_left: Левый ребёнок должен быть меньше корня!
'''

w.paste_right(11)
print(w.take_right_kid())
print(w.take_right_kid().take_base())

'''
Манипуляции выше вызовут данную ошибку так как правый потомок должен быть больше корня,
а в данном случае он меньше.

raise Error_right('Правый ребёнок должен быть больше корня!')
__main__.Error_right: Правый ребёнок должен быть больше корня!
'''

print(w.take_left_kid())
w.paste_left(8)
print(w.take_left_kid())
print(w.take_left_kid().take_base())
w.paste_right(13)
print(w.take_right_kid())
print(w.take_right_kid().take_base())
w.take_right_kid().install_base(26)
print(w.take_right_kid().take_base())

'''
Манипуляции выше не вызовут исключений так как по условию потомки добавлялись
верно.

12
empty
<__main__.BinaryWood object at 0x7f9b9b6c0a60>
8
<__main__.BinaryWood object at 0x7f9b9b63f310>
13
26
'''
