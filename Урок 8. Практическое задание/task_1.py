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

from collections import defaultdict

code_table = dict()
s = "beep boop beer!"

def count_letters(s):
    letters = defaultdict(int)
    for i in s:
        letters[i] += 1
    sorted_letters = list(sorted(letters.items(), key=lambda i: i[1]))
    return sorted_letters


def haffman_tree(s_letter):
    if len(s_letter) > 1:
        while len(s_letter) > 2:
            weight = s_letter[0][1] + s_letter[1][1]
            union = {0: s_letter.pop(0)[0], 1: s_letter.pop(0)[0]}
            for i in range(len(s_letter)):
                if weight <= s_letter[i][1]:
                    s_letter.insert(i, (union, weight))
                    break
            else:
                s_letter.append((union, weight))
        else:
            s_letter = {0: s_letter[0][0], 1: s_letter[1][0]}
    else:
        s_letter = {0: s_letter[0][0]}
    return s_letter


def code_letter(tree, code = ''):
    if not isinstance(tree, dict):
        code_table[tree] = code
    else:
        code_letter(tree[0], code=f'{code}0')
        code_letter(tree[1], code=f'{code}1')


s = "beep boop beer!"

sorted = count_letters(s)
tree = haffman_tree(sorted)
code_letter(tree)
for i in s:
    print(code_table[i], end=' ')


