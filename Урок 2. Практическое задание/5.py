i = 1
for char in range(32, 127 + 1):
    if i % 10 == 0:
        print(f'{char:5}: {chr(char)}')
    else:
        print(f'{char:5}: {chr(char)}', end=' ')
    i += 1

