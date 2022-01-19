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
from operator import itemgetter

hafm_table = {}


def form_haffman_tree(string):
    count = Counter(string)
    # получится отсортированный список deque, где элементы - кортежи(буква, кол-во)
    sorted_lst = deque(sorted(count.items(), key=itemgetter(1)))
    # print(sorted_lst)
    if len(sorted_lst) != 1:
        while len(sorted_lst) > 1:  # строим дерево
            w = sorted_lst[0][1] + sorted_lst[1][1]  # объединенный вес
            noda = {0: sorted_lst.popleft()[0],  # создаем элемент, вырезая из списка первые элементы в наш словарь
                    1: sorted_lst.popleft()[0]}
            # Ищем место для вставки объединенного элемента в тот же список
            for i, c in enumerate(sorted_lst):
                if w > c[1]:
                    continue
                else:
                    # Вставляем объединенный элемент
                    sorted_lst.insert(i, (noda, w))
                    break
            else:
                # если наш новый элемент весит больше всех, то добавляем его в хвост
                sorted_lst.append((noda, w))
    else:
        # приравниваем значение 0 к одному повторяющемуся символу
        w = sorted_lst[0][1]
        noda = {0: sorted_lst.popleft()[0], 1: None}
        sorted_lst.append((noda, w))

    return sorted_lst


def create_hafm_table(tree_dict, path=''):
    if not isinstance(tree_dict, dict):  # получили лист бинарного дерева
        hafm_table[tree_dict] = path
    else:
        create_hafm_table(tree_dict[0], path=f'{path}0')
        create_hafm_table(tree_dict[1], path=f'{path}1')


# строка для кодирования
s = "We race as one"

create_hafm_table(form_haffman_tree(s)[0][0])
# for key, val in hafm_table.items():
#     print(f'{key}: {val}')

for i in s:
    print(hafm_table[i], end='')
