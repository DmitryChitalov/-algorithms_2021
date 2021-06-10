from timeit import timeit


def func_1(nums):              # общая сложность - O(N)
    new_arr = []               # O(1)
    for i in range(len(nums)): # O(N) + O(1)
        if nums[i] % 2 == 0:   # O(1)
            new_arr.append(i)  # O(1)
    return new_arr             # O(1)


def func_2(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


my_list = [i for i in range(1000)]


print(f'Time for func_1 is {timeit("func_1(my_list)", globals=globals())} seconds')
print(f'Time for func_2 is {timeit("func_2(my_list)", globals=globals())} seconds')


'''
Time for func_1 is 181.1782283 seconds
Time for func_2 is 144.33410880000002 seconds 

Вывод: при малом числе элементов списка разница между двумя решениями почти не заметна. Но уже при len(nums) == 1000
видно, что list comprehension работает на 25% быстрее. Дополнительный аргумент в пользу этого решения - код становится
меньше в объеме, более лаконичным и читаемым. 
'''
