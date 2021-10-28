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
from operator import itemgetter


class Offspring:

    def __init__(self, left_ch=None, right_ch=None):
        self.left_ch = left_ch
        self.right_ch = right_ch

    def child(self):
        return self.left_ch, self.right_ch


def create_tree(root, cypher=str()):
    if type(root) is str:
        return {
            root: cypher
        }
    l, r = root.child()
    result = {}
    result.update(create_tree(l, cypher + "0"))
    result.update(create_tree(r, cypher + "1"))
    return result


# Подсчет букв
def count_rep_lett(data):
    dct_quantity = Counter(data)
    srt_dct = sorted(dct_quantity.items(), key=itemgetter(1))
    while len(srt_dct) > 1:
        srt_dct = sorted(srt_dct, key=itemgetter(1))
        counter = 0
        lett_1, cnt_1 = srt_dct[0]
        lett_2, cnt_2 = srt_dct[1]
        srt_dct = srt_dct[2:]
        counter += cnt_1 + cnt_2
        srt_dct.append(
            (Offspring(lett_1, lett_2), counter))
    return srt_dct


data = "beep boop beer!"
srt_dct = count_rep_lett(data)
# print(srt_dct)

code_letters = create_tree(srt_dct[0][0])
# print(code_letters)

# Закодированная строка
for el in code_letters.values():
    print(el, end=' ')


