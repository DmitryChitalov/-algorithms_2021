from memory_profiler import profile
from timeit import timeit

# !!!!!!!!! Почему то не получилось открыть текстовый файл, указав путь к нему!!!!!!!
# Получаем строку, содержащую путь к домашней директории:
# dir_path = Path.home()
# Объединяем полученную строку с недостающими частями пути
# path = Path(dir_path, 'text_1.txt')
# f = open(path, encoding="utf-8")
# print(f.read())

"""
Оператор return возвращает значение из функции все сразу вместе, как списки, а затем функция завершается. 
Выражение yield преобразует функцию в ГЕНЕРАТОР, чтобы возвращать значения одно за другим. 
Оператор return  не подходит, когда нам нужно вернуть большой объем данных. В этом случае 
выражение yield полезно для возврата только части данных и экономии памяти.

Использование ключевого слова yield, когда функция производит большой объем данных.
В файле Python уже есть встроенная функция readline() для чтения данных файла построчно, 
что позволяет эффективно использовать память, быстро и просто.
"""

# Применение ИТЕРАТОРА
@profile
def read_file(file_name):
    text_file = open(file_name, 'r', encoding="utf-8")
    line_list = text_file.readlines()
    text_file.close()
    return line_list
# print(read_file('text_1.txt'))
file_lines = read_file('text.txt')
print(type(file_lines))
# print(len(file_lines))
for line in file_lines:
    print(line)



# Применение ГЕНЕРАТОРА

@profile
def read_file_yield_1(file_name):
    text_file = open(file_name, 'r', encoding="utf-8")
    while True:
        line_data = text_file.readline()
        if not line_data:
            text_file.close()
            break
        yield line_data
file_data = read_file_yield_1('text.txt')
print(type(file_data))
for l in file_data:
    print(l)

print(f'Время Итератора', timeit("read_file", globals=globals(), number=1000))
print(f'Время Генератора', timeit("read_file_yield_1", globals=globals(), number=1000))

"""
функция генератора занимает немного больше времени, чем оператор return. 
Так как он должен отслеживать состояние функции при каждом вызове итератора next().
"""






