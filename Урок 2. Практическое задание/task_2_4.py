#*************************************************************************
def summa_elementov(numb, i=1):
    if numb > 0:
        yield i
        yield from summa_elementov(numb - 1, -i / 2)

num_element = float(input('Введите количество элементов: '))
result = list(summa_elementov(num_element))
print(*result)
print(f'Сумма всех улементов =  {sum(result)}')

#*************************************************************************