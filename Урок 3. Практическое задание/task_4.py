"""
Задание 4.
Реализуйте скрипт "Кэширование веб-страниц"

Функция должна принимать url-адрес и проверять
есть ли в кэше соответствующая страница, если нет, то вносить ее в кэш

Подсказка: задачу решите обязательно с применением 'соленого' хеширования и хеш-таблиц
Можете условжнить задачу, реализовав ее через ООП
Не забудьте, что кэширование - механизм, а хеш-таблица - средство его реализации.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

# from uuid import uuid4
import hashlib


# class WebCash:
#     """
#
#     Класс хеш-таблиц для хранения, проверки и использования хешей url-адресов открываемых веб-страниц
#
#     """
#     def __init__(self, hash_tbl, url, web_name, salt):
#         self.hash_tbl = hash_tbl
#         self.url = url
#         self.web_name = web_name
#         self.salt = salt
#
#     @staticmethod
#     def get_hash_cooked():
#         url_hash = hashlib.sha256(url.encode()).hexdigest()
#         return url_hash
#
#     def get_url_checked(self):
#         for h in hash_tbl.keys():
#             if url_hash == h:
#                 return hash_tbl[h]
#         return f'Web-site {web_name} is new-opened {url_hash}'
#
#     def get_url_in_cash(self):
#         pass
#
#
# hash_tbl = {'525fcfc5f271962740cde1d80c826da354798bdabbc84456270d250412a71ed0': 'italki'}
# url = 'https://www.italki.com'
# web_name = 'italki'
# salt = uuid4().hex
# italki = WebCash(hash_tbl, url, web_name, salt)
# print(italki.get_hash_cooked())

# реализация через функции:

def get_hash_cooked(url_str, web_name_str):
    return hashlib.sha256(web_name_str.encode() + url_str.encode()).hexdigest()


def get_url_checked_in_cash(hash_dict, url_hash_str, web_name_str):
    for h in hash_dict.keys():
        if url_hash_str == h:
            print(f'it is {hash_dict[h]} url-adress')
            return hash_dict
    hash_dict[url_hash_str] = web_name_str
    print(f'web-site {web_name_str} is newly-opened. put in cash')
    return hash_dict


if __name__ == '__main__':
    hash_tbl = {
        '41436726b4b3d0fd37f682aeb485ae5056526eef04449d607f177fd2eb184432': 'stepik',
        '12726e1d6cce142ff9b1b0c12a16763a8bf6d52b22fd2b0e23488b1da394bda3': 'gosuslugi',
        '1dd6a61a1ca0dfa2475e412e110a5fafd2a1050a69c5d0c275653e4ba25a7bf9': 'nalog'
    }
    url1 = 'https://www.italki.com'
    web_name1 = 'italki'
    # salt = uuid4().hex
    url_hash1 = get_hash_cooked(url1, web_name1)
    hash_tbl = get_url_checked_in_cash(hash_tbl, url_hash1, web_name1)

    url2 = 'https://www.nalog.gov.ru'
    web_name2 = 'nalog'
    url_hash2 = get_hash_cooked(url2, web_name2)
    hash_tbl = get_url_checked_in_cash(hash_tbl, url_hash2, web_name2)

    url3 = 'https://www.amazon.com/'
    web_name3 = 'amazon'
    url_hash3 = get_hash_cooked(url3, web_name3)
    hash_tbl = get_url_checked_in_cash(hash_tbl, url_hash3, web_name3)
    print(hash_tbl)

print()

# то же самое через ООП
class WebCash:
    def __init__(self, hash_dict, url_str, web_name_str):
        self.hash_dict = hash_dict
        self.url_str = url_str
        self.web_name_str = web_name_str

    def get_hash_cooked(self):
        return hashlib.sha256(self.web_name_str.encode() + self.url_str.encode()).hexdigest()

    def get_url_checked_in_cash(self, url_hash_str):
        for h in self.hash_dict.keys():
            if url_hash_str == h:
                print(f'it is {self.hash_dict[h]} url-adress')
                return self.hash_dict
        self.hash_dict[url_hash_str] = self.web_name_str
        print(f'web-site {self.web_name_str} is newly-opened. put in cash')
        return self.hash_dict


    def put_url_in_cash(self):
        pass


if __name__ == '__main__':
    hash_tbl_11 = {}
    url_11 = 'https://www.italki.com'
    web_name_11 = 'italki'
    web_obj_11 = WebCash(hash_tbl_11, url_11, web_name_11)
    hash_str_11 = web_obj_11.get_hash_cooked()
    hash_tbl_11 = web_obj_11.get_url_checked_in_cash(hash_str_11)
    print(f'renewed hash_tbl: {web_obj_11.get_url_checked_in_cash(hash_str_11)}')