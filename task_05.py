str_a = input('Введите первый символ: ')
str_b = input('Введите второй символ: ')

place_str_a = ord(str_a) - 96
place_str_b = ord(str_b) - 96
count_symbol = abs((ord(str_b) - ord(str_a))) - 1

print(f'Символ "{str_a}" находится на {place_str_a} месте алфавита, символ "{str_b}" - на {place_str_b} месте. '
      f'Между ними {count_symbol} символа')
