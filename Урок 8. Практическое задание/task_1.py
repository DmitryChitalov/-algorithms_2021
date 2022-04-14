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

from collections import Counter, deque


def construct_tree(string):
    storage_elems = Counter(string)
    storage_elems_sort = deque(
        sorted(storage_elems.items(), key=lambda item: item[1]))
    if len(storage_elems_sort) != 1:
        while len(storage_elems_sort) > 1:
            mass = storage_elems_sort[0][1] + storage_elems_sort[1][1]
            unite = {0: storage_elems_sort.popleft()[0],
                     1: storage_elems_sort.popleft()[0]}
            for i, _periodicity in enumerate(storage_elems_sort):
                if mass > _periodicity[1]:
                    continue
                else:
                    storage_elems_sort.insert(i, (unite, mass))
                    break
            else:
                storage_elems_sort.append((unite, mass))
    else:
        mass = storage_elems_sort[0][1]
        unite = {0: storage_elems_sort.popleft()[0], 1: None}
        storage_elems_sort.append((unite, mass))
    return storage_elems_sort[0][0]


code_table = dict()


def decryption_tree(tree, code=''):
    if not isinstance(tree, dict):
        code_table[tree] = code
    else:
        decryption_tree(tree[0], code=f'{code}0')
        decryption_tree(tree[1], code=f'{code}1')


string_code = "beep boop beer!"
a = construct_tree(string_code)
print(a)
decryption_tree(construct_tree(string_code))

for i in string_code:
    print(code_table[i], end=' ')
print()
