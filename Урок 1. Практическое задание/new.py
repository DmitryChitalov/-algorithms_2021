def min_val_check(lst):
    for i in range(len(lst)):     # O(n)
        min_value = lst[i]        # O(1)
        check_lst = lst[i + 1:]   # O(n)
        for val in check_lst:     # O(n)
            if val < min_value:   # O(n)
                min_value = val   # O(1)
        return min_value          # O(1)


print(min_val_check([234, 754, 146, 954, 432]))