"""
Нахождение минимального значения 2-мя способами.
"""

ls_initial = [110, 3, 5, 10, 6, 22, 111, 3, 33, 85, 3, 110, 3, 5, 10, 6, 22, 111, 3, 33, 85, 3]


# O(N^2)
def minimum(ls_input):
    mini = ls_input[0]
    for i in ls_input[0:]:  #O(N) * O(N)
        if i < mini:
            mini = i

    return mini


print(minimum(ls_initial))


# O(N)
def minimum2(ls_input):
    mini = ls_input[0]
    i = 1
    for i in range(len(ls_input) - 1): #O(N) * O(1)
        if mini > ls_input[i]:
            mini = ls_input[i]

    return mini


print(minimum2(ls_initial))
