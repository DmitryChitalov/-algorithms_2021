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

#Немного оптимизации в конце + rename для переменных
from collections import Counter, deque

def haffman_tree(user_answer):
    count = Counter(user_answer)
    srt_elems = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(srt_elems) != 1:
        while len(srt_elems) > 1:
            weight = srt_elems[0][1] + srt_elems[1][1]
            comb = {0: srt_elems.popleft()[0],
                    1: srt_elems.popleft()[0]}
            for i, el in enumerate(srt_elems):
                if weight > el[1]:
                    continue
                else:
                    srt_elems.insert(i, (comb, weight))
                    break
            else:
                srt_elems.append((comb, weight))
    else:
        weight = srt_elems[0][1]
        comb = {0: srt_elems.popleft()[0], 1: None}
        srt_elems.append((comb, weight))
    return srt_elems[0][0]

def printing_code(user_answer):
    return [dict_withelems[i] for i in user_answer]

dict_withelems = dict()

def haffman_code(tree, path=''):
    if not isinstance(tree, dict):
        dict_withelems[tree] = path
    else:
        haffman_code(tree[0], path=f'{path}0')
        haffman_code(tree[1], path=f'{path}1')

user_answer = "like vodka, like gin, like coctail" #input("Введите предложение для кодировки по Хаффману: ")
haffman_code(haffman_tree(user_answer))
print(" ".join(printing_code(user_answer)))


#Реализация через ООП
class Hauffman_tree:
    def __init__(self, value):
        self.value = value
        self.bin_dict = dict()
        self.code_maker(self.tree_maker)

    @property
    def tree_maker(self):
        valum = self.values_sorting.copy()
        if len(valum) != 1:
            while len(valum) > 1:
                elem = valum[0][1] + valum[1][1]
                el_join = {0: valum.popleft()[0],
                           1: valum.popleft()[0]}
                for i, k in enumerate(valum):
                    if elem > k[1]:
                        continue
                    else:
                        valum.insert(i, (el_join, elem))
                        break
                else:
                    valum.append((el_join, elem))
        else:
            elem = valum[0][1]
            el_join = {0: valum.popleft()[0], 1: None}
            valum.append((el_join, elem))
        return valum[0][0]

    def code_maker(self, tree, path=""):
        if not isinstance(tree, dict):
            self.bin_dict[tree] = path
        else:
            self.code_maker(tree[0], path=f'{path}0')
            self.code_maker(tree[1], path=f'{path}1')

    @property
    def user_str(self):
        bin_str = ''
        for i in self.value:
            bin_str += self.bin_dict[i] + " "
        return bin_str

    @property
    def system_counter(self):
        return Counter(self.value)

    @property
    def values_sorting(self):
        return deque(sorted(self.system_counter.items(), key=lambda x: x[1]))

if __name__ == '__main__':
    string_test = "like vodka, like gin, like coctail"
    tree_haff = Hauffman_tree(string_test)
    print(f"\nРеализация через ООП.\nДеревце: {tree_haff.tree_maker}\n")
    print(f'Словарь "бинарников":\n{tree_haff.bin_dict}\n')
    print(f'Строка "бинарников":\n{tree_haff.user_str}\n')