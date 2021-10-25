from collections import defaultdict


# вносим в словарь через коллекию
def entering_data():
    # метод upper() здесь играет роль ввода строчными латинскими буквами, переводя их в заглавные.
    first_number = (input('Введите 1-ое целое шестнадцатиричное число: ').upper())
    second_number = (input('Введите 2-ое целое шестнадцатиричное число: ').upper())
    storage = defaultdict(list)
    for bulkhead_1 in first_number:
        storage[first_number].append(bulkhead_1)
    for bulkhead_2 in second_number:
        storage[second_number].append(bulkhead_2)
    print(storage)
    return storage


# defaultdict(<class 'list'>, {'A2': ['A', '2'], 'C4F': ['C', '4', 'F']})

# сумма и произведение
def calculation():
    storage = entering_data()
    record = []
    for value in storage.values():
        refund = ''.join(value)
        numbers = int(refund, 16)
        record.append(numbers)
    return record


# выводим результат произведения и суммы
def completion():
    record = calculation()
    analysis = '0123456789ABCDEF'
    composition = record[0] * record[1]
    result = ''
    while composition > 0:
        result = analysis[composition % 16] + result
        composition //= 16

    addition = sum(record)
    result_1 = ''
    while addition > 0:
        result_1 = analysis[addition % 16] + result_1
        addition //= 16
    print(f'Сумма: {list(result_1)}')
    print(f'Произведение: {list(result)}')


completion()

"""
defaultdict(<class 'list'>, {'CCF': ['C', 'C', 'F'], '2FA': ['2', 'F', 'A']})
Сумма: ['F', 'C', '9']
Произведение: ['2', '6', '2', '0', '2', '6']

defaultdict(<class 'list'>, {'A2': ['A', '2'], 'C4F': ['C', '4', 'F']})
Сумма: ['C', 'F', '1']
Произведение: ['7', 'C', '9', 'F', 'E']
"""
