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


class HaffMan:

    def __init__(self, origin):
        self.origin = origin
        self.__code_table = dict()

    def __make_tree(self):
        string_deque = deque(sorted(Counter(self.origin).items(), key=lambda item: item[1]))

        if len(string_deque) != 1:

            while len(string_deque) > 1:
                weight = string_deque[0][1] + string_deque[1][1]
                comb = {0: string_deque.popleft()[0],
                        1: string_deque.popleft()[0]}

                for ind, count in enumerate(string_deque):
                    if weight > count[1]:
                        continue
                    else:
                        string_deque.insert(ind, (comb, weight))
                        break
                else:
                    string_deque.append((comb, weight))

        else:
            weight = string_deque[0][1]
            comb = {0: string_deque.popleft()[0], 1: None}
            string_deque.append((comb, weight))
        return string_deque[0][0]

    def __haffman_code(self, tree, path=''):
        if not isinstance(tree, dict):
            self.__code_table[tree] = path
        else:
            self.__haffman_code(tree[0], path=f'{path}0')
            self.__haffman_code(tree[1], path=f'{path}1')

    def __str__(self):
        self.__haffman_code(self.__make_tree())
        result = ''
        for i in self.origin:
            result += f'{self.__code_table[i]} '
        return result


obj = HaffMan('beep boop beer!')
print(obj.origin)
print(obj)

'''
По итогу, сильных изменений в самом коде я не произвел, а лишь адаптировал под ООП
(хотя все, что можно сделать в рамках объекта - это получить исходную строку и закодированную),
но при этом лучше изучил реализацию этого алгоритма в рамках кода.
'''