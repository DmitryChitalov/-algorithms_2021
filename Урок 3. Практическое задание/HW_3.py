def find(my_str, ss_list=[]):
    for el in range(len(my_str)):  # Разбивание строки от начала
        ss_list.append(my_str[el + 1:])
    for el in range(len(my_str)):  # Разбивание строки от конца
        ss_list.append(my_str[:el])
    reversed_my_str = my_str[::-1]
    for el in range(len(my_str)):  # Разбивание перевернутой строки от конца
        ss_list.append(reversed_my_str[:el])
    for el in range(len(my_str)):  # Разбивание перевернутой строки от начала
        ss_list.append(reversed_my_str[el+1:])
    print(f'Количесвто уникальных подстрок в строке: {len(set(ss_list)) - 1}')
    return set(ss_list)


print(find('рар'))
