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

"""Первый вариант. Сложность О(n**n)"""
def maximum1(companies_list):
    new_list = []
    for i in range(3):
        income = 0
        for i in companies_list.values():
            if i in new_list:
                continue
            if i > income:
                income = i
        new_list.append(income)
    return new_list



"""Второй вариант. Сложность О(nlogn)"""
def maximum2(companies_list):
    new_list = []
    for i in companies_list.values():
        new_list.append(i)
    new_list.sort()
    new_list.reverse()

    return new_list[:3]



print(maximum1(companies))
print(maximum2(companies))


""" По сложности быстрее будет работать функция maximum1()
По таблице она лучше, нежели функция maximum2(), которая сложнее первой """