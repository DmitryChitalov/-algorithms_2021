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


def haffman_tree(new_str):
    count = Counter(new_str)
    sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(sorted_elements) != 1:
        while len(sorted_elements) > 1:
            weight = sorted_elements[0][1] + sorted_elements[1][1]

            collect = {0: sorted_elements.popleft()[0],
                       1: sorted_elements.popleft()[0]}

            for elems, _count in enumerate(sorted_elements):
                if weight > _count[1]:
                    continue
                else:
                    sorted_elements.insert(elems, (collect, weight))
                    break
            else:
                sorted_elements.append((collect, weight))

    else:
        weight = sorted_elements[0][1]
        collect = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((collect, weight))
    return sorted_elements[0][0]


code_table = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


string = "close window!"
haffman_code(haffman_tree(string))
for i in string:
    print(code_table[i], end=' ')
print()

"""
Я заново сделал код, но не вижу как можно его улучшить
"""