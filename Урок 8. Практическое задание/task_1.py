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


class HaffmanCode:
    def __init__(self, str_obj: str):
        self.__data = str_obj
        self.__count_str = deque(sorted(Counter(str_obj).items(), key=lambda el: el[1]))
        self.tree = None

    # Функция получения значения
    def decode_in_str(self):
        return self.__data

    # Функция получения строки в бинарном формате
    def decode_in_bin(self):
        res = ' '.join(format(ord(i), 'b') for i in self.__data)
        return res

    # Функция кодировки по методу Хаффмана
    def encode(self):
        if len(self.__count_str) != 1:
            # Цикл для построения дерева
            while len(self.__count_str) > 1:
                # далее цикл объединяет два крайних левых элемента
                # Вес объединенного элемента (накопленная частота)
                # веса - 2, 4, 4, 7, 8, 15
                weight = self.__count_str[0][1] + self.__count_str[1][1]
                comb = {0: self.__count_str.popleft()[0],
                        1: self.__count_str.popleft()[0]}
                # Ищем место для ставки объединенного элемента
                for i, _count in enumerate(self.__count_str):
                    if weight > _count[1]:
                        continue
                    else:
                        # Вставляем объединенный элемент
                        # deque([({0: 'r', 1: '!'}, 2), ('p', 2), (' ', 2), ('o', 2), ('b', 3), ('e', 4)])
                        self.__count_str.insert(i, (comb, weight))
                        break
                else:
                    # Добавляем объединенный корневой элемент после
                    # завершения работы цикла
                    self.__count_str.append((comb, weight))
        else:
            # приравниваемыем значение 0 к одному повторяющемуся символу
            weight = self.__count_str[0][1]
            comb = {0: self.__count_str.popleft()[0], 1: None}
            self.__count_str.append((comb, weight))

        self.tree = self.__count_str[0][0]  # Собираем дерево

        code_table = {}

        # Функция для кодировки дерева
        def haffman_code(tree, path=''):
            # Если элемент не словарь, значит мы достигли самого символа
            # и заносим его, а так же его код в словарь (кодовую таблицу).
            if not isinstance(tree, dict):
                code_table[tree] = path
            # Если элемент словарь, рекурсивно спускаемся вниз
            # по первому и второму значению (левая и правая ветви).
            else:
                haffman_code(tree[0], path=f'{path}0')
                haffman_code(tree[1], path=f'{path}1')

        haffman_code(self.tree)  # Кодируем с помощью внутренней функции наше дерево

        code_table = ' '.join(code_table.values())  # Получаем результат в виде строки

        return code_table


h_code = HaffmanCode('beep boop beer!')

print(h_code.encode())
print(h_code.decode_in_bin())
