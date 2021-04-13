"""
Задание 1.
Реализуйте кодирование строки "по Хаффману".
У вас два пути:
1) тема идет тяжело? тогда вы можете, опираясь на пример с урока, сделать свою!!! версию алгоритма
Разрешается и приветствуется изменение имен переменных, выбор других коллекций, различные изменения
и оптимизации.


2) тема понятна? постарайтесь сделать свою реализацию.
Вы можете реализовать задачу, например, через ООП или предложить иной подход к решению.
"""

import random
from collections import Counter, deque


class Tree:
    def __init__(self, key):        # Инициализация класса
        self.key = key              # суммарное значение частоты ниже-расположенных листьев или значение листа
        self.left = None            # левая ветка
        self.right = None           # правая ветка

    def insert(self, value, key):   # добавить элемент лист (value) и учесть его частоту (key)
        # найдем самый малозначимый узел, учитывая глубину узла и значимость вставляемого элемента
        obj, weight = self._find_min_node(key, self, self)
        if obj.left is None:        # если левая ветка пуста, занесем в нее новый экземпляр (такого не произойдет)
            obj.key += key
            obj.left = Tree(value)
        elif obj.right is None:     # если правая ветка пуста, занесем в нее новый экземпляр
            obj.key += key
            obj.right = Tree(value)
        else:                       # обе ветки заняты
            new_obj_l = Tree(0)             # новая ветка для вставки
            new_obj_l.insert(value, key)    # добавим в нее лист
            new_obj_r = Tree(0)             # новая ветка для старого узла
            new_obj_r.key, new_obj_r.left, new_obj_r.right = obj.key, obj.left, obj.right
            obj.key, obj.left, obj.right = obj.key+key, new_obj_l, new_obj_r
        self.key = self._recount_key(self)      # могли "съехать" частоты после вставки элемента - пересчитаем

    def _find_min_node(self, key, obj, min, deep=1, weight=99999):
        # найдем самый малозначимый узел, учитывая глубину узла и значимость вставляемого элемента
        if obj is None:
            return min, weight
        if obj.left is not None or obj.right is not None:       # не лист
            weight_cur = key * deep                             # частота вставляемого элемента с учетом глубины
            if obj.left is not None and obj.right is not None:  # обе ветки заняты
                weight_cur += obj.key + key                     # учтем сдвижку "старой" ветки и нового листа на уровень
            if weight > weight_cur:                             # новая "частота" меньше ранее-найденной
                min = obj
                weight = weight_cur
            min, weight = self._find_min_node(key, obj.left, min, deep+1, weight)
            min, weight = self._find_min_node(key, obj.right, min, deep+1, weight)
        return min, weight

    def _recount_key(self, obj):    # пересчет частот с учетом всех листьев (нужен после вставки)
        if obj is None:
            return 0
        if obj.left is None and obj.right is None:  # лист
            return 0
        key = self._recount_key(obj.left) + self._recount_key(obj.right)
        if key != 0:        # первый узел после листьев берем за отправную точку (key==0)
            obj.key = key
        return obj.key

    def del_empty_branch(self, obj):   # т.к. вставка идет по одному эл., 50% есть узлы с одной веткой - можем сократить
        if obj is None:
            return
        if obj.left is None and obj.right is None:  # лист
            return
        if obj.right is None:                       # пустая ветка
            obj.key = obj.left.key
            obj.right = obj.left.right
            obj.left = obj.left.left
        self.del_empty_branch(obj.left)
        self.del_empty_branch(obj.right)

    def fill_code_dict(self, obj, dict={}, code=''):    # заполнение словаря кодирования
        if obj is None:
            return dict
        if obj.left is None and obj.right is None:      # лист
            dict[obj.key] = code                        # добавим в словарь значение и путь
        else:
            dict = self.fill_code_dict(obj.left, dict, code + '0')  # левые ветки считаем "0"
            dict = self.fill_code_dict(obj.right, dict, code + '1') # правые ветки считаем "1"
        return dict

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

# строка для кодирования
s = "beep boop beer!"

my_list = list(s)
my_list = [(el, my_list.count(el)) for el in set(my_list)]
my_list = sorted(my_list, key=lambda item: item[1], reverse=True)
print('Список, отсоортированный по частоте вхождения символов в строку:\n',my_list)
tree = Tree(0)
for el, value in my_list:
    tree.insert(el, value)      # Заполним дерево
tree.del_empty_branch(tree)     # Уберем пустую ветку (оптимизируем), если есть
print('Полученное дерево:')
tree.display()
code_dict = tree.fill_code_dict(tree)   # заполним словарь кодирования
print('Словарь кодирования:\n', code_dict)
print('Закодированная строка:')
for el in s:
    print(code_dict[el], end=' ')

str_b =''.join([code_dict[el] for el in s])
res = ''.join(format(ord(i), 'b') for i in s)
print(f'\nThe string before conversion : {s},\n(размер {len(s)*8} бит)')
print(f'The string after binary conversion : {str(res)}')
print(f'The string after Hoffman conversion: {str_b}\n(размер {len(str_b)} бит)')
print()

# while len(str_b) > 0:
#     str_b, sub_str = str_b[8:], str_b[:8].rjust(8,'0')
#
#     print(sub_str)