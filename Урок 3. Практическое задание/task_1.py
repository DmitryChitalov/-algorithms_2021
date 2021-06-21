"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   и укажите сложность функций для заполнения.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   и укажите сложность функций для операций.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: если вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""
from time import time


def timer(func):
    def f():
        start = time()
        result = func()
        end = time()
        print(f"Время выполнения: {end - start}")
        return result

    return f


@timer
def list_generator():
    return [el for el in range(10 ** 7)]        # O(n)


@timer
def dict_generator():
    return {el: el for el in range(10 ** 7)}    # O(n)


# не работает
# @timer
def list_operator(lst, count=0):
    if len(lst) > 0 and count < 900:
        lst.pop(count)                          # O(n)
        return list_operator(lst, count + 1)


# не работает
# @timer
def dict_operator(dct, count=0):
    if len(dct) > 0 and count < 900:
        dct.pop(count)                          # O(n)
        return dict_operator(dct, count + 1)


generated_list = list_generator()
generated_dict = dict_generator()

start = time()
print("Удаление из списка по индексу:")
list_operator(generated_list)
end = time()
print(end - start)

start = time()
print("Удаление из словаря по ключу:")
dict_operator(generated_dict)
end = time()
print(end - start)
