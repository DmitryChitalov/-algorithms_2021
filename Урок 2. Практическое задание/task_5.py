"""
5.	Вывести на экран коды и символы таблицы ASCII, начиная с символа
под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.

Пример:
32 -   33 - ! 34 - " 35 - # 36 - $ 37 - % 38 - & 39 - ' 40 - ( 41 - )
42 - * 43 - + 44 - , 45 - - 46 - . 47 - / 48 - 0 49 - 1 50 - 2 51 - 3
52 - 4 53 - 5 54 - 6 55 - 7 56 - 8 57 - 9 58 - : 59 - ; 60 - < 61 - =
62 - > 63 - ? 64 - @ 65 - A 66 - B 67 - C 68 - D 69 - E 70 - F 71 - G
72 - H 73 - I 74 - J 75 - K 76 - L 77 - M 78 - N 79 - O 80 - P 81 - Q
82 - R 83 - S 84 - T 85 - U 86 - V 87 - W 88 - X 89 - Y 90 - Z 91 - [
92 - \ 93 - ] 94 - ^ 95 - _ 96 - ` 97 - a 98 - b 99 - c 100 - d 101 - e
102 - f 103 - g 104 - h 105 - i 106 - j 107 - k 108 - l 109 - m 110 - n 111 - o
112 - p 113 - q 114 - r 115 - s 116 - t 117 - u 118 - v 119 - w 120 - x 121 - y
122 - z 123 - { 124 - | 125 - } 126 - ~ 127 - 

Подсказка:
Допускается исп-е встроенных ф-ций, в частности, chr()

Решите через рекурсию. Решение через цикл не принимается.
Для оценки Отлично в этом блоке необходимо выполнить 5 заданий из 7
"""


def ascii_show(start_code, end_code):
    """Формирует список из пар 'code - value' ASCII в заданном диапазоне"""
    res_lst = []  # хранилище для накопления результатов

    # базовый случай - дошли до конца диапазона
    if start_code == end_code:
        return [f'{end_code:03d} - {chr(end_code)}']

    # шаг рекурсии - пока не дошли до конца
    res_lst.append(f'{start_code:03d} - {chr(start_code)}')
    res_lst += ascii_show(start_code + 1, end_code)
    return res_lst


if __name__ == '__main__':

    # задаем начальные и конечные коды ASCII-таблицы
    START_CODE, END_CODE = 32, 127
    # разделитель пар код-значение при выводе
    SEPARATOR = '  '

    result = ascii_show(START_CODE, END_CODE)

    # вывод информации по 10 пар "код - значение"
    print(f"Вывод кодов и значений символов ASCII-таблицы "
          f"с кодами от {START_CODE} по {END_CODE}:")
    for idx, el in enumerate(result):
        if (idx + 1) % 10 == 0:
            print(el)
            continue
        print(el, end=SEPARATOR)
