# Сложность О(n)
def compare(my_numbers):
    min_number = my_numbers[0]
    for number in my_numbers:
        if number < min_number:
            min_number = number
    return min_number

# Сложность О(n^2)
def compare_difficult(my_numbers):
    min_number = 0
    for i in my_numbers:
        for j in my_numbers:
            if i <= j:
                min_number = i
    return min_number


my_list = [5, 15, 45, 13, 100, 32, 65, 3]

print(compare(my_list))
print(compare_difficult(my_list))
