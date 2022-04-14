"""
Задание 1.
Реализуйте свои пользовательские функции, в которых реализуйте:
a) заполнение списка и словаря,
   сделайте замеры и сделайте выводы, что выполняется быстрее и почему
b) выполните набор операций и со списком, и со словарем,
   сделайте замеры и сделайте выводы, что и где выполняется быстрее и почему
Подсказка: для замеров воспользуйтесь модулем time (см. примеры урока 1)
Примечание: eсли вы уже знаете, что такое декоратор и как его реализовать,
то реализуйте ф-цию-декоратор для подсчета времени работы ваших пользовательских функций
И примените ее к своим функциям!
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.
"""

from time import time

new_random_list = []
new_random_number = 1000
some_dictionary = {}

def decorator_time(myfunc):
    def wrapper_time(*args, **kwargs):
        start = time()
        result = myfunc(*args, **kwargs)
        end = time()
        print(f'Время выполенения функции {myfunc.__name__} '
              f'{end - start}')
        return result

    return wrapper_time()


@decorator_time
def fill_list_1(newlst, number_elements):
    # Заполнение через append
    for i in range(number_elements):
        newlst.append(i)  # Сложность операции константная, вставка в конец списка


fill_list_1(new_random_list, new_random_number)

@decorator_time
def fill_list_2(newlst, number_elements):
     # Заполнение через insert
    for i in range(number_elements):
        newlst.insert(0, i)  # Сложность операции O(n), вставка в список

fill_list_2(new_random_list, new_random_number)


@decorator_time
def fill_dictionary(new_dict, number_elements):
    # произвольное заполнение словаря
    for i in range(number_elements):  # сложность константная О(1).
        new_dict[i] = i


fill_dictionary(some_dictionary, new_random_number)

another_dictionary = {}
another_number = 1234

fill_dictionary(another_dictionary, another_number)
#еще проверка обновления словаря

start = time()
some_dictionary.update(another_dictionary)
end = time()
print(f'Время выполенения метода update' 
      f'{end - start}')


