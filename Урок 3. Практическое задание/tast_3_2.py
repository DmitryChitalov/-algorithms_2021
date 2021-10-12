import hashlib, uuid
import pymysql




def my_hash_passwd():
    input_first = input('Введите пароль : ')
    hash_first = hashlib.sha256(input_first.encode('utf-8')).hexdigest()
    print(hash_first)
    print(f'С генерированный пароль - {hash_first}')

    input_second = input('Введите еще раз пароль :')
    hash_secont = hashlib.sha256(input_second.encode('utf-8')).hexdigest()

    if hash_first == hash_secont:
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели не правильный пароль')

# Вариант 1
my_hash_passwd()



# Вариант 2 работаем через файл
def files_save(txt):
    f = open('passwd.txt', 'w', encoding='utf-8')
    f.write(txt)
    f.close()
    return print('хеш от пароля сохранен в файл passwd.txt')

def files_load():
    f = open('passwd.txt', 'r', encoding='utf-8')
    xeh_pass = f.readline()
    f.close()
    return xeh_pass


def my_hash_passwd_file():
    input_first = input('Введите пароль : ')
    hash_first = hashlib.sha256(input_first.encode('utf-8')).hexdigest()
    files_save(hash_first)                                          # Сохраняем хеш пароль в файл 'passwd.txt'

    input_second = input('Введите еще раз пароль :')
    hash_secont = hashlib.sha256(input_second.encode('utf-8')).hexdigest()
    hash_load = files_load()                                        # Загружаем хеш пароль из файла.
    if hash_load == hash_secont:
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели не правильный пароль')


my_hash_passwd_file()




# Вариант 3 Работа с БД.
def save_db(txt_hash):
    try:
        try:
            connect = pymysql.connect(host='localhost', user='root', password='mysql', db='algoritm')
            print("Connection Good")
            with connect.cursor() as cursor:
                my_password = txt_hash
                insert_query = f"insert into `hash_password` (my_password) values ('{my_password}');"
                cursor.execute(insert_query)
                connect.commit()
        finally:
            connect.close()
    except Exception as ex:
        print("Connection Error")

def load_db():
    try:
        try:
            connect = pymysql.connect(host='localhost', user='root', password='mysql', db='algoritm')
            print("Connection Good")
            with connect.cursor() as cursor:
                insert_query = f"select my_password from hash_password"
                cursor.execute(insert_query)
                return str(cursor.fetchone())[2:-3]

        finally:
            connect.close()
    except Exception as ex:
        print("Connection Error")




def hash_passwd_db():
    input_first = input('Введите пароль : ')
    hash_first = hashlib.sha256(input_first.encode('utf-8')).hexdigest()
    save_db(hash_first)

    print(f'С генерированный пароль - {hash_first}')

    input_second = input('Введите еще раз пароль :')
    hash_secont = hashlib.sha256(input_second.encode('utf-8')).hexdigest()
    load_hash = load_db()
    if load_hash == hash_secont:
        print('Вы ввели правильный пароль')
    else:
        print('Вы ввели не правильный пароль')

hash_passwd_db()