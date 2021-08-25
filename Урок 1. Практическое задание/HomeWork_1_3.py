# 1st O(n log n)

import operator

company_income = {'Matreshka': 100, 'Pepsi': 300, 'Microsoft': 700, 'Gazprom': 50, 'Apple': 800}

sort_company_income = sorted(company_income.items(), key=operator.itemgetter(1), reverse=-1)
top_company = sort_company_income[0:3]

sorted_dict = {company: value for company, value in top_company}

print(sorted_dict)

# 2nd O(n^2)

sorted_values = sorted(company_income.values(), reverse=-1)
top_company_1 = sorted_values[0:3]
sorted_dict_1 = {}

for i in top_company_1:
    for c in company_income.keys():
        if company_income[c] == i:
            sorted_dict_1[c] = company_income[c]
            break
print(sorted_dict_1)
