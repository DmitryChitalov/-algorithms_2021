"""
Задание 1.

Выполните профилирование памяти в скриптах.
Проанализируйте результат и определите программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять только домашние задания с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""


from memory_profiler import profile
from json import dumps, loads
from numpy import array


@profile
def read_txt(txt):
    with open(txt, encoding='UTF-8') as text:
        return [i.lower() for i in text.read().split()]


@profile
def read_txt_2(txt):
    with open(txt, encoding='UTF-8') as text:
        lst = [i.lower() for i in text.read().split()]
        lst_arr = array(lst)
        del lst
    return lst_arr

# print(lst)

# word_dict = {}


@profile
def similar_words(text_lst):
    word_dict = {}
    for word in text_lst:
        count = 0
        for i in text_lst:
            if word == i:
                count += 1
                word_dict[word] = count
    return word_dict


@profile
def similar_words_2(text_lst):
    lst = text_lst.copy()
    word_dict_2 = {}
    for word in lst:
        count = 0
        for i in lst:
            if word == i:
                count += 1
                word_dict_2[word] = count
    del lst, text_lst
    dumped_word_dict = dumps(word_dict_2)
    del word_dict_2
    return dumped_word_dict


@profile
def sort_dict(dic):
    sorted_tuple = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_tuple)


@profile
def sort_dict_2(dic):
    dic = loads(dic)
    sorted_tuple = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    return dict(sorted_tuple)


print(sort_dict(similar_words(read_txt('text.txt'))))

print(sort_dict_2(similar_words_2(read_txt_2('text.txt'))))


'''
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    35     20.2 MiB     20.2 MiB           1   @profile
    36                                         def similar_words(text_lst):
    37     20.2 MiB    -98.6 MiB        3280       for word in text_lst:
    38     20.2 MiB    -98.5 MiB        3279           count = 0
    39     20.2 MiB -323327.0 MiB    10755120           for i in text_lst:
    40     20.2 MiB -323228.5 MiB    10751841               if word == i:
    41     20.2 MiB  -1302.2 MiB       43811                   count += 1
    42     20.2 MiB  -1302.2 MiB       43811                   word_dict[word] = count
    43     20.1 MiB     -0.0 MiB           1       return word_dict
    
    Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    64     20.5 MiB     20.5 MiB           1   @profile
    65                                         def sort_dict(dic):
    66     20.5 MiB      0.0 MiB        4263       sorted_tuple = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    67     20.6 MiB      0.1 MiB           1       return dict(sorted_tuple)
    
    Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    50     20.7 MiB     20.7 MiB           1   @profile
    51                                         def similar_words_2(text_lst):
    52     20.7 MiB      0.0 MiB           1       word_dict_2 = {}
    53     20.7 MiB      0.0 MiB        3280       for word in text_lst:
    54     20.7 MiB      0.0 MiB        3279           count = 0
    55     20.7 MiB      0.0 MiB    10755120           for i in text_lst:
    56     20.7 MiB      0.0 MiB    10751841               if word == i:
    57     20.7 MiB      0.0 MiB       43811                   count += 1
    58     20.7 MiB      0.0 MiB       43811                   word_dict_2[word] = count
    59     21.0 MiB      0.3 MiB           1       dumped_word_dict = dumps(word_dict_2)
    60     21.0 MiB      0.0 MiB           1       word_dict.clear()
    61     21.0 MiB      0.0 MiB           1       return dumped_word_dict


Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    70     21.0 MiB     21.0 MiB           1   @profile
    71                                         def sort_dict_2(dic):
    72     21.0 MiB      0.0 MiB           1       dic = loads(dic)
    73     21.0 MiB      0.0 MiB        4263       sorted_tuple = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    74     21.0 MiB      0.0 MiB           1       return dict(sorted_tuple)
    

Три дня пытался разобраться, так и не понял до конца, очень много своих скриптов перепробовал, ни в одном результатов
не добился (в контексте скриптов, а не искусственного создания и удаления массивов). Написал парсинг (условно) 
большого файла, вообще замеры странные -323327.0 MiB. В сети информации по memory_profiler очень мало и отзывы
о нем плохие: очень медленный так, как написан на чистом Python.
После использования numpy.array значения памяти увеличились на 10 MiB, удаление ссылок переменных ничего не даёт.

  
  Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    31     30.6 MiB     30.6 MiB           1   @profile
    32                                         def read_txt(txt):
    33     30.6 MiB      0.0 MiB           1       with open(txt, encoding='UTF-8') as text:
    34     30.7 MiB      0.1 MiB         492           lst = [i.lower() for i in text.read().split()]
    35     30.7 MiB      0.0 MiB           1           lst_arr = array(lst)
    36     30.7 MiB      0.0 MiB           1           del lst
    37     30.7 MiB      0.0 MiB           1       return lst_arr
    
    Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    44     30.7 MiB     30.7 MiB           1   @profile
    45                                         def similar_words(text_lst):
    46     30.7 MiB      0.0 MiB           1       word_dict = {}
    47     30.7 MiB      0.0 MiB         490       for word in text_lst:
    48     30.7 MiB      0.0 MiB         489           count = 0
    49     30.7 MiB      0.0 MiB      239610           for i in text_lst:
    50     30.7 MiB      0.0 MiB      239121               if word == i:
    51     30.7 MiB      0.0 MiB        1625                   count += 1
    52     30.7 MiB      0.0 MiB        1625                   word_dict[word] = count
    53     30.7 MiB      0.0 MiB           1       return word_dict




Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    72     30.7 MiB     30.7 MiB           1   @profile
    73                                         def sort_dict(dic):
    74     30.7 MiB      0.0 MiB         741       sorted_tuple = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    75     30.7 MiB      0.0 MiB           1       return dict(sorted_tuple)
    
    
    Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    31     30.8 MiB     30.8 MiB           1   @profile
    32                                         def read_txt(txt):
    33     30.8 MiB      0.0 MiB           1       with open(txt, encoding='UTF-8') as text:
    34     30.8 MiB      0.0 MiB         492           lst = [i.lower() for i in text.read().split()]
    35     30.8 MiB      0.0 MiB           1           lst_arr = array(lst)
    36     30.8 MiB      0.0 MiB           1           del lst
    37     30.8 MiB      0.0 MiB           1       return lst_arr




Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    56     30.8 MiB     30.8 MiB           1   @profile
    57                                         def similar_words_2(text_lst):
    58     30.8 MiB      0.0 MiB           1       lst = text_lst.copy()
    59     30.8 MiB      0.0 MiB           1       word_dict_2 = {}
    60     30.8 MiB      0.0 MiB         490       for word in lst:
    61     30.8 MiB      0.0 MiB         489           count = 0
    62     30.8 MiB      0.0 MiB      239610           for i in lst:
    63     30.8 MiB      0.0 MiB      239121               if word == i:
    64     30.8 MiB      0.0 MiB        1625                   count += 1
    65     30.8 MiB      0.0 MiB        1625                   word_dict_2[word] = count
    66     30.8 MiB      0.0 MiB           1       del lst, text_lst
    67     30.8 MiB      0.0 MiB           1       dumped_word_dict = dumps(word_dict_2)
    68     30.8 MiB      0.0 MiB           1       del word_dict_2
    69     30.8 MiB      0.0 MiB           1       return dumped_word_dict



Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    78     30.8 MiB     30.8 MiB           1   @profile
    79                                         def sort_dict_2(dic):
    80     30.8 MiB      0.0 MiB           1       dic = loads(dic)
    81     30.8 MiB      0.0 MiB         741       sorted_tuple = sorted(dic.items(), key=lambda x: x[1], reverse=True)
    82     30.8 MiB      0.0 MiB           1       return dict(sorted_tuple)
'''

from collections import namedtuple
from recordclass import recordclass
from memory_profiler import profile


ProfitEnterprise = namedtuple('profit_enterprise', 'first second third fourth')


enterprise = {}


def enter_info_enterprise(i):
    info_enterprise = input(f'Введите название предприятия {i} \n'
                            f'и через пробел прибыль данного предприятия\n'
                            f'за каждый квартал(Всего 4 квартала):').split()
    return info_enterprise


def number_enterprise():
    return int(input('Введите количество предприятий: '))


def average_profit():
    total_profit = []
    for profit in enterprise.values():
        for i in profit:
            total_profit.append(int(i))
    average = sum(total_profit) / len(total_profit)

    above_average = ''
    below_average = ''
    for title, profit in enterprise.items():
        if sum(map(int, profit)) > average:
            above_average += f'"{title}" '
        else:
            below_average += f'"{title}" '

    return f'Средняя годовая прибыль всех предприятий: {average}\n' \
           f'Предприятия, с прибылью выше среднего значения: {above_average}\n' \
           f'Предприятия, с прибылью ниже среднего значения: {below_average}'


@profile
def main():
    for i in range(1, number_enterprise() + 1):
        temp = enter_info_enterprise(i)
        enterprise[temp[0]] = ProfitEnterprise._make(temp[1:])
    return average_profit()


@profile
def main_2():
    for i in range(1, number_enterprise() + 1):
        temp = enter_info_enterprise(i)
        enterpr = recordclass('enterprise', ('first', 'second', 'third', 'fourth'))
        enterprise[temp[0]] = enterpr(first=temp[1], second=temp[2], third=temp[3], fourth=temp[4])
    return average_profit()


print(main())
print(main_2())

'''
Заменил namedtuple на recordclass - результат как и в примере выше, результатов так и не заметил.

Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    43     20.0 MiB     20.0 MiB           1   @profile
    44                                         def main():
    45     20.0 MiB      0.0 MiB           2       for i in range(1, number_enterprise() + 1):
    46     20.0 MiB      0.0 MiB           1           temp = enter_info_enterprise(i)
    47     20.0 MiB      0.0 MiB           1           enterprise[temp[0]] = ProfitEnterprise._make(temp[1:])
    48     20.0 MiB      0.0 MiB           1       return average_profit()
    
Line #    Mem usage    Increment  Occurences   Line Contents
============================================================
    51     20.1 MiB     20.1 MiB           1   @profile
    52                                         def main_2():
    53     20.1 MiB      0.0 MiB           2       for i in range(1, number_enterprise() + 1):
    54     20.1 MiB      0.0 MiB           1           temp = enter_info_enterprise(i)
    55     20.1 MiB      0.0 MiB           1           enterpr = recordclass('enterprise', ('first', 'second', 'third', 'fourth'))
    56     20.1 MiB      0.0 MiB           1           enterprise[temp[0]] = enterpr(first=temp[1], second=temp[2], third=temp[3], fourth=temp[4])
    57     20.1 MiB      0.0 MiB           1       return average_profit()
'''