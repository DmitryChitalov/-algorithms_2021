from hashlib import sha256


def uniq_substrings(result_set, target_string):
    for i in range(len(target_string) + 1):
        for j in range(i, len(target_string) + 1):
            substring = target_string[i:j]
            if len(substring) > 0 and len(substring) != len(target_string):
                my_hash = sha256(substring.encode('utf-8'))
                result_set.add(my_hash.hexdigest())
    return len(result_set)


if __name__ == '__main__':
    string_set = set()
    print(uniq_substrings(string_set, 'papa'))
