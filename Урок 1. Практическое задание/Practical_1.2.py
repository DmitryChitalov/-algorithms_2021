def find_min(lst):
    """ Difficult: O(n^2)"""

    for i in lst:  # O(n)
        my_bool = False
        for j in lst:  # O(n)
            if i < j:  # O(1)
                my_bool = True
            else:
                my_bool = False
        if my_bool:
            return i


lst = [11, 55, 32, 4, 7]
print(find_min(lst))

###################################################################################

def find_min_2(el):
    """Difficult: O(n) """
    param = el[0]
    for i in el:  # O(1)
        if param > i:  # O(1)
            param = i
    return param


lst = [31, 52, 25 , 78]
print(find_min_2(lst))