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


class Haffman:
    def __init__(self, obj):
        self.obj = obj
        self.bin_tab = {}

    def __str__(self):
        self.haffman_bin(self.haffman_structure())
        code = ''
        for i in self.obj:
            code += f'{self.bin_tab[i]} '
        return code

    def haffman_bin(self, dct, bin=''):
        if isinstance(dct, dict):
            self.haffman_bin(dct[0], bin=f'{bin}0')
            self.haffman_bin(dct[1], bin=f'{bin}1')
        else:
            self.bin_tab[dct] = bin

    def my_sort(self, dct):
        sort_i_cnt = {}
        for i in sorted(dct, key=dct.get, reverse=True):
            sort_i_cnt[i] = dct[i]
        return sort_i_cnt

    def haffman_structure(self):
        cnt = {}
        for i in set(self.obj):
            cnt[i] = 0
            for j in self.obj:
                if i == j:
                    cnt[i] += 1
        sort_i_cnt = self.my_sort(cnt)

        if len(sort_i_cnt) == 1:
            double = {0: sort_i_cnt.popitem()[0], 1: None}
            return double
        else:
            while len(sort_i_cnt) > 1:
                double_cnt = []
                sum_double_cnt = 0
                for i in range(2):
                    double_cnt.append(sort_i_cnt.popitem())
                    sum_double_cnt += double_cnt[-1][1]
                double = {0: double_cnt[0][0],
                          1: double_cnt[1][0]}
                sort_i_cnt[str(double)] = sum_double_cnt
                sort_i_cnt = self.my_sort(sort_i_cnt)
            str_tree = list(sort_i_cnt)[0].replace("'", '')
            for i in str_tree:
                if i in self.obj and i != '' and i != ' ':
                    str_tree = str_tree.replace('\\', '').replace('"', '').replace(i, f"'{i}'").replace(':  ', ": ' '")
            tree = eval(str_tree)
        return tree


s = "extremes meet too"

haf_obj = Haffman(s)

print(haf_obj)
print(haf_obj.obj)
print(haf_obj.bin_tab)
print(haf_obj.haffman_structure())

# 11 1010 00 10111 11 011 11 10110 100 011 11 11 00 100 00 010 010
# extremes meet too
# {'t': '00', 'o': '010', 'm': '011', ' ': '100', 'x': '1010', 's': '10110', 'r': '10111', 'e': '11'}
# {0: {0: 't', 1: {0: 'o', 1: 'm'}}, 1: {0: {0: ' ', 1: {0: 'x', 1: {0: 's', 1: 'r'}}}, 1: 'e'}}
