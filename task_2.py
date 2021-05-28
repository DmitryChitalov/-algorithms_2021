import hashlib


def passwd():
    f = open('text.txt', 'w+')
    new_passwd = input("Придумайте пароль: ")
    hash_obj = hashlib.md5(new_passwd.encode()).hexdigest()
    f.write(hash_obj + '\n')
    check_passwd = input("Проверьте пароль: ")
    hash_obj_1 = hashlib.md5(check_passwd.encode()).hexdigest()
    f.write(hash_obj_1 + '\n')
    f.seek(0)
    first = f.readline()
    second = f.readline()
    if first == second:
        print("Все верно")
    else:
        print("Вы ввели пароль не верно, попробуйте снова.")
        f.seek(0)
        f.truncate()
        return passwd()
    f.close()


passwd()
