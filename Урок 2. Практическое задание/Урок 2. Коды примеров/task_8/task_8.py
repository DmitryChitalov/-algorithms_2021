
import os


def get_directory_files(path):
    """Функция вывода содержимого директории"""
    struct = []
    for file_or_directory in os.listdir(path):
        full_name = os.path.join(os.path.abspath(path), file_or_directory)
        if os.path.isfile(full_name):
            struct.append((os.path.abspath(path), file_or_directory))
        else:
            struct.extend(get_directory_files(full_name))
    return struct


my_res = get_directory_files('mainapp')
print(my_res)
