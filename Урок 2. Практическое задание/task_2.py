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

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7

Пример:
Введите число: 123
Количество четных и нечетных цифр в числе равно: (1, 2)
"""
from operator import add


"""
Функция возвращает массив, в котором перывый элемент - число четных цифр в записи числа,
а второй элемент - число нечетных цифр в записи числа
"""
def get_digit_stats(number,inprogress_result = [0,0]): # inprogress_result is an array for iteration's result (# of evens, # of odds)
    incoming_number = number
    if len(incoming_number) == 1:
        incoming_number = int(incoming_number)
        if incoming_number%2 == 0:
            return [1,0]
        else:
            return [0,1]
    else:
        current_number = int(incoming_number)%10
        incoming_number = int(incoming_number)//10
        if current_number%2 == 0:
            will_return = [1,0] # even
        else:
            will_return = [0,1] # odd
        return list(map(add, will_return, get_digit_stats(str(incoming_number))))
            

string_to_process = input("Input number: ")
print(get_digit_stats(string_to_process))