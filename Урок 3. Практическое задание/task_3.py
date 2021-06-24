
str_user = input('Введите строку, состоящую только из маленьких латинских букв: ')
print(f"Строка {str_user} имеет длину {len(str_user)} символов.")

sum_substring = set()
for i in range(len(str_user)):
    for j in range(len(str_user), i, -1):
        sum_substring.add(hash(str_user[i:j]))
print(f'{len(sum_substring) -1} различных подстрок в строке {str_user}')
