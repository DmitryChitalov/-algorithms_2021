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

my_str = 'Мой дядя самых честных правил'


def my_tree(any_str):
    elemcount = Counter(any_str)
    my_deque = deque(sorted(elemcount.items(), key=lambda item: item[1]))
    while len(my_deque) > 1:
        elemweight = my_deque[0][1] + my_deque[1][1]
        tree = {0: my_deque.popleft()[0], 1: my_deque.popleft()[0]}
        for i, num in enumerate(my_deque):
            if elemweight > num[1]:
                continue
            else:
                my_deque.insert(i, (tree, elemweight))
                break
        else:
            my_deque.append((tree, elemweight))

    return my_deque[0][0]


encoding_table = dict()


def recur_encode(tree, branch=''):
    if not isinstance(tree, dict):
        encoding_table[tree] = branch
    else:
        recur_encode(tree[0], branch=f'{branch}0')
        recur_encode(tree[1], branch=f'{branch}1')


print(my_tree(my_str))
recur_encode(my_tree(my_str))
print(encoding_table)
for value in encoding_table.values():
    print(value, end=' ')
