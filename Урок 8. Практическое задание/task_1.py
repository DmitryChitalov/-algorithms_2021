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
"""Хаффман через коллекции"""

from collections import Counter, deque


def tree_to_haffman(user_val):
    count_uniq_symb = Counter(user_val)
    sort_elem = deque(sorted(count_uniq_symb.items(), key=lambda x: x[1]))
    if len(sort_elem) != 1:
        while len(sort_elem) > 1:
            weight = sort_elem[0][1] + sort_elem[1][1]
            union = {0: sort_elem.popleft()[0],
                     1: sort_elem.popleft()[0]}
            for i, cnt in enumerate(sort_elem):
                if weight > cnt[1]:
                    continue
                else:
                    sort_elem.insert(i, (union, weight))
                    break
            else:
                sort_elem.append((union, weight))
    else:
        weight = sort_elem[0][1]
        union = {0: sort_elem.popleft()[0], 1: None}
        sort_elem.append((union, weight))
    return sort_elem[0][0]


code_tbl = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_tbl[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


_str = "beep boop beer!"

haffman_code(tree_to_haffman(_str))

for i in _str:
    print(code_tbl[i], end=' ')
print()

"""
Переписал код вручную. Разобрал. До определенного момента все четко понятно, потом тманнее.
Буду еще разбирать.
"""