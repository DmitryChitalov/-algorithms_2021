companies = {"company_1": 56,
             "company_2": 856,
             "company_3": 560,
             "company_4": 7600,
             "company_5": 1560,
             "company_6": 2600,
             "company_7": 10560,
             "company_8": 11560,
             "company_9": 956,
             }


def top_3_shops(source):
    """
    Сложность O(n log n)
    Данный способ предпочтительнее, чем второй(квадратичный)
    """
    list_company = list(source.items())
    list_company.sort(key=lambda i: i[1], reverse=True)
    return list_company[:3]


print(top_3_shops(companies))


def second_top_3_shops(source):
    """
    Сложность O(n^2)
    """
    sorted_values = sorted(source.values(), reverse=True)
    result = []
    for i in sorted_values:
        for s in source.keys():
            if source[s] == i:
                result.append(s)
    return result[:3]


print(second_top_3_shops(companies))
