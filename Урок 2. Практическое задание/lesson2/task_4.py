"""
Подсчёт суммы элементов числового ряда.
"""


def get_number_series(input_number, element_value=1, sum_elements=0):

    if input_number == 0:
        return sum_elements
    else:
        # print(element_value)
        sum_elements += element_value
        element_value *= -0.5
        input_number -= 1
        return get_number_series(input_number, element_value, sum_elements)


number = int(input("Введите количество элементов: \n"))
print(f"Вы ввели: {number}\n")
print(get_number_series(number))
