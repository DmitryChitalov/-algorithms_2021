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


def double_tree(str_in):
    count_el = Counter(str_in)
    deque_elem = deque(sorted(count_el.items(), key=lambda item: item[1]))
    while len(deque_elem) > 1:
        weight_el = deque_elem[0][1] + deque_elem[1][1]
        tree = {0: deque_elem.popleft()[0], 1: deque_elem.popleft()[0]}
        for i, count_el in enumerate(deque_elem):
            if weight_el > count_el[1]:
                continue
            else:
                deque_elem.insert(i, (tree, weight_el))
                break
        else:
            deque_elem.append((tree, weight_el))
    return deque_elem[0][0]


encoding_table = dict()


def encoding(tree, branch=''):
    if not isinstance(tree, dict):
        encoding_table[tree] = branch
    else:
        encoding(tree[0], branch=f'{branch}0')
        encoding(tree[1], branch=f'{branch}1')


in_str = str(input('Введите строку для кодирования: '))
print(f'Исходная строка: {in_str}')

print(f'Итоговое дерево: {double_tree(in_str)}')
encoding(encoding(double_tree(in_str)))
print(f'Таблица кодировок: {encoding_table}')
print('Строка в кодированном виде:')
for value in encoding_table.values():
    print(value, end=' ')
