"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""

from uuid import uuid4
from time import time

random_list = []
random_dict = {}


def speed_list(lst, strain):
    start = time()

    for _ in range(1, strain):
        lst.append(uuid4().hex)

    ending = time()
    return ending - start


def speed_dict(dct, strain):
    start = time()

    for key in range(1, strain):
        dct[key] = uuid4().hex

    ending = time()
    return ending - start


print(f'speed test list 1 {speed_list(random_list, 101)}')
print(f'speed test list 2 {speed_list(random_list, 1001)}')
print(f'speed test list 3 {speed_list(random_list, 100001)}')
print()
print(f'speed test dict 1 {speed_dict(random_dict, 101)}')
print(f'speed test dict 2 {speed_dict(random_dict, 1001)}')
print(f'speed test dict 3 {speed_dict(random_dict, 100001)}')
print()

"""
Результат теста заполнения на моём пк:
speed test list 1 0.0007414817810058594
speed test list 2 0.005364656448364258
speed test list 3 0.39629197120666504

speed test dict 1 0.0003819465637207031
speed test dict 2 0.0039768218994140625
speed test dict 3 0.40450620651245117

"""

print(min(0.0007414817810058594, 0.0003819465637207031))
print(min(0.005364656448364258, 0.0039768218994140625))
print(min(0.39629197120666504, 0.40450620651245117))

"""
Мы видим что скорость зависит от колличества операций.
Словарь на 101 и 1001 колличестве был чуть быстрее списка,
но на 100001 его уделал по скорости список. 
"""


def speed_list_2(lst):
    start = time()

    if lst[50000] in lst:
        print(True)

    ending = time()
    return ending - start


def speed_dict_2(dct):
    start = time()

    if dct[50000] in dct.values():
        print(True)

    ending = time()
    return ending - start


print(f'speed test list 4 {speed_list_2(random_list)}')
print(f'speed test dict 4 {speed_dict_2(random_dict)}')

"""
Результат теста заполнения на моём пк:
speed test list 4 0.0007843971252441406
speed test dict 4 0.001051187515258789
"""

print(min(0.0007843971252441406, 0.001051187515258789))

"""
Как мы видим судя по времени в списке быстрее искать по индексу
чем в словаре по ключу. Несмотря на то что в словаре ключи хэшируемый объект
и по ключу скорость должна быть быстрой в связи с этим, но в тесте на время я не увидел
преимущества словаря перед списком. Скорее напротив в больших объёмах данных список выигрывает
словарь в первых двух тестах.
"""


def speed_list_3(lst):
    start = time()

    print(lst[50000])

    ending = time()
    return ending - start


def speed_dict_3(dct):
    start = time()

    print(dct[50000])

    ending = time()
    return ending - start


print(f'speed test list 5 {speed_list_3(random_list)}')
print(f'speed test dict 5 {speed_dict_3(random_dict)}')

"""
Результат теста заполнения на моём пк:
speed test list 5 2.6226043701171875e-06
speed test dict 5 5.4836273193359375e-06
"""

print(min(2.6226043701171875e-06, 5.4836273193359375e-06))

"""
В третьем тесте мы вывели по ключу значение словаря и значение по индексу из списка.
В итоге список оказался опять быстрее. Обращение по ключу O(1) сложность, по индексу
O(1) сложность. Поиск в списке O(N) сложность, а поиск в словаре это O(1). В связи с
этим рекомендуется использовать словарь, так как ключ хешируемый. for в словаре и в списке
имеют O(N) сложности. Лучше всего опираться на сложность, чем на время при анализе алгоритмов.
В этом случае мы видим что for проход сложность одинаковая. Во втором тесте if in 
сложность разная и быстрее должен быть словарь O(1) против O(N). В третьем случае сложность
одинаковая O(1). По результатам оценки сложности в O большое преимущество у словаря. Также я
заметил что показатель времени может быть не стабилен и в некоторых случаях быстрее оказывается
словарь. Что даёт дополнительную сложность оценке.
"""
