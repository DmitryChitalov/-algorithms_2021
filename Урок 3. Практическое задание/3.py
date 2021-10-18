import hashlib


def unique_wrd_1(words):
    storing_set = set()
    for i in range(len(words)):
        for g in range(len(words) - 1 if i == 0 else len(words), i, -1):
            storing_set.add(hashlib.sha256(words[i:g].encode()).hexdigest())
            print(words[i:g], end=' ')

    print('\n', storing_set)
    print("Количество различных подстрок в этой строке:", len(storing_set))


def unique_wrd_2(words):
    storing_set_2 = set()
    for i in range(len(words)):
        for g in range(len(words) - 1 if i == 0 else len(words), i, -1):
            storing_set_2.add(hash(words[i:g]))
            print(words[i:g], end=' ')

    print('\n', storing_set_2)
    print("Количество различных подстрок в этой строке:", len(storing_set_2))


analysis = 'papa'
unique_wrd_1(analysis)
print('_' * 500)
unique_wrd_2(analysis)
