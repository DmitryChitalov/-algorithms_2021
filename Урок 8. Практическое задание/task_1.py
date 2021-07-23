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


def haffman_treefy(string: str):
    count = Counter(string)
    symb_freq = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(symb_freq) != 1:
        while len(symb_freq) > 1:
            weight = symb_freq[0][1] + symb_freq[1][1]
            node = {0: symb_freq.popleft()[0],
                    1: symb_freq.popleft()[0]}
            for i, _count in enumerate(symb_freq):
                if weight > _count[1]:
                    continue
                else:
                    symb_freq.insert(i, (node, weight))
                    break
            else:
                symb_freq.append((node, weight))
    else:
        weight = symb_freq[0][1]
        node = {0: symb_freq.popleft()[0], 1: None}
        symb_freq.append((node, weight))
    return symb_freq[0][0]


def haffman_encode(tree, symbol_tbl, path=''):
    if not isinstance(tree, dict):
        symbol_tbl[tree] = path
    else:
        haffman_encode(tree[0], symbol_tbl, path=f'{path}0')
        haffman_encode(tree[1], symbol_tbl, path=f'{path}1')


def haffman(string: str):
    symbol_tbl = dict()
    haffman_encode(haffman_treefy(string), symbol_tbl)
    print('Symbol table:', symbol_tbl)
    for i in string:
        print(symbol_tbl[i], end=' ')
    print()



haffman('beep boop beer!')
haffman(
    'Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
    'incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud '
    'exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure '
    'dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. '
    'Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum. '
)
