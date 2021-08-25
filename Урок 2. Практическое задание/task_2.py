"""
2.	Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры
(4, 6 и 0) и 2 нечетные (3 и 5).

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
и смотреть является ли она четной или нечетной. При этом увеличиваем соответствующий счетчик
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все числа извлечены

Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""
# операции % - взятие остатка от деления
#		 и // - целая часть
def input_digit():
    try:
        number = abs(int(input("Введите число: ")))
    except ValueError:
        return input_digit()
    return number

def count_num_recursion_3(number, count_even=0, count_odd=0):
	if number == 0:
		return count_even, count_odd
	else:
		if number % 2 == 0:
			count_even += 1
		else:
			count_odd += 1
		return count_num_recursion_3(number//10, count_even, count_odd)


number_inp = input_digit()
print("Количество четных и нечетных цифр в числе равно:", count_num_recursion_3(number_inp))


def count_num_for_cycle(number):
	# решение через цикл (просто для себя оставила)
	count_even, count_odd = 0, 0
	# print("number", number)
	while number != 0:
		num = number % 2
		# print("num", num)
		if num == 0:
			count_even += 1
			# print("count_even", count_even)
		else:
			count_odd += 1
		number = number // 10
	return count_even, count_odd
# print(count_num_for_cycle(number_inp))
# print(99003%10 )
