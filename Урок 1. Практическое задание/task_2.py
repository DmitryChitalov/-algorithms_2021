test_list = [5, 1, 10, 3, 9]


def min_search(lst):
    """
    Сложность O(n^2)
    """
    for i in lst:
        min_value = True
        for s in lst:
            if i > s:
                min_value = False
        if min_value:
            return i


def second_min_search(lst):
    """
    Сложность O(n)
    """
    min_value = test_list[0]
    for item in lst:
        if item <= min_value:
            min_value = item
    return min_value


if __name__ == '__main__':
    print(second_min_search(test_list))
    print(min_search(test_list))
