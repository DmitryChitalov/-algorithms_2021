# Общая сложность О(n^2)
def min_search2(new_list):
    for a in new_list:  # O(n)
        min_number = True  # O(1)
        for b in new_list:  # O(n)
            if a > b:  # O(1)
                min_number = False  # O(1)
        if min_number:  # O(1)
            return a  # O(1)


# Общая сложность O(n)
def min_search(list):
    min_number = list[0]  # O(1)
    for i in range(1, len(list)):  # O(n)
        if min_number > list[i]:  # O(1)
            min_number = list[i]  # O(1)
    return min_number  # O(1)


my_list = (4, 5, 66, 14, 12, 18, 2)
print(min_search(my_list))
print(min_search2(my_list))
