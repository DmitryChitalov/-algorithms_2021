import collections

def input_companies():
    global number_of_companies
    number_of_companies = int(input("Input number of companies "))
    global d
    d = collections.defaultdict()
    for i in range(number_of_companies):
        name_of_companies = input("Input name of company ")
        income_for_quarter = input("input 4 numbers ")
        income_for_quarter = list(map(int, income_for_quarter.split(" ")))
        total_income = (sum(income_for_quarter))
        d.update({name_of_companies: total_income})
    return d

def avg_income(dict_of_companies):
    return sum(list(dict_of_companies.values())) / number_of_companies



def analyse(dict_of_companies):
    less = []
    more = []
    for i in list(d.keys()):
        if dict_of_companies[i] < total_avg:
            less.append(i)
        elif dict_of_companies[i] > total_avg:
            more.append(i)
    return f"Higher than avg: {more}\nLower than avg: {less}"

d = input_companies()
total_avg = avg_income(d)
print(f'Total year avg income is {total_avg}')
print(analyse(d))





