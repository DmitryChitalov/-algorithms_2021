def recursion(n):
    sum = n
    if n == 0:
        return n
    else:
        sum += recursion(n-1)
        return sum

def is_equal(n):
    return recursion(n) == n * (n+1) / 2

#example
for i in range(15):
    print(is_equal(i))