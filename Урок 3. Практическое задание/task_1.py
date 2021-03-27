"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря программно,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
"""


from time import time


def count_time(func):
    def wrapper(*args):
        start_time = time()
        res = func(*args)
        end_time = time()
        print(end_time - start_time)
        return res
    return wrapper


@count_time
def gen_lst():
    print("Generate list:")
    return [i for i in range(10**5)]


@count_time
def gen_dict():
    print("Generate dictionary:")
    return {i: i for i in range(10**5)}


@count_time
def add_lst(lst):
    print("Update list:")
    [lst.append(i) for i in range(10**5, 10**6)]
    return lst


@count_time
def add_dct(dct):
    print("Update dictionary:")
    dct.update({i: i for i in range(10**5, 10**6)})
    return dct


@count_time
def delete_lst(lst):
    print("Delete in list:")
    [lst.pop(i) for i in range(10**6 - 1, 10**5 - 1, -1)]
    return lst


@count_time
def delete_dct(dct):
    print("Delete in dictionary:")
    [dct.pop(i) for i in range(10**5, 10**6)]
    return dct


my_lst = gen_lst()
my_dct = gen_dict()

my_lst = add_lst(my_lst)
my_dct = add_dct(my_dct)

my_lst = delete_lst(my_lst)
my_dct = delete_dct(my_dct)


"""
Мои результаты:
    Generate list:
    0.0029916763305664062
    Generate dictionary:
    0.004987239837646484
    Update list:
    0.053853511810302734
    Update dictionary:
    0.06283211708068848
    Delete in list:
    0.05086469650268555
    Delete in dictionary:
    0.064849853515625

Вывод:

a) Наполнение словаря происходит дольше, так как на этапе добавления ключа,
создается хэш, в избежании коллизии. В списке данной проверки нет.

б) Обновление производится дольше по той же причине, что и заполнение- проверка уникальности.
Удаление в словаре дольше, по всей видимости, из-за того,
что требуется удаление как самого ключа так и его значения.

По поводу вывода значения по ключу в словаре и индексу в списке, в разборе дз,
считаю несопоставимыми тесты и некорректным использование цикла for для списка,
так как индекс известен заранее и достаточно указать list[index] (возможно стоило,
для уравнивания ситуаций, применить цикл для перебора ключей словаря).
У себя не стал проверять вызов по индексу, так как он делается на столько
быстро в обоих случаях, что разница не фиксируется.
Прошу поправить, если я не прав в своих суждениях, по поводу взятия по индексу. 
"""