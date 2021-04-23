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

        # исходный текст
        self.origin = origin
        # код по Хаффману
        self.__code_table = dict()

    def __make_tree(self):

        # Сортируем по возрастанию количества повторений.
        sorted_elements = deque(sorted(Counter(self.origin).items(), key=lambda item: item[1]))
        # Проверка, если строка состоит из одного повторяющего символа.
        if len(sorted_elements) != 1:
            # Цикл для построения дерева
            while len(sorted_elements) > 1:
                # далее цикл объединяет два крайних левых элемента
                # Вес объединенного элемента (накопленная частота)
                # веса - 2, 4, 4, 7, 8, 15
                weight = sorted_elements[0][1] + sorted_elements[1][1]
                # Словарь из 2 крайних левых элементов, попутно вырезаем их
                # из "sorted_elements" (из очереди).
                # comb - объединенный элемент
                comb = {0: sorted_elements.popleft()[0],
                        1: sorted_elements.popleft()[0]}
                # Ищем место для ставки объединенного элемента
                for ind, count in enumerate(sorted_elements):
                    if weight > count[1]:
                        continue
                    else:
                        # Вставляем объединенный элемент
                        # deque([({0: 'r', 1: '!'}, 2), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
                        sorted_elements.insert(ind, (comb, weight))
                        break
                else:
                    # Добавляем объединенный корневой элемент после
                    # завершения работы цикла
                    sorted_elements.append((comb, weight))
        else:
            # приравниваемыем значение 0 к одному повторяющемуся символу
            weight = sorted_elements[0][1]
            comb = {0: sorted_elements.popleft()[0], 1: None}
            sorted_elements.append((comb, weight))
            # sorted_elements -
            # deque([({0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}, 15)])
            # {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
            # словарь - дерево
        return sorted_elements[0][0]

    # tree - {0: {0: 'b', 1: {0: ' ', 1: 'o'}}, 1: {0: {0: {0: 'r', 1: '!'}, 1: 'p'}, 1: 'e'}}
    def __haffman_code(self, tree, path=''):

        # Если элемент не словарь, значит мы достигли самого символа
        # и заносим его, а так же его код в словарь (кодовую таблицу).
        if not isinstance(tree, dict):
            self.__code_table[tree] = path
        # Если элемент словарь, рекурсивно спускаемся вниз
        # по первому и второму значению (левая и правая ветви).
        else:
            self.__haffman_code(tree[0], path=f'{path}0')
            self.__haffman_code(tree[1], path=f'{path}1')

    def __str__(self):

        self.__haffman_code(self.__make_tree())
        result = ''
        # выводим коды для каждого символа
        for i in self.origin:
            result += f'{self.__code_table[i]} '
        return result


# строка для кодирования
obj = HaffMan('beep boop beer!')
# функция заполняет кодовую таблицу (символ-его код)
# {'b': '00', ' ': '010', 'o': '011', 'r': '1000', '!': '1001', 'p': '101', 'e': '11'}
print(f'Исходная строка: {obj.origin}')
print(f'Код Хаффмана: {obj}')

"""
Подогнал код под ООП, скрыл функции алгоритма Хаффмана.
(можно получить доступ только так obj._HaffMan__haffman_code)
"""
