"""
Задание 2.

"""
import random


def minimum_list_value_1(check_list):
    """Функция осуществляет поиск минимального значения для списка.

        Алгоритм 1:
        Проходимся по списку и сравниваем каждое число со всеми
        другими элементами списка.

        Сложность: O(N**2)
        """
    min_elem = check_list[0]                        # O(1)
    for i in range(len(check_list)):                # O(N)
        for j in range(len(check_list)):            # O(N)
            if check_list[i] < check_list[j]:       # O(1)
                if check_list[i] < min_elem:        # O(1)
                    min_elem = check_list[i]        # O(1)
    return min_elem                                 # O(1)


def minimum_list_value_2(check_list):
    """Функция осуществляет поиск минимального значения для списка.

        Алгоритм 2:
        Проходимся по списку и сравниваем каждое число с найденным раннее минимальным значением.

        Сложность: O(N)
        """
    min_elem = check_list[0]    # O(1)
    for elem in check_list:       # O(N)
        if min_elem > elem:       # O(1)
            min_elem = elem       # O(1)
    return min_elem             # O(1)


my_list = [random.randint(1, 1000) for i in range(20)]
print(my_list)

print(minimum_list_value_1(my_list))
print(minimum_list_value_2(my_list))
