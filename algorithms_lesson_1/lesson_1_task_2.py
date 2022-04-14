# N^2 - decision  1*N*(N + 1 + 1) + 1 + 1 == N^2

def find_min_long(check_list):
    for i in check_list:            #O(N)
        is_min = True               #O(1)
        for k in check_list:        #O(N)
            if i > k:               #O(1)
                is_min = False      #O(1)
        if is_min:                  #O(1)
            return i                #O(1)


# O(N) - decision 1 + 1 + N + 1 + 1 + 1 == O(N)
def find_min_short(check_list):
    min_val = check_list[0]         #O(1) + O(1)
    for el in check_list:           #O(N)
        if el < min_val:            #O(1)
            min_val = el            #O(1)
    return min_val                  #O(1)


my_list = [2, 7, 4, 10, 23]
print(find_min_long(my_list))
print(find_min_short(my_list)) 
