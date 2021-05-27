companies = {
    "exxon mobil": 265700,
    "state grid": 387000,
    "volkswagen": 275200,
    "cnpc": 364100,
    "sinopecgroup": 329800,
    "shell":311600,
    "sinopecgroup": 386200,
    "toyota": 280500,
    "bp": 278400,
    "walmart": 524000
}

#1 решение, сложность О(NlogN)
new_list = list(companies.items())
new_list.sort(key=lambda i: i[1])
for i in new_list:
    print(i[0], ':', i[1])


#2 решениеб сложность О(n)
def maximum(list1):
    dict1 = {}
    list1 = dict(list1)
    for i in range(3):
        m = max(list1.items())
        del list1[m[1]]
        dict1[m[0]] = m[1]
    return dict1
print(maximum(companies))


#Эффективней решение 2, так как  оно эвляется более быстрым, в нем не используются длительные вложенные операции