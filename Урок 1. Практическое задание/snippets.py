# sort dict by values
key2 = max(dic, key=lambda k: dic[k])
print("The key with the largest value:", key2)


# sort dict by values
def by_value(item):
   return item[1]
for k, v in sorted(dic.items(), key=by_value):