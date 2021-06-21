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


def haffman_tree(text):
    count = Counter(text)
    deque_elem = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(deque_elem) != 1:
        while len(deque_elem) > 1:
            weight = deque_elem[0][1] + deque_elem[1][1]
            comb = {0: deque_elem.popleft()[0],
                    1: deque_elem.popleft()[0]}

            for i, _count in enumerate(deque_elem):
                if weight > _count[1]:
                    continue
                else:
                    deque_elem.insert(i, (comb, weight))
                    break
            else:
                deque_elem.append((comb, weight))
    else:
        weight = deque_elem[0][1]
        comb = {0: deque_elem.popleft()[0], 1: None}
        deque_elem.append((comb, weight))
    return deque_elem[0][0]


result_code = dict()


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        result_code[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


text = input("Введите фразу для кодирования методом Хаффмана: ")
haffman_code(haffman_tree(text))

for i in text:
    print(result_code[i], end=' ')
print()
