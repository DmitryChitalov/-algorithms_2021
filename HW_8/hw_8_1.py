
from collections import Counter, deque


def binary_tree(s):
    count = Counter(s)
    sort_elem = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(sort_elem) != 1:

        while len(sort_elem) > 1:
            weight = sort_elem[0][1] + sort_elem[1][1]
            comb = {0: sort_elem.popleft()[0],
                    1: sort_elem.popleft()[0]}
            for i, _count in enumerate(sort_elem):
                if weight > _count[1]:
                    continue
                else:
                    sort_elem.insert(i, (comb, weight))
                    break
            else:
                sort_elem.append((comb, weight))
    else:
        weight = sort_elem[0][1]
        comb = {0: sort_elem.popleft()[0], 1: None}
        sort_elem.append((comb, weight))
    return sort_elem[0][0]


code_table = dict()


def encoding(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        encoding(tree[0], path=f'{path}0')
        encoding(tree[1], path=f'{path}1')

s = input('Введите строку для кодирования:\n')

encoding(binary_tree(s))
for i in s:
    print(code_table[i], end=' ')

#тема для меня достаточно сложная, по большому счету только переименовала переменные
#но я лучше разобралась в теме 