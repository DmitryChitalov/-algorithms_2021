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
import random


def double_tree(str_):
    count_el = Counter(str_)
    deque_elem = deque(sorted(count_el.items(), key=lambda item: item[1]))
    while len(deque_elem) > 1:
        weight_el = deque_elem[0][1] + deque_elem[1][1]
        tree = {0: deque_elem.popleft()[0], 1: deque_elem.popleft()[0]}
        for i, count_ in enumerate(deque_elem):
            if weight_el > count_[1]:
                continue
            else:
                deque_elem.insert(i, (tree, weight_el))
                break
        else:
            deque_elem.append((tree, weight_el))
    # else:
    #     weight_el = deque_elem[0][1]
    #     tree = {0: deque_elem.popleft()[0], 1: None}
    #     deque_elem.append((deque_elem, weight_el))
    return deque_elem[0][0]


encoding_table = dict()


def encoding(tree, branch=''):
    if not isinstance(tree, dict):
        encoding_table[tree] = branch
    else:
        encoding(tree[0], branch=f'{branch}0')
        encoding(tree[1], branch=f'{branch}1')


all_elements = 'qwertyuiopasdfghjklzxcvbnmйцукенгшщзхъфывапролджэячсмитьбю1234567890 '
rand_list = []
for el in range(10):
    rand_list.append(all_elements[random.randrange(0, len(all_elements))])
rand_string = ''.join(rand_list)
print(rand_string)

print(double_tree(rand_string))
encoding(encoding(double_tree(rand_string)))
print(encoding_table)
for value in encoding_table.values():
    print(value, end=' ')
