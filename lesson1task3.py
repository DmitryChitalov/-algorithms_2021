companies_earnings = {
    'apple': 50000000,
    'google': 60000000,
    'twitter': 45000000,
    'instagram': 70000000
}

#решение 1, O(n log n)
def highest_income (new_dict):
    x = sorted(new_dict, key= new_dict.get, reverse=True)
    return x[0],x[1],x[2]

print(highest_income(companies_earnings))

#решение 2, O n
def highest_income_1 (my_list):
    highest_inc = {}
    list_d = my_list
    for i in range(3):
        maximum = max(list_d.items(), key= lambda k_v : k_v[1])
        del list_d[maximum[0]]
        highest_inc[maximum[0]] = maximum[1]
    return highest_inc

print(highest_income_1(companies_earnings))


#второе решение эффективнее так как оно быстрее
#и при работе с большим количеством данных будет работать лучше
