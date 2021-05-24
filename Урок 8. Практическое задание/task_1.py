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

from collections import Counter


class BTree:
    def __init__(self, node_name, node_weight, lc, rc):
        if node_name != '':             # Если передали лист
            self.name = node_name       # название листа
            self.id_parent = 0          # пока родительский узел равен 0
            self.lc = 0                 # пока правый потомок равен 0
            self.rc = 0                 # пока левый потомок равен 0
            self.weight = node_weight   # вес листа
        else:                           # Если передали потомков
            self.name = ''              # наименование узла пустое
            self.id_parent = 0          # пока родительский узел равен 0
            self.lc = lc                # объект - левый потомок
            self.rc = rc                # объект - правый потомок
            lc.id_parent = self         # теперь для левого потомка записываем родителя
            rc.id_parent = self         # теперь для правого потомка записываем родителя
            self.weight = lc.weight + rc.weight     # вес узла


def make_btree(s):
    # преобразуем строку в отсортированный список
    lst = sorted(dict(Counter(s)).items(), key=lambda x: x[1])

    # преобразуем каждый символ в объект класса BTree
    lst_node = []
    for el in lst:
        new_node = BTree(el[0], el[1], 0, 0)
        lst_node.append((new_node, new_node.weight))

    # Строим дерево
    while len(lst_node) > 1:
        l_node = lst_node.pop(0)
        r_node = lst_node.pop(0)
        new_node = BTree('', 0, l_node[0], r_node[0])
        lst_node.append((new_node, new_node.weight))
        lst_node.sort(key=lambda x: (x[1]))

    # Возвращаем объект - дерево
    return lst_node[0][0]


def get_s_dict(s_dict, obj_tree, encode):

    if obj_tree.lc == 0 and obj_tree.rc == 0:
        # Если спустились по дереву до уровня листа, записываем кодированную строку
        s_dict[obj_tree.name] = encode
    else:
        # Если на уровне узла/корня, рекурсивно проходим до листьев
        if obj_tree.lc:
            get_s_dict(s_dict, obj_tree.lc, ''.join([encode, '0']))

        if obj_tree.rc:
            get_s_dict(s_dict, obj_tree.rc, ''.join([encode, '1']))

    return


def encode_haffman(s):
    # Строим бинарное дерево
    s_btree = make_btree(s)

    # Получаем словарь на основе бинарного дерева
    s_dct = {}
    get_s_dict(s_dct, s_btree, '')
    print('Словарь: ', s_dct)

    # Формируем закодированную строку
    res = ''
    for el in s:
        res += s_dct.get(el)

    return res


print('Закодированная строка: ', encode_haffman('abrakadabra'))

# Словарь:  {'a': '0', 'k': '100', 'd': '101', 'b': '110', 'r': '111'}
# Закодированная строка:  01101110100010101101110
