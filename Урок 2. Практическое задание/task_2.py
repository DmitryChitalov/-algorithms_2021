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

counts = {"even_numbers_count": 0,
          "odd_numbers_count": 0}


def my_func(num, res_list):
    def fill_res_list(list_for_fill, num_for_check):
        if num_for_check % 2 == 0:
            list_for_fill['even_numbers_count'] = list_for_fill.get('even_numbers_count') + 1
        else:
            list_for_fill['odd_numbers_count'] = list_for_fill.get('odd_numbers_count') + 1

    remainder = num % 10
    whole_part = num // 10
    if whole_part == 0:
        fill_res_list(res_list, remainder)
        return res_list
    else:
        fill_res_list(res_list, remainder)
        return my_func(whole_part, res_list)


print(my_func(1210132222, counts))
