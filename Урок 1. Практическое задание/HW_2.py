alist = [5, 2, 6, 9, 4, 9, 4, 7, 2, 6, 15]


def min_num_1():  # O(n)
    num = alist[0]  # O(1)
    for el in alist:  # O(n)
        if num > el:  # O(1)
            num = el  # O(1)
    return num  # O(1)


def min_num_2():  # O(n^2)
    num = alist[0]
    for el in range(len(alist) - 1):
        for ell in alist:
            if ell < alist[el]:
                num = ell
    return num


print(min_num_1())
print(min_num_2())
