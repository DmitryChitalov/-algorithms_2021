def find_unique_substring(my_string):
    my_set = set()
    for i in range(1, len(my_string)):
        for j in range(len(my_string)):
            sub_string = my_string[j:j+i]
            my_set.add(hash(sub_string))

    substrings_count = len(my_set)
    return f"В строке: '{my_string}' {substrings_count} подстрок."


print(find_unique_substring('papa'))
