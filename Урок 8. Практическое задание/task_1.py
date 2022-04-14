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

lst = 'beep boop beer!'
new_lst = deque(sorted(Counter(lst).items(), key=lambda x: x[1]))


def tree(vol):
    if len(vol) > 1:
        w = vol[0][1] + vol[1][1]
        new = {0: vol.popleft()[0], 1: vol.popleft()[0]}
        for i, j in enumerate(vol):
            if w > j[1]:
                continue
            else:
                vol.insert(i, (new, w))
                break
        else:
            vol.append((new, w))
        tree(vol)
    return vol[0][0]


# print(tree(new_lst))
code_table = {}


def code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        code(tree[0], path=f'{path}0')
        code(tree[1], path=f'{path}1')


def call_code(some_str):
    if len(some_str) <= 1:
        print('0')
    else:
        code(tree(some_str))
        print(*[code_table[i] for i in lst])


call_code(new_lst)
