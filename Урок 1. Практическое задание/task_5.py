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

STACK_SIZE = 10  # размер стопки тарелок


class StackPlates:
    """Класс стэк.
    """
    def __init__(self):
        self.plates = []

    def push_in(self):
        self.plates.append('Тарелка')

    def pop_out(self):
        return self.plates.pop()

    def stack_size(self):
        return len(self.plates)

    def __str__(self):
        return str(len(self.plates))

    @property
    def is_empty(self):
        return self.plates == []

    @property
    def is_full(self):
        return len(self.plates) == STACK_SIZE


class Handler:
    """Класс обработчик.
       Содержит список стэков.
       Отслеживает заполнение стэка и в случае необходимости создает новый
    """
    def __init__(self):
        self.stacks = []

    def get_actual_stack(self):
        """Функция получения актуального стэка.
           Если стэков нет, то создает новый.
           Если стэки есть, то находит первых неполный
        """
        if self.is_empty():
            self.stacks.append(StackPlates())
            return self.stacks[0]
        else:
            for stack in self.stacks:
                if not stack.is_full:
                    return stack

    def put_plates(self, N):
        stack = self.get_actual_stack()
        for i in range(N):
            if not stack.is_full:
                stack.push_in()
            else:
                stack = StackPlates()      # Создаем новый экземпляр стэка
                self.stacks.append(stack)
                stack.push_in()

    def is_empty(self):
        return self.stacks == []

    def __str__(self):
        """Функция переопределения вывода.
        """
        string = ''
        for stack in self.stacks:
            string = f'{string}Количестов тарелок в стопке {stack}\n'
        return string


plates = int(input('Введите количество тарелок: '))
stack_plates = Handler()
stack_plates.put_plates(plates)
print(stack_plates)

