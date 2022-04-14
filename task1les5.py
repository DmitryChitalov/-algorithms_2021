from collections import namedtuple

n = int(input("Введите количество предприятий: "))
companies_tuple = namedtuple('Companies', ['quart1', 'quart2', 'quart3', 'quart4'])
num = 0
result = {}
for i in range(n):
    company = str(i + 1) + "-е предприятие"
    print(f'Введите прибыль за каждый квартал за {company}:')
    q1, q2, q3, q4 = map(int, input().split())
    result[company] = companies_tuple(quart1=q1, quart2=q2, quart3=q3, quart4=q4)

total = ()
print()
for company, prof in result.items():
    print(f'{company} прибыль за год - {sum(prof)}')
    total += prof

average = sum(total) / len(prof)
print(f'Средняя прибыль за год для всех предприятий: {average}')

print()
print('Предприятия, у которых прибыль выше среднего:')
for company, profit in result.items():
    if sum(profit) > average:
        print(f'{company} - {sum(profit)}')

print()
print('Предприятия, у которых прибыль ниже среднего:')
for company, profit in result.items():
    if sum(profit) < average:
        print(f'{company} - {sum(profit)}')