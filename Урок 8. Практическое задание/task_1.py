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


# 1)
def haffman_tree(s):
    count_string = Counter(s)
    sorted_string = deque(sorted(count_string.items(), key=lambda item: item[1]))
    if len(sorted_string) != 1:
        while len(sorted_string) > 1:
            duplication = sorted_string[0][1] + sorted_string[1][1]
            merger = {0: sorted_string.popleft()[0],
                      1: sorted_string.popleft()[0]}

            for i, _count in enumerate(sorted_string):
                if duplication > _count[1]:
                    continue
                else:
                    sorted_string.insert(i, (merger, duplication))
                    break
            else:
                sorted_string.append((merger, duplication))
    else:
        duplication = sorted_string[0][1]
        merger = {0: sorted_string.popleft()[0], 1: None}
        sorted_string.append((merger, duplication))

    return sorted_string[0][0]


code_table = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


s = "мама мыла раму!"

haffman_code(haffman_tree(s))

for _ in s:
    print(code_table[_], end=' ')
