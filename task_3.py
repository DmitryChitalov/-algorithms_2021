def strings(new_str):
    my_list = []
    for i in range(len(new_str)):
        my_list.append(new_str[i])
        my_list.append(new_str[i:])
        my_list.append(new_str[:-i])

    my_list = set(my_list)
    my_hash = []
    for el in my_list:
        my_hash.append(hash(el))
    elements = len(my_hash)
    return elements


print(strings('gramma'))

#не уверена как правильно найти все подстроки, попыталась вот так, но все равно находит не все