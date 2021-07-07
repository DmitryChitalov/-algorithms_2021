s = "papa"

def create_sub_list(s):
    l = []
    for i in range(len(s) + 1):
        for j in range(len(s)):
            t = s[j:i]
            if t != '':
                l.append(t)
    return l
def create_sub_dict(l):
    h = dict()
    for i in range(len(l)):
        if l[i].__hash__() in h:
            pass
        else:
            h.update({l[i]: l[i].__hash__()})
    del h[s]
    return h

l = create_sub_list(s)
h = create_sub_dict(l)

for i in range(len(h)):
    print(list(h.keys())[i])