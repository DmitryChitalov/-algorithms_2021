"""
Задание 5.
Задание на закрепление навыков работы со стеком

Реализуйте структуру "стопка тарелок".

Мы можем складывать тарелки в стопку и при превышении некоторого значения
нужно начать складывать тарелки в новую стопку.

Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы,
для реализации это структуры, добавьте новые методы (не рассмотренные в примере с урока)
для реализации этой задачи.

После реализации структуры, проверьте ее работу на различных сценариях

Подсказка:
Отдельне стопки можно реализовать через:
1) созд-е экземпляров стека (если стопка - класс)
или
2) lst = [[], [], [], [],....]

Примечание: в этом задании вспомните ваши знания по работе с ООП
и опирайтесь на пример урока

Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""

from random import choice


class StackOfPlates:
    def __init__(self, limit):
        self.stack = [[]]  # Хранилище экземпляров
        self.limit = limit  # Максимальная величина стопки
        self.last_stack = 0  # Индекс последней стопки в списке self.stack

    def __str__(self):  # Перегрузим встроенный метод. Будем визуально понятно выводить стопки.
        txt = ''
        for _ in range(len(self.stack)):
            txt += f'Стопка {_ + 1}:   '
        txt += '\n'
        for _ in range(self.limit - 1, -1, -1):
            for value in self.stack:
                txt += f'{value[_]:<12}' if _ < len(value) else '-' * 6 + ' ' * 6
            txt += '\n'
        return txt

    def is_empty(self):  # Проверка на пустоту.
        return self.stack == [[]]

    def push_in(self, elem):  # Добавление тарелки в последнюю стопку
        if len(self.stack[self.last_stack]) == self.limit:
            self.stack.append([])
            self.last_stack += 1
        self.stack[self.last_stack].append(elem)

    def pop_out(self):  # Убирает последнюю добавленную тарелку
        if not self.is_empty():
            plate = self.stack[self.last_stack].pop()
            if not self.is_empty() and not len(self.stack[self.last_stack]):
                self.stack.pop()
                self.last_stack -= 1
            return plate
        else:
            return 'Забирать нечего. Тарелок в стопках нет.'

    def pop_out_from_stack(self, stack_number):  # Убирает тарелку из стопки с введенным номером.
        if not self.is_empty():  # Проверку корректности вводимых данных не делаю. Итак код раздулся уже.
            plate = self.stack[stack_number - 1].pop()  # Так что предположим, что вводится корректный номер стопки.
            if not self.is_empty() and not len(self.stack[stack_number - 1]):
                self.stack.pop(stack_number - 1)
                self.last_stack -= 1
            return plate
        else:
            return 'Забирать нечего. Тарелок в стопках нет.'

    def push_in_stack(self, elem, stack):  # Добавление тарелки в конкретную стопку
        if stack < 1 or stack > self.last_stack + 1:
            return print('Стопки тарелок с таким номером нет.')
        if len(self.stack[stack - 1]) == self.limit:
            return print('Стопка тарелок с данным номером уже заполнена. Выберите другую стопку.')
        self.stack[stack - 1].append(elem)

    def get_val(self):  # Возвращает значение последней тарелки.
        return self.stack[self.last_stack][-1]

    def number_of_stacks(self):  # Возвращает количество стопок тарелок.
        return self.last_stack + 1

    def last_stack_count(self):  # Возвращает количество тарелок в последней стопке.
        return len(self.stack[self.last_stack])

    def number_of_plates(self):  # Возвращает общее число тарелок.
        return len(self.stack[self.last_stack]) + self.limit * self.last_stack

    def number_of_plates_like(self, value):  # Возвращает количество тарелок с введенным значением.
        counter = 0
        for i in self.stack:
            for j in i:
                counter = counter + 1 if j == value else counter
        return counter


# Создадим случайную последовательность элеметов.
rnd_plates = [choice(['red', 'orange', 'yellow', 'green', 'blue', 'violet', 'purple']) for _ in range(14)]
print('Сгенерированные данные:\n' + ', '.join(str(i) for i in rnd_plates))

# Создадим и заполним элемент класса значениями и выведем их.
instance = StackOfPlates(4)
instance1 = StackOfPlates(4)

for i in rnd_plates:
    instance.push_in(i)

print('\nНаши стопки:')
print(instance)

# Теперь продемонстрируем работу методов(push_in показан выше).
print(f'Проверка на пустоту:\n'
      f'Пуста ли наша заполненая коллекция стопок: {instance.is_empty()}\nА не заполненная: {instance1.is_empty()}\n')

print('Уберем последнюю добавленную в конец тарелку: ', instance.pop_out())
print('Уберем еще одну: ', instance.pop_out())

print('\nВидим, что последняя стопка пропала:')
print(instance)

print('Пробуем удалить тарелку из пустого множества стопок:\n' + instance1.pop_out())

print('\nУберем две тарелки из второй стопки: ' + ', '.join([str(instance.pop_out_from_stack(2)) for i in range(2)]))
print(instance)

print('Добавим красную тарелку во вторую стопку: ')
instance.push_in_stack('red', 2)
print(instance)

print('Пробуем добавить тарелку в полную стопку: ')
instance.push_in_stack('red', 1)
print(instance)

print('Уберем еще пять тарелок: ' + ', '.join([str(instance.pop_out_from_stack(2)) for i in range(5)]))
print('Видим, что пустая стопка пропала.')
print(instance)

print('Последней лежит тарелка цвета:', instance.get_val())
print('Количество стопок тарелок:', instance.number_of_stacks())
print('В последней стопке лежит тарелок:', instance.last_stack_count())
print('Общее число тарелок: ', instance.number_of_plates())
print('Число желтых тарелок в стопках:', instance.number_of_plates_like('yellow'))

