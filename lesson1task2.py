#O(n^2)
def min_n(n):
    for i in n: # O(n)
        min_number = True
        for j in n: #O(n)
            if i > j: #O(1)
                min_number = False
        if min_number: #O(n)
            return i


#O(n)
def min_number(n):
    min_num = n[0]
    for i in n: #O(n)
        if i < min_num: #O(n)
            min_num = i
    return min_num

list1 = [1,2,5,4,0]
print(min_n(list1))
print(min_number(list1))