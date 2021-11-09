"""
Вывод символы и кодов таблицы ASCII по quantity_elements_in_line в строку
"""


def print_ansi_in_range(start_ansi_index, end_ansi_index, final_string="", count=1, quantity_elements_in_line=10):

    if start_ansi_index > end_ansi_index + 1:
        return "Начальный индекс не может быть > конечного!"

    if start_ansi_index == end_ansi_index + 1:
        return final_string
    else:
        if count < quantity_elements_in_line:
            final_string += f"{start_ansi_index} - {chr(start_ansi_index)} "
        else:
            final_string += f"{start_ansi_index} - {chr(start_ansi_index)} \n"
            count = 0

        count += 1
        start_ansi_index += 1
        return print_ansi_in_range(start_ansi_index, end_ansi_index, final_string, count)


print(print_ansi_in_range(32, 127))
