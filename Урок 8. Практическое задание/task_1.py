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
from collections import deque, Counter


def get_freq(string):
    tuples = []
    for j in Counter(string).keys():
        tuples.append((Counter(string)[j], j))
    return deque(sorted(Counter(string).items(), key=lambda item: item[1]))


def get_tree(sorted_deque):
    if len(sorted_deque) != 1:
        while len(sorted_deque) > 1:
            weight = sorted_deque[0][1] + sorted_deque[1][1]
            comb = {0: sorted_deque.popleft()[0], 1: sorted_deque.popleft()[0]}
            for i, _count in enumerate(sorted_deque):
                if weight > _count[1]:
                    continue
                else:
                    sorted_deque.insert(i, (comb, weight))
                    break
            else:
                sorted_deque.append((comb, weight))
        else:
            weight = sorted_deque[0][1]
            comb = {0: sorted_deque.popleft()[0]}
            sorted_deque.append((comb, weight))
        return sorted_deque[0][0][0]


code_table = dict()


def get_haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        get_haffman_code(tree[0], path=f'{path}0')
        get_haffman_code(tree[1], path=f'{path}1')


def get_code(string):
    get_haffman_code(get_tree(get_freq(string)))
    for i in string:
        print(code_table[i], end="")
    print()


get_code("beep boop beer!")
