import time

def get_lst_time():
    start_time_lst = time.time()
    lst = [i for i in range(100000)]
    stop_time_lst = time.time()
    result_time = stop_time_lst - start_time_lst
    return print (f'Время заполнения списка: {result_time}')

def get_dct_time():
    start_time_dct = time.time()
    dct = {x: x for x in range(100000)}
    stop_time_dct = time.time()
    result_time = stop_time_dct - start_time_dct
    return print(f'Время заполнения словаря: {result_time}')

def get_lst_el():
    lst = [i for i in range(100000)]
    start_time_lst = time.time()
    temp = lst[12345]
    stop_time_lst = time.time()
    result_time = stop_time_lst - start_time_lst
    return print(f'Время присвоения эл-та списка по индексу: {result_time}')

def get_dct_el():
    dct = {x: x for x in range(100000)}
    start_time_dct = time.time()
    temp = dct.get(12345)
    stop_time_dct = time.time()
    result_time = stop_time_dct - start_time_dct
    return print(f'Время присвоения эл-та словаря по ключу: {result_time}')

def get_lst_index():
    lst = [i for i in range(100000)]
    start_time_lst = time.time()
    temp = lst.index(12345)
    stop_time_lst = time.time()
    result_time = stop_time_lst - start_time_lst
    return print(f'Время поиска эл-та списка(индекс) по значению: {result_time}')

def add_list_el():
    lst = [i for i in range(100000)]
    start_time_lst = time.time()
    lst.append(666)
    stop_time_lst = time.time()
    result_time = stop_time_lst - start_time_lst
    return print(f'Время добавления эл-та в списко: {result_time}')

def add_dict_el():
    dct = {x: x for x in range(100000)}
    start_time_dct = time.time()
    dct.update({666666: 666666})
    stop_time_dct = time.time()
    result_time = stop_time_dct - start_time_dct
    return print(f'Время добавления элемента в словарь: {result_time}')

def pop_list_el():
    lst = [i for i in range(100000)]
    start_time_lst = time.time()
    lst.pop(666)
    stop_time_lst = time.time()
    result_time = stop_time_lst - start_time_lst
    return print(f'Время удаления эл-та из списка: {result_time}')

def pop_dict_el():
    dct = {x: x for x in range(100000)}
    start_time_dct = time.time()
    dct.pop(666)
    stop_time_dct = time.time()
    result_time = stop_time_dct - start_time_dct
    return print(f'Время удаления элемента из словаря: {result_time}')

get_lst_time()
get_dct_time()
get_lst_el()
get_dct_el()
add_list_el()
add_dict_el()
pop_list_el()
pop_dict_el()

# Заполнение словаря дольше, чем списка, потому что необходимо считать хэш

# Поиск по ключу в словаре происходит быстрее, чем поиск в списке (словарь хэш-таблица). Об этом говорят операции
#  "присвоения" элемента и "удаление" элемента в программе выше.
