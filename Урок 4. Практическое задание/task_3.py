"""
Задание 3.

Приведен код, формирующий из введенного числа
обратное по порядку входящих в него
цифр и вывести на экран.

Сделайте профилировку каждого алгоритма через cProfile и через timeit

Обязательно предложите еще свой вариант решения и также запрофилируйте!

Сделайте вывод, какая из четырех реализаций эффективнее и почему!!!

Без аналитики задание считается не принятым
"""


import timeit
import cProfile


def revers_1(enter_num, revers_num=0):
    if enter_num == 0:
        return revers_num
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        return revers_1(enter_num, revers_num)


def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return revers_num


def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


# Взял свой же алгоритм из второго задания
def revers_4(enter_num, result):
    this_number = enter_num % 10

    result = f'{result}{this_number}'

    if len(str(enter_num)) > 1:
        next_numbers = enter_num // 10
        return revers_4(next_numbers, result)

    return result


# Алгоритм, предложенный гуглом
def revers_5(enter_num):
    return ''.join(reversed(str(enter_num)))


numbers = 1234567890123456789012345678901234567890123456789012345678901234567890123456789012345678901234567890123456789
# numbers = 1234567890
empty_str = ''

print(f'Проверка TimeIt:\n'
      f'1. reverse_1: {timeit.timeit("revers_1(numbers)", globals=globals())}\n'
      f'2. reverse_2: {timeit.timeit("revers_2(numbers)", globals=globals())}\n'
      f'3. reverse_3: {timeit.timeit("revers_3(numbers)", globals=globals())}\n'
      f'4. reverse_4: {timeit.timeit("revers_4(numbers, empty_str)", globals=globals())}\n'
      f'5. reverse_5: {timeit.timeit("revers_5(numbers)", globals=globals())}\n')

cProfile.run('revers_1(numbers)')
cProfile.run('revers_2(numbers)')
cProfile.run('revers_3(numbers)')
cProfile.run('revers_4(numbers, empty_str)')
cProfile.run('revers_5(numbers)')

"""
Вывод:
Самыми эффективной оказалась вторая функция. Не зависимо от объема данных, она всегда выполняется менее,чем за
секунду. Обусловлено это тем, что сложность алгоритма константная. Исходя из данных профилирования, следует, что она так
же, как и вторая функция, задействует всего 4 штатные функции. Но вторая медленнее, потому что алгоритм является линейным.
Так же хорошо, на большом объеме данных, показывает себя пятая функция. При 109 символах, среднее время выполнения 1, 2
функции составляет ~30 секунд, третья справляется за 0.7 сек, пятая за 2.4, а вот 4 за 70 секунд, т.к. рекурсия + 221 
вызов стандартных функций
"""