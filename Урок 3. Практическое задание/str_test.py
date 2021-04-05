import time

dct = dict()
dct = {i:i for i in range(10000000)}
dct_time = 0
lst = list()
lst = [i for i in range(10000000) ]
lst_time = 0


for i in range(1):
    st = time.time()
    dct[i]
    et = time.time()
    dct_time += et - st

print(f"dict read time: {dct_time:0.8f}")

for i in range(10000000):
    st = time.time()
    lst[i]
    et = time.time()
    lst_time += et - st

print(f"list read time: {lst_time:0.8f}")

    