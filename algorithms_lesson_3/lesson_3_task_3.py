import hashlib


final_set = set()
origin_str = 'kolovorot'
for i in range(len(origin_str)):
    for k in range(i + 1, len(origin_str) + 1):
        if origin_str[i:k] == origin_str:
            continue
        print(origin_str[i:k])
        final_set.add(hashlib.sha256(origin_str[i:k].encode()).hexdigest())
        # final_set.add(origin_str[i:k]) без хеша результат тот же
print(f'{final_set}')
print(f'The number of unique substrings is {len(final_set)}')
