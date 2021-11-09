import random


def get_min_value_v1(data: list) -> int:
    '''
    Поиск минимального значеия O(n^2)
    '''

    data_copy = data.copy()
    for i in range(len(data_copy)):
        for j in range(len(data_copy)):
            if data_copy[i] < data_copy[j]:
                data_copy[i], data_copy[j] = data_copy[j], data_copy[i]
    return data_copy[0]


def get_min_value_v2(data: list) -> int:
    '''
    Поиск минимального значения O(n)
    '''

    result = None
    for x in data:
        if result == None or x < result:
            result = x
    return result


def main():
    data = [random.randint(0, 10000) for _ in range(100)]
    print(f'Input data: {data}')
    print(f'Min value v1: {get_min_value_v1(data)}')
    print(f'Min value v2: {get_min_value_v2(data)}')


if __name__ == '__main__':
    main()
