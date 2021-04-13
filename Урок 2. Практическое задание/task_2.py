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


def get_digit_number(number, position):
    position_pow = pow(10, position)
    return (number % (position_pow * 10) - number % position_pow) // position_pow


def count_evens_and_odds(number, number_decreaser=0, position=0, result=None):
    # Базовый случай
    if number_decreaser < 0:
        return result
    elif position == 0:
        number_decreaser = number
        result = [0, 0]
    number_decreaser = number_decreaser - pow(10, position) * 9
    digit = get_digit_number(number, position)
    result_position = digit % 2
    result[result_position] = result[result_position] + 1
    position += 1
    # Шаг рекурсии
    return count_evens_and_odds(number, number_decreaser, position, result)


test_cases = [
    {
        'props': 111112,
        'result': [1, 5],
    },
    {
        'props': 123456789,
        'result': [4, 5],
    },
    {
        'props': 0,
        'result': [1, 0],
    },
    {
        'props': 1,
        'result': [0, 1],
    },
    {
        'props': 2244661,
        'result': [6, 1],
    }
]

passed_tests = 0
for test_case in test_cases:
    props = test_case["props"]
    expected_result = test_case["result"]
    real_result = count_evens_and_odds(props)
    is_ok = real_result == expected_result
    if is_ok:
        passed_tests += 1
    print(f'{is_ok} count_evens_and_odds({props}) => {real_result}')
print(f'passed tests: {passed_tests}/{len(test_cases)}\n')
