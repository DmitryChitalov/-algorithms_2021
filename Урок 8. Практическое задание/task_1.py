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
import collections

def haffman_tree(s):
    d = collections.Counter(s)
    sorted_d = collections.deque(sorted(d.items(), key=lambda item: item[1]))
    if len(sorted_d) != 1:
        while len(sorted_d) > 1:
            weight = sorted_d[0][1] + sorted_d[1][1]
            comb = {0: sorted_d.popleft()[0],
                    1: sorted_d.popleft()[0]}

            for i, _count in enumerate(sorted_d):
                if weight > _count[1]:
                    continue
                else:
                    sorted_d.insert(i, (comb, weight))
                    break
            else:
                sorted_d.append((comb, weight))

    else:
        weight = sorted_d[0][1]
        comb = {0: sorted_d.popleft()[0], 1: None}
        sorted_d.append((comb, weight))
    return sorted_d[0][0]

code_table = dict()

def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


s = "beep boop"

haffman_code(haffman_tree(s))

for i in s:
    print(code_table[i], end=' ')
print()
