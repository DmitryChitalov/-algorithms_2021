## Везде выводим данные Компания и ее прибыль
## Предпочтительнее выглядит вариант 3, меньше код
## Первый метод с помощью двух функций - сложность O(n**2) за счет вызова из цикла со сложностью O(n)
## функции с циклом сложности O(n)
def max_ebitda_11(ebitda):
    max_ebitda = 0
    max_name = ''
    for key, value in ebitda.items():
        if max_ebitda < value:
             max_ebitda = value
             max_name = key
    return max_name

def max_ebitda_1(ebitda_dict):
    company_dict = {}
    ebitda_dict_1 = ebitda_dict.copy()
    for i in range (3):
        m = max_ebitda_11(ebitda_dict_1)
        company_dict[i]= {m, ebitda_dict_1.get(m)}
        del ebitda_dict_1[m]
    return company_dict

## 2 и 3 методы с помощью сортировок, сложность обоих O(n log n) за счет сортировок
def max_ebitda_2(ebitda_dict):
    company_lst = []
    for key, value in ebitda_dict.items():
        company_lst.append((value,key))
    company_lst.sort(reverse = True)
    return company_lst[:3]


def max_ebitda_3(ebitda_dict):
    company_lst = sorted(ebitda_dict.items(), key=lambda x: x[1], reverse=True)[:3]
    return company_lst

## Входные данные и вызов функций
ebitda_dict = {
    'Yandex' : 200,
    'Google' : 150,
    'Facebook' : 600,
    'Instagram' : 300,
    'Telegram' : 100,
    'AT&T' : 800,
    'Orange' : 950,
    'Vodafone' : 350
        }

print(max_ebitda_1(ebitda_dict))
print(max_ebitda_2(ebitda_dict))
print(max_ebitda_3(ebitda_dict))