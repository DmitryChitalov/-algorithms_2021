import hashlib

s = []
n = 'lala'
itog = 0
for i in range(len(n)):
    for j in range(i + 1, len(n) + 1):
        if n[i:j] != n:
            s.append(hashlib.sha256(n[i:j].encode()).hexdigest())
            print(n[i:j], end=' ')
print(n)

s2 = []
for x in s:
    if x not in s2:
        s2.append(x)

print(len(s2))
