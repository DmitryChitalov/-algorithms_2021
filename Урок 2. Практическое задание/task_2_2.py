# Вариант 1
my_list = 2345601
result = []
result_old = []
def number_cout(my_lst):
    result_str = map(int, str(my_lst))
    for nums in result_str:
        if nums % 2 == 0:
            result.append(nums)
        else:
            result_old.append(nums)
    print(f'Список четных чисел  = {result}')
    print(f'Список НЕ четных чисел  = {result_old}')

# number_cout(my_list)


# Вариант 2
lv_result = 0
old_result = 0
def number_cout2(my_lst):

    if my_lst == 0:
        exit()

    lv_result = my_lst % 10
    if lv_result % 2 == 0:
        lv_result = lv_result
        my_lst = my_lst // 10
        number_cout2(my_lst)
    else:
        old_result = lv_result
        my_lst = my_lst // 10
        number_cout2(my_lst)


number_cout2(my_list)