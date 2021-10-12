import time
def full_data():
    my_dict = {'one': 1, 'two': 2, 'three': 3, 'foo': 4}
    print(f'Время словаря = {time.time_ns()}')
    print(f'Время словаря в милисекундах = {time.perf_counter()}')

    my_spisok = []
    old_spisok = [1, 2, 3, 4]
    my_spisok.extend(old_spisok)
    print(f'Время исполнения Листа = {time.time_ns()}')
    print(f'Время исполнения листа в милисекундах = {time.perf_counter()}')
full_data()