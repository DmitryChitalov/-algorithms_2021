def unique_value(text):
    substrings_hash = {}
    for i in range(len(text) + 1):
        for j in range(i + 1, len(text) + 1):
            substring = text[i:j]
            substrings_hash[hash(substring)] = substring
    substrings_hash.pop(hash(text))
    return substrings_hash


def substrings_print(text):
    for value in unique_value(text).values():
        print(value)
    return f''


print(substrings_print('papa'))
