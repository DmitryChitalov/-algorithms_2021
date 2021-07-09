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

from collections import deque

def my_tree(text):
    my_dict = dict()
    # {'b': 3, 'e': 4, 'p': 2, ' ': 2, 'o': 2, 'r': 1, '!': 1}

    for i in text:
        my_dict[i] = text.count(i)

    # {'r': 1, '!': 1, 'p': 2, ' ': 2, 'o': 2, 'b': 3, 'e': 4}
    my_sorted_dict = deque(sorted(my_dict.items(), key=lambda item: item[1]))
    del my_dict

    if len(my_sorted_dict) != 1:
        while len(my_sorted_dict) > 1:
            num = my_sorted_dict[0][1] + my_sorted_dict[1][1]
            new_branch = {0: my_sorted_dict.popleft()[0], 1: my_sorted_dict.popleft()[0]}

            for i, val in enumerate(my_sorted_dict):
                if num > val[1]:
                    continue
                else:
                    my_sorted_dict.insert(i, (new_branch, num))
                    break
            else:
                my_sorted_dict.append((new_branch, num))
    else:
        num = my_sorted_dict[0][1]
        new_branch = {0: my_sorted_dict.popleft()[0]}
        my_sorted_dict.append((new_branch, num))
    return my_sorted_dict[0][0]


def hoffman_code(tree, path=''):
    if not isinstance(tree, dict):
        my_dict[tree] = path
    else:
        hoffman_code(tree[0], path=f'{path}0')
        hoffman_code(tree[1], path=f'{path}1')


my_text = "beep boop beer!"
my_dict = dict()
hoffman_code(my_tree(my_text))
result = ''
for i in my_text:
    result += my_dict[i] + ' '
print(f"Исходный текст: '{my_text}'\nresult: '{result}'")
