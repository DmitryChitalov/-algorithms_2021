
companies = {
    'Роснефть': 708,
    'Газпром': 1203,
    'Лукойл': 640,
    'Сбербанк России': 845,
    'Российские железные дороги': 156,
    'Ростех': 179
}
### Способ 1 #O^2
companis_list = list(companies.items())
values_list = list(companies.values())
for i in range(len(values_list) - 1):
  firstTree = 0
  for j in range(len(values_list) - 1): 
    if (values_list[i] < values_list[j]): # я посчитал сколько раз i элемент меньше остальных, если он меньше остальных 0 раз, то он самый большой, получается кто набрал 0,1,2 тот в ТОП 3
      firstTree += 1
  if(firstTree < 3):
    print(companis_list[i])

### Способ 2 # O(N)
companis_list = list(companies.items())
keys_list = list(companies.keys())
revers_companies={}
for i in range(len(values_list) - 1):             # O(N)
  revers_companies[values_list[i]] = keys_list[i] # поменяем местами keys и values
keys_companies = sorted(revers_companies, reverse=True)[:3] #O(NlogN)
for company in keys_companies:                    # O(N)
  print(revers_companies[company])
  