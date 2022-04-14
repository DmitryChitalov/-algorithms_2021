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
import ast


def create_branch(future_branch):
    tree_dict = {}
    weight = 0
    while len(tree_dict) != 2:
        tmp = future_branch.most_common()[-1]
        weight += tmp[1]
        if len(tree_dict) == 0:
            tree_dict[0] = tmp[0]
        else:
            tree_dict[1] = tmp[0]
        del future_branch[tmp[0]]
    future_branch[f"{tree_dict}"] = weight


def fun(future_tree):
    while len(future_tree) != 1:
        create_branch(future_tree)


s = 'beep boop beer!'
# s = '''Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex.'''
new_tree = Counter(s).copy()
fun(new_tree)
res_json = str(new_tree.keys()).replace('\'', '"').replace('\\', '').replace('\'', '')
res_json = res_json.replace('}"', '}').replace('"{', '{')[11:-2]
# превращаем строку в словарь
res_json = ast.literal_eval(res_json)


# res_json - {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')


code_table = dict()
haffman_code(res_json)
print(code_table)

for _ in s:
    print(code_table[_], sep='', end=' ')
