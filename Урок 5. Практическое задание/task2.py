from collections import deque

def sum(x, y):
    TABLE = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    t = 0

    if len(y) > len(x):
        x, y = deque(y), deque(x)
    else:
        x, y = deque(x), deque(y)

    while x:
        if y:
            res = TABLE[x.pop()] + TABLE[y.pop()] + t
        else:
            res = TABLE[x.pop()] + t
        t = 0
        if res < 16:
            result.appendleft(TABLE[res])
        else:
            result.appendleft(TABLE[res - 16])
            t = 1
    if t:
        result.appendleft('1')
    return list(result)


def mult(x, y):
    TABLE = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
               'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
               0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
               10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    result = deque()
    sm = deque([deque() for _ in range(len(y))])
    x, y = x.copy(), deque(y)

    for i in range(len(y)):
        m = TABLE[y.pop()]
        for j in range(len(x) - 1, -1, -1):
            sm[i].appendleft(m * TABLE[x[j]])
        for _ in range(i):
            sm[i].append(0)

    t = 0

    for _ in range(len(sm[-1])):
        res = t

        for i in range(len(sm)):
            if sm[i]:
                res += sm[i].pop()

        if res < 16:
            result.appendleft(TABLE[res])
        else:
            result.appendleft(TABLE[res % 16])
            t = res // 16
    if t:
            result.appendleft(TABLE[t])

    return list(result)


a = list(input('Input first number: '))
b = list(input('Input second number: '))


print(f'Sum : {sum(a, b)}')

print(f'Multiplication : {mult(a, b)}')