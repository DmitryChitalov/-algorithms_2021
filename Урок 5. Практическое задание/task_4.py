from collections import OrderedDict
from timeit import timeit


my_dict = {}
my_ordered_dict = OrderedDict()


def fill_dict(target):
    for i in range(100000):
        target[i] = i


def get_element(target):
    for i in range(100000):
        target.get(i)


if __name__ == '__main__':
    print("Замер заполнения словарей...")
    print(f"Dict: {timeit('fill_dict(my_dict)', globals=globals(), number=1000)}")
    print(f"Ordered: {timeit('fill_dict(my_ordered_dict)', globals=globals(), number=1000)}")
    print("Замер получения элементов словарей...")
    print(f"Dict: {timeit('get_element(my_dict)', globals=globals(), number=1000)}")
    print(f"Ordered: {timeit('get_element(my_ordered_dict)', globals=globals(), number=1000)}")

    """
    Вывод:
    
    Замер заполнения словарей...
    Dict: 13.952096822000385
    Ordered: 18.664729992000503
    
    Замер получения элементов словарей...
    Dict: 15.711155884000618
    Ordered: 14.772621052999966
    
    C версии 3.6 и выше обычные словари хранят порядок, что касается замеров, то обычный словарь 
    оказался прилично быстрее при заполнении, что касается получения элементов , то почти
    одинаково работают.
    
    Мое мнение - смысла использовать OrderedDict нет.
    """
