"""
1.
Написать программу, которая будет

складывать, вычитать, умножать или делить два числа.

Числа и знак операции вводятся пользователем.

После выполнениявычисления программа не должна завершаться, а должна запрашивать новые данные
для вычислений.

Завершение программы должно выполняться при вводе символа '0' в качестве знака операции.

Если пользователь вводит неверный знак
(не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и
снова запрашивать знак операции.

Также сообщать пользователю о невозможности деления на ноль,
если он ввел 0 в качестве делителя.
Подсказка:
Вариант исполнения:
- условие рекурсивного вызова - введена операция +, -, *, / - ШАГ РЕКУРСИИ
- условие завершения рекурсии - введена операция 0 - БАЗОВЫЙ СЛУЧАЙ
Пример:
Введите операцию (+, -, *, / или 0 для выхода): +
Введите первое число: 214
Введите второе число: 234
Ваш результат 448
Введите операцию (+, -, *, / или 0 для выхода): -
Введите первое число: вп
Вы вместо трехзначного числа ввели строку (((. Исправьтесь
Введите операцию (+, -, *, / или 0 для выхода):
Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def calc():
    """Рекурсия"""
    operation_type = input("Введите операцию (+, -, *, / или 0 для выхода): ")

    if operation_type == '0': # Базовый случай, т.е. условие завершения рекурсивных вызовов (Ввод НУЛЯ)
        return "Выход"

    else:
        if operation_type in "+-*/":
            try:
                num_1 = int(input("Введите первое число: "))
                num_2 = int(input("Введите второе число: "))

                if operation_type == '+': # Если ввели +
                    res = num_1 + num_2
                    print(f"Ваш результат {res}")
                    return calc() # Возвращаем рез-т операции сложения (запрашиваем новые данные для вычислений)

                elif operation_type == '-': # ЧТО ЕСЛИ предыдущие условие были невернымио, тогда попробуйте это условное
                    res = num_1 - num_2
                    print(f"Ваш результат {res}")
                    return calc()

                elif operation_type == '*':
                    res = num_1 * num_2
                    print(f"Ваш результат {res}")
                    return calc()

                elif operation_type == '/':
                    try:
                        res = num_1 / num_2
                    except ZeroDivisionError:# сообщение пользователю о невозможности деления на ноль
                        print("Деление на 0 невозможно")
                    else:
                        print(f"Ваш результат {res}")
                    finally:
                        return calc()

            except ValueError:
                print("Вы вместо трехзначного числа ввели строку. Исправьтесь")
                return calc()

        else:
            print("Введен неверный символ, попробуйте еще раз")
            return calc()


calc()
