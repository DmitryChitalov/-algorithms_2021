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
    temp_dict = Counter(s)
    s_elems = deque(sorted(temp_dict.items(), key=lambda item: item[1]))
    if len(s_elems) != 1:
        while len(s_elems) > 1:
            weight = s_elems[0][1] + s_elems[1][1]
            comb = {0: s_elems.popleft()[0],
                    1: s_elems.popleft()[0]}
            for i, _count in enumerate(s_elems):
                if weight > _count[1]:
                    continue
                else:
                    s_elems.insert(i, (comb, weight))
                    break
            else:
                s_elems.append((comb, weight))
    else:
        weight = s_elems[0][1]
        comb = {0: s_elems.popleft()[0], 1: None}
        s_elems.append((comb, weight))
    return s_elems[0][0]


code_table = dict()


def haf_encode(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haf_encode(tree[0], path=f'{path}0')
        haf_encode(tree[1], path=f'{path}1')


s = "happy new year!"

haf_encode(haffman_tree(s))


for i in s:
    print(code_table[i], end=' ')
print()