"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух) разной!! сложности
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

from random import choice, randint

# Создадим хранилище

company_profit = {'company_' + str(_): randint(0, 1000000) for _ in range(10)}

# Выведем хранилище

print(' '.join(i + ':' + str(company_profit[i]) for i in company_profit))

##################################### First decision. #####################################

"""
Сложность - O(n**2) Мы пробегаем абсолютно все значения друг с другом. Пачка линейных пробегов
в конце кода сложности не добавляет.
Сортировка под названием "Странная".
"""


def top_three_1(dct):
    storage, storage_keys_sort = {}, []
    for i in dct:
        counter = 0
        for j in dct:
            if dct[i] < dct[j]:
                counter += 1
        if counter < 3:
            storage[i] = counter
    for i in range(3):  # Хранилища storage все еще не хватает для корректной работы. Если к примеру будет более трех
        for _ in storage:  # компании с равной наибольшей прибылью, равно как и 2 или 1 компания с наибольшей прибылью
            if storage[_] == i:  # плюс несколько компаний с равной по величине прибылью, но меньшей только чем у
                storage_keys_sort.append(_)  # вышеописанных, то в хранилище окажется больше трех элементов. Для этого
    storage = {_: storage[_] for _ in storage_keys_sort[:3]}  # мы и сортируем хранилище и выводим первых трех.
    return storage


print('\nПервое решение:')
print('Следующие компании получили наибольшую прибыль:', ' '.join(str(i) for i in top_three_1(company_profit)), '\n')

##################################### Second decision. #####################################

"""
Реализуем рандомный Quicksort. Хорошо бы выбирать середиинный элемент, но для его дополнительного нахождения
каждый раз потратится в среднем больше ресурсов, чем будет ожидаемая выгода от этого мероприятия.

Специально добавил решение сюда, чтобы порассуждать о сложности...
По хорошему, она будет O(nlog(n)) т.е. линейно-логарифмическая.
Но если вдруг так окажется, что массив уже отсортирован, то та же сортировка пузырьком за 1 проход скажет, что ничего не 
поменялось, значит хватит сортировать, а этот алгоритм будет упорно и долго копать всю коллекццию.
"""


def qsort(nums):
    if len(nums) <= 1:
        return nums
    else:
        symbol = choice(nums)
        nums_low, nums_high, nums_equal = [], [], []
        for i in nums:
            if i < symbol:
                nums_low.append(i)
            elif i > symbol:
                nums_high.append(i)
            else:
                nums_equal.append(i)
        return qsort(nums_low) + nums_equal + qsort(nums_high)


def top_three_2(dct):
    values = qsort(list(dct.values()))[-3:]
    keys = []
    for v in values:
        for k in dct:
            if dct[k] == v:
                keys.append(k)

    return keys[-3:]


print('Второе решение:')
print('Следующие компании получили наибольшую прибыль:', ' '.join(str(i) for i in top_three_2(company_profit)), '\n')

##################################### Third decision. #####################################

"""
Просто не напрягаясь пробежимся 3 раза по коллекции, вытащим ключи с максимальными значениями.
3 пробега. Зависим от длины сорваря => линейная сложность O(n)
"""


def top_three_3(dct):
    keys = []
    for _ in range(3):
        v_max, k_max = 0, ''
        for i in dct:
            if dct[i] > v_max and i not in keys:
                v_max = dct[i]
                k_max = i
        keys.append(k_max)
    return keys


print('Третье решение:')
print('Следующие компании получили наибольшую прибыль:', ' '.join(str(i) for i in top_three_3(company_profit)), '\n')

"""
Вывод:
"какое решение эффективнее" 

Эффективнее из трех решений самое простое, третье. Не всегда сложные и крутые инструменты вроде сортировки Хоара
дают лучший результат. Так что надо всегда в каждый момент рефлексировать на тему того, хороший ли код мы пишем.

"и почему"
 
В таблице к уроку было написано, что линейная сложность хороша тут)
Три пробега всегда будут лучше циклов, тем более вложенных.
Да и писать третье решение было быстрее и проще. Так что оно эффективнее еще и по времени разработки.
"""