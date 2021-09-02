def substring_count(string: str):
    # набор уникальных подстрок
    result = set()

    # список все подстрок
    for i in range(len(string)):
        for j in range(i + 1, len(string) + 1):
            # Вычисляем Хэш и добавляем его во множество
            hash_obj = hash(string[i:j])
            result.add(hash_obj)
            # result.add(string[i:j])

        # Return the HashSet
    return len(result)


if __name__ == '__main__':
    my_string = "abracatabra"
    subs = substring_count(my_string)
    print(f"Количество уникальных подстрок для строки {my_string}: {subs}")
