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
# Код идентичен материалу с урока, в доработке не нуждается на мой взгляд. Решение красивое и эффективное.
# Также вы на уроке разрешили не менять решение, если сложно придумать что-либо свое. В теме разобрался-это главное.

from collections import Counter, deque


def huffman_tree(str_obj):
    count = Counter(str_obj)
    sorted_elements = deque(sorted(count.items(), key=lambda symbol: symbol[1]))

    if len(sorted_elements) != 1:
        while len(sorted_elements) > 1:
            weight = sorted_elements[0][1] + sorted_elements[1][1]

            comb = {0: sorted_elements.popleft()[0], 1: sorted_elements.popleft()[0]}

            for index, _count in enumerate(sorted_elements):
                if weight > _count[1]:
                    continue
                else:
                    sorted_elements.insert(index, (comb, weight))
                    break
            else:
                sorted_elements.append((comb, weight))
    else:
        weight = sorted_elements[0][1]
        comb = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((comb, weight))

    return sorted_elements[0][0]


code_table = dict()


def huffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        huffman_code(tree[0], path=f'{path}0')
        huffman_code(tree[1], path=f'{path}1')


s = "huffman code"

huffman_code(huffman_tree(s))

for i in s:
    print(code_table[i], end=' ')
print()
