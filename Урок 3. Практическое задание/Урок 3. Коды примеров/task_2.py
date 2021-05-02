"""Примеры с md5"""

import hashlib

hash_obj = hashlib.md5(b'Testing')
print(hash_obj)  # -> <md5 HASH object @ 0x0000021C4B589A20>
print(type(hash_obj))  # -> <class '_hashlib.HASH'>
res = hash_obj.hexdigest()
print(type(res))  # -> <class 'str'>
print(res)  # -> fa6a5a3224d7da66d9e0bdec25f62cf0 ==
                                # fa6a5a3224d7da66d9e0bdec25f62cf0

print()
hash_obj_2 = hashlib.sha1(("Тестинг").encode('utf-8'))
print(hash_obj_2)  # -> <md5 HASH object @ 0x0000021C4D53ED50>
print(type(hash_obj_2))  # -> <class '_hashlib.HASH'>
res_2 = hash_obj_2.hexdigest()
print(type(res_2))  # -> <class 'str'>
print(res_2)  # -> cb63de18e7c52d17e3b5e9743210ab74

# python -> json-строка -> байты
