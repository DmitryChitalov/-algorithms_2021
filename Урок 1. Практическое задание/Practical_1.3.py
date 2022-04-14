data_dict = {'Apple': 55256, 'Microsoft': 39240, 'Alphabet': 34343,
             'Walmart': 14881, 'Pfizer': 16273, 'Saudi Aramco': 88211}


# Difficult: O(n)
def find_max(lst):
    """Difficult: O(n) """
    result_dict = dict()
    for _ in range(3):  # O(1)
        el = max(lst, key=lst.get)  # O(n)
        result_dict[el] = lst[el]  # O(1)
        lst.pop(el)
    return result_dict


print(find_max(data_dict))

#############################################################################################


def find_max_2(dct):
    """ Difficult: O(n^2)
    Это решение менее эффективно, по причине квадратичной сложности
    """
    result_dct = {}
    list_value = list(dct.values())
    for _ in range(3):
        param = 0
        for i in list_value:  # O(n)
            if param < i:
                param = i
        list_value.remove(param)
        for key in dct.keys():  # O(n)
            if dct[key] == param:  # O(1)
                result_dct[key] = dct[key]
    return result_dct


print(find_max_2(data_dict))
