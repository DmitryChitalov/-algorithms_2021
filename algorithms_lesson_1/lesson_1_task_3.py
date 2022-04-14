comp_dict = {'company_1': 80, 'company_2': 10,
             'company_3': 40, 'company_4': 20}
# РЕШЕНИЕ 1:
# сложность N log N

sorted_dict = sorted(comp_dict.items(), key=lambda kv: kv[1], reverse=True)[:3] # N log N
for key, val in sorted_dict: # O(1), т.к. число итераций цикла заранее известно [:3]
    print(key,':',val)		 # O(1) 

print()

# РЕШЕНИЕ 2:
sort_dict = {}                                              # O(N)
val_list = sorted(comp_dict.values(), reverse=True)[:3]     # N log N
for key, val in comp_dict.items():                          # O(N)
    if val in val_list:                                     # O(N)
        sort_dict[key] = comp_dict[key]                     # O(1)

res_dict = (sorted(sort_dict.items(), key=lambda kv: kv[1], reverse=True)) # N log N
for key, val in res_dict:                                                  # O(N)
    print(key, ':', val)                                                   # O(1)

# Итого, сложность N log N


#РЕШЕНИЕ 3: 
result_max = {}
list_d = dict(comp_dict)
for i in range(3):
    maximum = max(list_d.items(), key=lambda kv: kv[1])  # O(N) - доминанта 
    del list_d[maximum[0]]
    result_max[maximum[0]] = maximum[1]
for key, val in result_max.items():						 # O(N)
    print(key,':',val)

# Итого, сложность O(N) 

# Вывод: решение 2 по сложности равнозначно решению 1, 
# но явл. более громоздким. Третье решение оптимальное, 
# т.к. у него наименьшая сложность за счет отсутствия функции sorted 
