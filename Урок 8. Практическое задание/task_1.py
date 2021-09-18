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


def haffman_tree(s):

    counter = Counter(s)
    sorted_elements = deque(sorted(counter.items(), key=lambda x: x[1]))
    if len(sorted_elements) != 1:
        while len(sorted_elements) > 1:
            new_weight = sorted_elements[0][1] + sorted_elements[1][1]
            comb = {0: sorted_elements.popleft()[0],
                    1: sorted_elements.popleft()[0]}
            for i, j in enumerate(sorted_elements):
                if new_weight > j[1]:
                    continue
                else:
                    sorted_elements.insert(i, (comb, new_weight))
                    break
            else:
                sorted_elements.append((comb, new_weight))

    else:

        weight = sorted_elements[0][1]
        comb = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((comb, weight))

    return sorted_elements[0][0]


code_table = dict()


def haffman_code(tree, path=''):

    if not isinstance(tree, dict):
        code_table[tree] = path

    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


# строка для кодирования
s = "hello!"

haffman_code(haffman_tree(s))

for i in s:
    print(code_table[i], end=' ')
print()
#это ваш код, в котором я разобралась и слегка подредактировала