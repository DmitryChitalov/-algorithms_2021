import random
int_num_a = int(input('Введите нижнюю границу диапазона int: '))
int_num_b = int(input('Введите верхнюю границу диапазона int: '))

float_num_a = int(input('Введите нижнюю границу диапазона float: '))
float_num_b = int(input('Введите верхнюю границу диапазона float: '))

str_a = input('Введите первый символ: ')
str_b = input('Введите второй символ: ')

rand_int_number = random.randint(int_num_a, int_num_b)
rand_float_number = round(random.uniform(float_num_a, float_num_b), 1)
rand_str = chr(random.randint(ord(str_a), ord(str_b)))

print(rand_int_number)
print(rand_float_number)
print(rand_str)
