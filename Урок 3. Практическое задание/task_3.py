""" Задание 3.
Определить количество различных (уникальных) подстрок с использованием хеш-
функции. Дана строка S длиной N, состоящая только из строчных латинских букв.

Подсказка: примените вычисление хешей для подстрок с помощью хеш-функций и
множества Можно воспользоваться ф-цией hash() (см. материалы к уроку)

Пример:
рара - 6 уникальных подстрок
рар
ра
ар
ара
р
а

Экономия на размере хранимых данных (для длинных строк) и
скорость доступа вместе с уникальностью элементов,
которые даёт множество, сделают решение коротким и эффективным."""


def get_uniq_substr_v1(src_str: str):
    """возвращает множество всех уникальных подстрок переданной строки"""
    # метод полного перебора подстрок с отсевом неуникальных добавлением в set
    uniq_substr_set = set()
    len_src_str = len(src_str)  # для читабельности - зададим алиас
    for len_substr in range(1, len_src_str):
        # print(f'{len_substr=}')
        for idx in range(0, (len_src_str - len_substr + 1)):
            curr_substr = src_str[idx:(idx + len_substr)]
            uniq_substr_set.add(curr_substr)
            # print(f'{idx=}, {curr_substr=}, {uniq_substr_set=}')
    return uniq_substr_set


def get_uniq_substr_v2(src_str: str):
    """возвращает множество всех уникальных подстрок переданной строки"""
    uniq_substr_set = set()
    len_src_str = len(src_str)  # для читабельности - зададим алиас
    for len_substr in range(1, len_src_str):
        # print(f'{len_substr=}')
        for idx in range(0, (len_src_str - len_substr + 1)):
            curr_substr = src_str[idx:(idx + len_substr)]
            hash_curr_substr = hash(curr_substr)
            uniq_substr_set.add(hash_curr_substr)
            # print(f'{idx=}, {curr_substr=}, {hash_curr_substr=},'
            #       f' {uniq_substr_set=}')
    return uniq_substr_set


if __name__ == '__main__':
    print('Скрипт вычисляет кол-во уникальных подстрок переданной на вход '
          'строки, состоящей только из строчных латинских букв\n')

    source_str = input('Введите строку для анализа: ')

    uniq_substr = get_uniq_substr_v1(source_str)
    print('\nМетод 1 - хранение в множестве самих уникальных подстрок.')
    print(f'В строке "{source_str}" содержится '
          f'{len(uniq_substr)} уникальных подстрок!')
    # print(*uniq_substr, sep='\n')

    uniq_hash_substr = get_uniq_substr_v2(source_str)
    print('\nМетод 2 - хранение в множестве хешей уникальных подстрок.')
    print(f'В строке "{source_str}" содержится '
          f'{len(uniq_hash_substr)} уникальных подстрок!')
    # print(*uniq_hash_substr, sep='\n')
