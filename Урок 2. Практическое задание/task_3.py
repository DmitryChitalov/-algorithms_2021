"""
3.	Сформировать из введенного числа обратное по порядку входящих в него
цифр и вывести на экран. Например, если введено число 3486,
 то надо вывести число 6843.

Подсказка:
На каждом шаге вам нужно 'доставать' из числа очередную цифру
Пока все числа не извлечены рекурсивные вызовы продолжаем
Условие завершения рекурсии - все цифры извлечены

Используем операции % //, НЕ ИСПОЛЬЗУЕМ ОПЕРАЦИИ ВЗЯТИЯ ЭЛЕМЕНТА ПО ИНДЕКСУ

Пример:
Введите число, которое требуется перевернуть: 123
Перевернутое число: 321

Не забудьте проверить и на числах, заканчивающихся нулем.
Пример:
Введите число, которое требуется перевернуть: 1230
Перевернутое число: 0321

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def get_digit_number(number, position):
    position_pow = pow(10, position)
    return (number % (position_pow * 10) - number % position_pow) // position_pow


def revert_number(number, number_decreaser=0, position=0, result=None):
    # Базовый случай
    if number_decreaser < 0:
        return result
    elif position == 0:
        number_decreaser = number
        result = ''
    number_decreaser = number_decreaser - pow(10, position) * 9
    digit = get_digit_number(number, position)
    result = f'{result}{digit}'
    position += 1
    # Шаг рекурсии
    return revert_number(number, number_decreaser, position, result)


test_cases = [
    {
        'props': 123,
        'result': '321',
    },
    {
        'props': 1230,
        'result': '0321',
    },
    {
        'props': 0,
        'result': '0',
    },
    {
        'props': 11223344,
        'result': '44332211',
    }
]

passed_tests = 0
for test_case in test_cases:
    props = test_case["props"]
    expected_result = test_case["result"]
    real_result = revert_number(props)
    is_ok = real_result == expected_result
    if is_ok:
        passed_tests += 1
    print(f'{is_ok} revert_number({props}) => {real_result}{(f", but {expected_result} expected", "")[is_ok]}')
print(f'passed tests: {passed_tests}/{len(test_cases)}\n')
