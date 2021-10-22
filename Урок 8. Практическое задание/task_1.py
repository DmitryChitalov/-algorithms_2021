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
from collections import Counter


def a(li):
    my_dict = {}
    if li[-1][-1] < li[-2][-1]:
        my_dict[0] = li.pop()[0]
        my_dict[1] = li.pop()[0]
    else:
        my_dict[1] = li.pop()[0]
        my_dict[0] = li.pop()[0]
    return my_dict


def haffman_coder(li, dict_coder):
    if len(li) > 1 and len(dict_coder) != 2:
        dict_coder[0] = a(li)
        dict_coder[1] = a(li)
        return haffman_coder(li, dict_coder)
    elif len(li) > 1 and len(dict_coder) == 2:
        dict_coder[0] = dict_coder.copy()
        dict_coder[1] = a(li)
        return haffman_coder(li, dict_coder)
    else:
        copy_dict = dict_coder.copy()
        dict_coder[0] = copy_dict
        dict_coder[1] = li.pop()[0]
        return dict_coder


def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


hash_dict = {}
you = "beep boop beer!"
you_sort = sorted(Counter(you).items(), key=lambda x: x[1], reverse=True)
dict_hash = haffman_coder(you_sort, hash_dict)
code_table = dict()
haffman_code(dict_hash)
print(code_table)

for i in you:
    print(code_table[i], end=' ')
"""
{'r': '0000', '!': '0001', ' ': '0010', 'o': '0011', 'p': '010', 'b': '011', 'e': '1'}
011 1 1 010 0010 011 0011 0011 010 0010 011 1 1 0000 0001 
"""
