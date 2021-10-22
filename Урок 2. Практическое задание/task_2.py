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


def count_even_and_odd_digits(number, odd_counter=0, even_counter=0):
    '''
    the function counts the number of odd and even digits

    param number: positive integer 
    param odd_counter: odd digit counter
    param even_counter: even digit counter

    return: a tuple with the first count value of non-even digits,
    and the second position - even
    '''
    if (number % 10) % 2:
        odd_counter += 1
    else:
        even_counter += 1
    if number // 10 == 0: # условия завершение рекурсии
        return odd_counter, even_counter
    return count_even_and_odd_digits(number // 10, odd_counter, even_counter)


number = 112200

print(f'не чётных = {count_even_and_odd_digits(number)[0]}, \
четных = {count_even_and_odd_digits(number)[1]}')


def count(number, odd_counter=0, even_counter=0):
    if (number % 10) % 2:
        odd_counter += 1
    else:
        even_counter += 1
    if len(str(number)) == 1:
        return odd_counter, even_counter
    return count(number // 10, odd_counter, even_counter)

print(count(number))