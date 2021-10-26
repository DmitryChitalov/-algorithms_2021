import random
from statistics import median


def get_data_from_user() -> list:
    while True:
        el_count = input("Введите m: ")
        print(el_count)
        if el_count.isdigit():
            el_count = int(el_count)
            break
        else:
            print("Ввод неверный, повторите попытку")

    return [random.randint(0, 50) for _ in range(2 * el_count + 1)]


orig_list = get_data_from_user()
med_index = orig_list
print("Оригинальный список: ")
print(*orig_list)

print("Медиана из модуля statistics(для проверки): ", median(orig_list))

[orig_list.remove(max(orig_list)) for _ in range(int(len(orig_list) / 2))]

print("Медиана полученная удалением максимальных элементов: ", max(orig_list))
