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


def stupped_recursion_decision():

    def num_counter_recursion(number: int) -> dict:
        counter = {"odd": 0, "even": 0}
        if number == 0:
            return counter
        if (number % 10) % 2 == 0:
            counter['even'] += 1
        else:
            counter['odd'] += 1
        next_dig = num_counter_recursion(number//10)
        counter['even'] += next_dig['even']
        counter['odd'] += next_dig['odd']
        return counter

    num = input("Введите число (0 for exit): ")
    if num.isdigit():
        if num == '0':
            return
        print(num_counter_recursion(int(num)))
    else:
        print("Мне нужно натуральное число!")

    stupped_recursion_decision()


if __name__ == '__main__':
    stupped_recursion_decision()
