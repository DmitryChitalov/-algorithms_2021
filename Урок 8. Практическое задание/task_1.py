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


def haff_tree(st):
    #  подсчет уникальных символов
    count = Counter(st)
    #сортируем повторения по возрастанию
    sort_elem = deque(sorted(count.items(), key=lambda  item: item[1]))
    if len(sort_elem) != 1: #проверка строки на повторяющиеся элементы
        # Построение дерева с помощью цикла
        while len(sort_elem) > 1: # цикл объединяет два крайних эл-та
            # вес накопленного элемента
            weight = sort_elem[0][1] + sort_elem[1][1]
            # словарь из 2 крайних элементаб попутно вырезаем из "sort_elem"(из очереди)
            # comb  - объединенный элемент
            combined_element = {0: sort_elem.popleft()[0],
                    1: sort_elem.popleft()[0]}
        # ищем место для вставки объединенного элемента
            for i, _count in enumerate(sort_elem):
                if weight > _count[1]:
                    continue
                else:
                # вставляем объединенный элемент
                    sort_elem.insert(i, (combined_element, weight))
                    break
            else:
                # добавляем объединенный корневой элемент после заверш. цикла
                sort_elem.append((combined_element, weight))

    else: # приравнивание значение 0 к одному повторяющемуся символу
        weight = sort_elem[0][1]
        combined_element = {0: sort_elem.popleft()[0], 1: None}
        sort_elem.append((combined_element, weight))
    return sort_elem[0][0]


cod_tbl = dict()

def haff_cod(tree, path=''):
    # если элемент не словарь мы достигли самого символа и заносим его,
    # а так же заносим его код в кодовую таблицу
    if not isinstance(tree, dict):
        cod_tbl[tree] = path
    #если элемент словарьб рекурсивно спускаемся вниз по 1-му и 2-му значениям(левая и правая ветви)
    else:
        haff_cod(tree[0], path=f'{path}0')
        haff_cod(tree[1], path=f'{path}1')

#строка для кодирования
st = input(str("Введите строку для шифрования: "))

haff_cod(haff_tree(st))

for i in st:
    print(cod_tbl[i], end=' ')
print()