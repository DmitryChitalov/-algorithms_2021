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


def tree_build(string_obj):
    el_count = Counter(string_obj)
    sorted_counts = deque(sorted(el_count.items(), key=lambda i: i[1]))
    if len(sorted_counts) != 1:
        while len(sorted_counts) > 1:
            weight = sorted_counts[0][1] + sorted_counts[1][1]
            combine = {0: sorted_counts.popleft()[0],
                       1: sorted_counts.popleft()[0]}
            for i, cnt in enumerate(sorted_counts):
                if weight > cnt[1]:
                    continue
                else:
                    sorted_counts.insert(i, (combine, weight))
                    break
            else:
                sorted_counts.append((combine, weight))
    else:
        weight = sorted_counts[0][1]
        combine = {0: sorted_counts.popleft()[0], 1: None}
        sorted_counts.append((combine, weight))
    return sorted_counts[0][0]


table = dict()


def tree_code(tree, path=''):
    if not isinstance(tree, dict):
        table[tree] = path
    else:
        tree_code(tree[0], path=f'{path}0')
        tree_code(tree[1], path=f'{path}1')


string = 'beep boop beer!'
tree_code(tree_build(string))


for i in string:
  print(table[i], end=' ')


