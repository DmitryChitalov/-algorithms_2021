def sub(string):
    sub_lst = [] # список подстрочек
    sub_lst_hashed = [] # список хэшей подстрочек
    for i in range(len(string)):
        for j in range(len(string) - i):
            substring = string[i:len(string)-j] # формируем элементы списка подстрочек через срез исходной строчки
            sub_lst.append(substring) # формируем список
            sub_lst_hashed.append(hash(substring))
    sub_lst_hashed.remove(hash(string))  # удаляем хэш самой строки из списка хэшей подстрочек
    sub_lst.remove(string) # удаляем саму строку из списка
    result = set(sub_lst_hashed) # с помощью множества отсекаем повторяющиеся подстрочки
    sub_lst_res = set(sub_lst)
    print(f'Количество уникальных подстрок: {len(result)}')
    print(f'Подстрочки: {sub_lst_res}')


sub('papa')