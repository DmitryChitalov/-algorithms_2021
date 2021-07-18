"""
Задание 1.

Реализуйте свои пользовательские функции, в которых реализуйте:

a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
   И укажите сложность каждой ф-ции, которую вы применяете для заполнения.
   У этих ф-ций может быть разная сложность. Поэтому время заполнения списка и словаря может как совпадать, так и отличаться.
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
   И укажите сложность ф-ций, которые вы используете для операций.

Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)

Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""


# 1 В моем случае чуть быстрее заполняется список. Сложность одинакова, но заполнение словаря требует больше ресурсов


def timing(func):
    def f(*args):
        b_time = time.time()
        r = func(*args)
        e_time = time.time()
        return r, f'{e_time - b_time :.10f}', func.__name__

    return f


@timing
def dict_filling(my):  # O(n) - линейная
    my_dict = {}  # O(1) - константная
    for m, x in enumerate(my):  # O(n) - линейная
        my_dict[x] = m if x not in my_dict.keys() else m + 1  # O(1) - константная
    return my_dict


@timing
def list_filling(my):  # O(n) - линейная
    my_list = []  # O(1) - константная в данном случае, а вообще O(n) - зависит от длины аргумента
    for m in my:  # O(n) - линейная
        my_list.append(m)  # O(1) - константная
    return my_list


# в моем случае вывод данных из листа выполняется быстрее, несмотря на нотацию. Вероятно, на больших данных картина
# будет совсем другой


@timing
def dict_take(my):  # O(n) - линейная
    s = dict_filling(my)  # O(n) - линейная
    for i in my:  # O(n) - линейная
        print(f'{i} - {s[0][i]}', end=' ')  # O(1) - константная


@timing
def list_take(my):  # O(n*2 ) - Квадратичная, так как list.index вложен в цикл
    s = list_filling(my)  # O(n) - линейная
    for i in my:  # O(n) - линейная
        print(f'{i} = {s[0].index(i)}', end=' ')  # O(n) - линейная


# Словарь выполняется чуть быстрее
@timing
def dict_rem(my):  # O(n) - линейная
    s = dict_filling(my)  # O(n) - линейная
    for i in my:  # O(n) - линейная
        s[0].pop(i, 0)
    return s[0]  # O(1) - константная


@timing
def list_rem(my):  # O(n * 2) - Снова квадратичная, так как remove вложен в цикл
    s = list_filling(my)  # O(n) - линейная
    for i in my:  # O(n) - линейная
        s[0].remove(i)  # O(n) - линейная
    return s[0]  # O(1) - константная


if __name__ == '__main__':
    import time

    data = "There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration " \
           "in some form, by injected humour, or randomised words which dont look even slightly believable. If you " \
           "are going to use a passage of Lorem Ipsum, you need to be sure there isnt anything embarrassing hidden in " \
           "the middle of text. All the Lorem Ipsum generators on the Internet tend to repeat predefined chunks as " \
           "necessary, making this the first true generator on the Internet. It uses a dictionary of over 200 Latin " \
           "words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks " \
           "reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, " \
           "or non-characteristic words etc."

    print(dict_filling(''.join(data.split())))
    print(list_filling(''.join(data.split())))
    print(dict_take(''.join(data.split())))
    print(list_take(''.join(data.split())))
    print(dict_rem(''.join(data.split())))
    print(list_rem(''.join(data.split())))
