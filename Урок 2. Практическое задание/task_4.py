"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.

Пример:
Введите количество элементов: 3
Количество элементов: 3, их сумма: 0.75

Подсказка:
Каждый очередной элемент в 2 раза меньше предыдущего и имеет противоположный знак

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""

def double_decrease_with_alternating_sign(counter, number=1, sum=1):
    # Базовый случай
    if counter <= 1:
        return sum
    number = - number / 2
    sum += number
    counter -= 1
    # Шаг рекурсии
    return double_decrease_with_alternating_sign(counter, number, sum)


test_cases = [
    {
        'props': 0,
        'result': 1,
    },
    {
        'props': 1,
        'result': 1,
    },
    {
        'props': 2,
        'result': 0.5,
    },
    {
        'props': 3,
        'result': 0.75,
    },
    {
        'props': 5,
        'result': 0.6875,
    },
]

passed_tests = 0
for test_case in test_cases:
    props = test_case["props"]
    expected_result = test_case["result"]
    real_result = double_decrease_with_alternating_sign(props)
    is_ok = real_result == expected_result
    if is_ok:
        passed_tests += 1
    print(f'{is_ok} double_decrease_with_alternating_sign({props}) => {real_result}{(f", but {expected_result} expected", "")[is_ok]}')
print(f'passed tests: {passed_tests}/{len(test_cases)}\n')
