def true_false(n):
    if n == 1:
        return n
    else:
        return n + true_false(n-1)


digit = 6 * (6 + 1) / 2
print(true_false(6) == digit)
