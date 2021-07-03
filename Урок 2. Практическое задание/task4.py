n = 1
i = 0
sum = 0
a = 1
def recursion(n):
    global a,sum,i
    if i == n:
        print(sum)
    else:
        sum += a
        a = (-1) * a / 2
        recursion(n-1)

recursion(n)