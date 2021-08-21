from collections import Counter

dict_firms = {}
dict_firms.update({
    'Apple': 300.3,
    'Microsoft': 120.1,
    'DELL': 57.7,
    'NEC': 100.2,
    'Samsung': 450.9,
    'LG': 310.6,
    'Yamaha': 75.0
}) 



"""
1-й вариант решения
"""
print(dict(Counter(firms).most_common(3)))
# Counter(firms).most_common(3)  - O(N log N)
# => O(N log N)




"""
2-й вариант решения
"""
max_income1 = (None, 0)
max_income2 = (None, 0)
max_income3 = (None, 0)

for curr_firm in dict_firms:  #O(N)
    if dict_firms[curr_firm] > max_income1[1]:
        max_income3 = max_income2
        max_income2 = max_income1
        max_income1 = curr_firm, dict_firms[curr_firm]
    elif dict_firms[curr_firm] > max_income2[1]:
        max_income3 = max_income2
        max_income2 = curr_firm, dict_firms[curr_firm]
    elif dict_firms[curr_firm] > max_income3[1]:
        max_income3 = curr_firm, dict_firms[curr_firm]

print(max_income1)
print(max_income2)
print(max_income3)
# => O(N)

# 2-е решение эфективнее первого т.к. во 2-м идет линейный перебор значений во всем словаре. В итоге сложность O(N)
# В первом же варианте функция Counter().most_common() имеет сложность O(N log N) из-за того, что внутри ее используется сортировка, а сортировка имеет сложность O(N log N), следовательно ее сложность - O(N log N).
