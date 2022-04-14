

def unique(string):
    my_set = set()
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            if string[i: j] != string:
                my_set.add(hash(string[i:j]))
    return len(my_set)


print(unique('papa'))
