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


def tree(s):
    count = Counter(s)
    sorted_elements = deque(sorted(count.items(), key=lambda item: item[1]))
    if len(sorted_elements) != 1:

        while len(sorted_elements) > 1:
            weight = sorted_elements[0][1] + sorted_elements[1][1]
            comb = {0: sorted_elements.popleft()[0],
                    1: sorted_elements.popleft()[0]}

            for i, _count in enumerate(sorted_elements):
                if weight > _count[1]:
                    continue
                else:
                    sorted_elements.insert(i, (comb, weight))
                    break
            else:
                sorted_elements.append((comb, weight))
    else:
        weight = sorted_elements[0][1]
        comb = {0: sorted_elements.popleft()[0], 1: None}
        sorted_elements.append((comb, weight))
    return sorted_elements[0][0]


def haf_code(tree, path=''):
    if not isinstance(tree, dict):
        code_table[tree] = path
    else:
        haf_code(tree[0], path=f'{path}0')
        haf_code(tree[1], path=f'{path}1')


if __name__ == '__main__':
    code_table = dict()
    string = "beep boop beer!"
    haf_code(tree(string))

    for i in string:
        print(code_table[i], end=' ')
    print()

"""
Дмитрий, спасибо за представленный курс. Праваило подтвердилось: "Все что я знаю - это то,
что ничего не знаю". Очень много интересного и полезного, что обязательно возьму на вооружение.
Пытался в ДЗ по 8-му уроку изобрести вилосипед без подсказок в течении 4-х дней (через коллекции, ООП 
с визуаьным выводом), но на 4-5 уровне вводимые данные начинали некорректно распределяться по дереву
(понимаю из-за чего, но не понял как это обойти). Знаю, что со временем это всетаки войдет в меня,
Но на сегодняшний момент ничего своего толкового предложить не могу, а говнокод отправлять не хочется,
да и время поджимает.
Спасибо за науку!
"""