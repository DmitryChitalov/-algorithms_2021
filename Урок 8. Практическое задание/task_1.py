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

str_user = "beep boop beer!"
code_table = dict()


def haffman_tree(str_u):
    haffman_elem = deque(sorted(Counter(str_u).items(), key=lambda el: el[1]))
    if len(haffman_elem) != 1:
        while len(haffman_elem) > 1:
            part = haffman_elem[0][1] + haffman_elem[1][1]
            united = {0: haffman_elem.popleft()[0], 1: haffman_elem.popleft()[0]}
            for index_elem, elem in enumerate(haffman_elem):
                if part > elem[1]:
                    continue
                else:
                    haffman_elem.insert(index_elem, (united, part))
                    break
            else:
                haffman_elem.append((united, part))
    return haffman_elem[0][0]


def haffman_code(binary_tree, path=''):
    if not isinstance(binary_tree, dict):
        code_table[binary_tree] = path
    else:
        haffman_code(binary_tree[0], path + '0')
        haffman_code(binary_tree[1], path + '1')


haffman_code(haffman_tree(str_user[:]))

print(*(code_table[i] for i in str_user))


"""по сути чуть переделанный код с урока"""
