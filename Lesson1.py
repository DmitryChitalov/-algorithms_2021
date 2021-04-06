"""Задание 1.

Для каждой из трех задач выполнить следующее:

1) для каждой инструкции рядом в комментарии определите сложность этой инструкции;
2) определите сложность алгоритма в целом;

укажите сложность непосредственно в этом файле
точки, где нужно поработать вам, отмечены знаком '!!!'
Не забудтье оценить итоговую сложность каждого из трех алгоритмов."""

import random


#############################################################################################
def check_1(lst_obj):
    """Функция должна создать множество из списка.
    Алгоритм 3:
    Создать множество из списка
    Сложность: O(n).
    """
    lst_to_set = set(lst_obj)  # O(n)
    return lst_to_set  # O(1)


#############################################################################################
def check_2(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.
    Алгоритм 1:
    Проходимся по списку и для каждого элемента проверяем,
    что такой элемент отстутствует
    в оставшихся справа элементах
    Сложность: O(n ^ 2).
    """
    for jj in range(len(lst_obj)):          # O(n)
        if lst_obj[jj] in lst_obj[jj+1:]:    # O(n)
            return False                   # O(1)
    return True                            # O(1)


#############################################################################################
def check_3(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.
    Алгоритм 2:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.
    Сложность: O(n * log(n))
    """
    lst_copy = list(lst_obj)                 # O(n)
    lst_copy.sort()                          # O(n * log(n))
    for i in range(len(lst_obj) - 1):        # O(n)
        if lst_copy[i] == lst_copy[i+1]:     # O(1)
            return False                     # O(1)
    return True                              # O(1)

#############################################################################################


for j in (50, 500, 1000, 5000, 1000):
    # Из 100000 чисел возьмем 'j' случайно выбранных
    # Всего 10 тыс. чисел
    lst = random.sample(range(-100000, 100000), j)

print(check_1(lst))
print(check_2(lst))
print(check_3(lst))

"""Задание 2.

Реализуйте два алгоритма:

Первый, в виде функции, должен обеспечивать поиск минимального значения для списка.
В основе алгоритма должно быть сравнение каждого числа со всеми другими элементами списка.
Сложность такого алгоритма: O(n^2) - квадратичная.

Второй, в виде функции, должен обеспечивать поиск минимального значения для списка.
Сложность такого алгоритма: O(n) - линейная.
Не забудьте указать где какая сложность."""

# Сложность: O(n).


def min_in_list(list_1):

    min_n = list_1[0]

    for i in range((len(list_1) - 1)):

        if min_n > list_1[i + 1]:
            min_n = list_1[i + 1]

    return min_n


# Сложность: O(n ^ 2).


def min_in_list_2(list_1):

    min_n = list_1[0]

    for i in range(2, (len(list_1)), 2):  # 0 2 4

        for k in range(1, (len(list_1)), 2):  # 1 3

            if min_n > list_1[k] > list_1[i] or min_n > list_1[k] == list_1[i] or list_1[k] > min_n > list_1[i]:
                min_n = list_1[i]

            elif min_n > list_1[i] > list_1[k] or list_1[i] > min_n > list_1[k]:
                min_n = list_1[k]

    return min_n


print(min_in_list(lst))
print(min_in_list_2(lst))
print(min(lst))

"""Задание 3.

Для этой задачи:

1) придумайте 2-3 решения (не менее двух);
2) оцените сложность каждого решения в нотации О-большое;
3) сделайте вывод, какое решение эффективнее и почему.

Примечание:

Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.

Сама задача:

Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат."""

company_name = ['Компания 1', 'Компания 2', 'Компания 3', 'Компания 4', 'Компания 5']
company_profit = [0, 10000, 5000, 223587, 15474]
random.shuffle(company_profit)
company_data = {i: j for i, j in zip(list(set(company_name)), company_profit)}
# из двух списков создаю случайный словарь данных
print('')
print(company_data)

# solution 1: O(n ^ 2)

list_2 = []

for i in company_data:

    list_2.append(company_data.get(i))

while len(list_2) > 3:

    list_2.remove(min(list_2))  # Просьба прокомментировать:
    # даёт ли удаление элемента, который высчитывается через min/max, двойной (квадратичный) перебор.
    # Я понял, что да, поэтому в следующем решении выполню это действие пошагово.

a = '\n«Solution 1». Top-3 the most profitable companies:'

for i in company_data:  # Потеря в эффективности происходит и здесь из-за for in + if in. Попробую избежать этого.

    if company_data[i] in list_2:
        a = a + ', ' + i

a = a.replace(':,', ':') + '.'
print(a)

# solution 2: O(n ^ 2)

n_list = []

for i, n in company_data.items():

    n_list.append(n)

i = 0

while len(n_list) > 3:

    n_list_max = min(n_list)
    n_list.remove(n_list_max)

n_index = 0

a = '\n«Solution 2». Top-3 the most profitable companies:'

for i, n in company_data.items():  # Двойного поиска в списках/словарях не удалось избежать таким способом.

    try:
        n_index = n_list.index(n)  # Получение индекса по элементу — O(n)
    except ValueError:
        continue

    if n == n_list[n_index]:
        a = a + ', ' + i

a = a.replace(':,', ':') + '.\n'
print(a)

# Вывод: Оба решения имеют квадратичную О-нотацию. Если, как я указывал в примечании, моё понимание верно, то второй
# способ будет чуть быстрее, так как квадратичный расчёт будет использован единожды.

"""Задание 4.

Для этой задачи:

1) придумайте 2-3 решения (не менее двух);
2) оцените сложность каждого решения в нотации О-большое;
3) сделайте вывод, какое решение эффективнее и почему.

Примечание:

Без выполнения пунктов 2 и 3 задание считается нерешенным. 
Пункты 2 и 3 можно выполнить через строки документации в самом коде.

Сама задача:

Пользователи веб-ресурса проходят аутентификацию. 
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована, а если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход, который вы придумаете, например, реализовать словарь."""

login_list = ['Angeline81', 'Caro_line', 'hHelen', 'Made_@leine', 'MagadanElena', 'iZubia487', 'Z1ubZie']
chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'
password_list = [''.join(random.choices(chars, weights=None, cum_weights=None, k=10)) for i in range(len(login_list))]
activation = [random.choice([True, False]) for i in range(len(login_list))]
user_data = [[a, b, c] for a, b, c in zip(login_list, password_list, activation)]

for i in enumerate(user_data, 1):
    print(i[0], '— login|password|activation:', i[1][0], '| ', i[1][1], '| ', i[1][2])

print('\nSolution 1:\n')
# solution 1: O(n)


def log_check(login, password, activation1):  # самое затратное действие  — перебор элементов, входящих в список.

    for i in user_data:

        if login == i[0] and password == i[1] and activation1 is True:
            print('Correct. Welcome!')
            break

        elif login == i[0] and password == i[1] and activation1 is False:
            print('Please activate your profile.')
            break

        elif i == user_data[-1]:
            print('Incorrect password or the login does not exist.')


log_check('a', 'b', 'c')
print()

for a1, b1, c1 in user_data:

    log_check(a1, b1, c1)

print()

for a1, b1, c1 in user_data:

    log_check(b1, a1, c1)

print('\nSolution 2:\n')

# solution 2: O(1) — второе решение эффективнее по временным затратам.


def log_check2(login, password, activation1):  # за счёт вызова элемента списка по индексу — O(1)

    for i in range(len(user_data)):

        if user_data[i][0] == login and user_data[i][1] == password and activation1 is True:
            print('Correct. Welcome!')

        elif user_data[i][0] == login and user_data[i][1] == password and activation1 is False:
            print('Please activate your profile.')
            break

        else:
            print('Incorrect password or the login does not exist.')


log_check('a', 'b', 'c')
print()

for a1, b1, c1 in user_data:

    log_check(a1, b1, c1)

print()

for a1, b1, c1 in user_data:

    log_check(b1, a1, c1)

print()


"""Задание 5. Задание на закрепление навыков работы со стеком.

Примечание: в этом задании вспомните ваши знания по работе с ООП и опирайтесь на пример урока.

Реализуйте структуру "стопка тарелок". 

Мы можем складывать тарелки в стопку, при превышении некоторого значения нужно начать складывать тарелки в новую стопку.
Структура должна предусматривать наличие нескольких стеков.
Создание нового стека происходит при достижении предыдущим стеком порогового значения.
Реализуйте по аналогии с примером, рассмотренным на уроке, необходимые методы, для реализации это структуры.
Добавьте новые методы (не рассмотренные в примере с урока) для реализации этой задачи.
После реализации структуры, проверьте ее работу на различных сценариях.

Подсказка:

Отдельные стопки можно реализовать через:
# 1) созд-е экземпляров стека (если стопка - класс);
# 2) lst = [[], [], [], [],....]."""


class Plates:
    def __init__(self, max_num=5):
        self.amount = []
        self.num = ''
        self.max_num_in_stack = max_num

    @property
    def name(self):
        for k, v in globals().items():
            if v == self:
                return k

    def __str__(self):

        self.plates_stacks = ''
        i = 0
        kk = 1

        while i < len(self.amount):

            for k in range(self.max_num_in_stack):
                if i < len(self.amount):
                    self.plates_stacks = self.plates_stacks + str(self.amount[-1 - i]) + ' '
                    i += 1

            self.plates_stacks = self.plates_stacks + f'— Стопка{kk};\n'
            kk += 1

        return self.plates_stacks

    def __add__(self, other):  # Просьба подсказать, как реализовать сумму, чтобы результат был объектом класса,
        # сохраняющим все параметры от сложения двух объектов

        i = 0

        while i < len(other.amount):
            self.amount.append(other.amount[-1 - i])
            i += 1

        return self.__str__()

    def is_empty(self):
        return self.amount == []

    def push_in(self, num):

        if isinstance(num, int) and num > 0:
            self.num = num

        i = 0
        while i < num:
            self.amount.append('Тарелка')
            i += 1
        return self.__str__()

    def push_smth(self, el):
        self.amount.append(el)

    def pop(self):
        return self.amount.pop()

    def pop_amount(self, num):

        if isinstance(num, int) and num > 0:
            self.num = num

        i = 0
        while i < num:
            self.amount.pop()
            i += 1
        return self.__str__()

    def get_val(self):
        return self.amount[len(self.amount) - 1]

    def stack_size(self):
        return len(self.amount)

    def all_plates(self):
        return self.amount

    def change_max_in_stack(self, new_max_in_stack):
        self.max_num_in_stack = new_max_in_stack


if __name__ == '__main__':

    stack = Plates()
    stack_1 = Plates()

    print(stack.is_empty())  # -> стек пустой

    stack.push_in(10)  # → 2 полные стопки
    print(stack)
    stack.pop()  # → 9
    stack_1.push_in(14)  # → 14
    print(stack_1)
    stack_1.push_in(3)  # → 17
    print(stack_1)
    print(stack_1 + stack)  # → 26
    print(stack)
    stack.push_smth('«Совсем не тарелка»')
    print(stack)
    stack.pop_amount(4)
    print(stack)
    stack.change_max_in_stack(3)
    print(stack)

"""Задание 6. Задание на закрепление навыков работы с очередью.

Примечание: в этом задании вспомните ваши знания по работе с ООП и опирайтесь на пример урока.

Реализуйте структуру "доска задач".

Структура должна предусматривать наличие несольких очередей задач, например:
1) базовой, откуда задачи берутся, решаются и отправляются в список решенных;
2) очередь на доработку, когда нерешенные задачи из первой очереди отправляются на корректировку решения.

После реализации структуры, проверьте ее работу на различных сценариях."""


class TaskBoard:

    def __init__(self):
        self.task_list = []
        self.task_name = ''
        self.ready_list = []
        self.in_process = []

    def is_empty(self):
        return self.task_list == []

    def add_task(self, task_name):

        self.task_name = task_name

        self.task_list.insert(0, self.task_name)

    def add_status_to_task(self, task_name, status):

        self.task_name = task_name

        if task_name in self.task_list:

            if status == 'ready'.lower():

                self.ready_list.insert(0, self.task_list.pop(self.task_list.index(task_name)))

            elif status == 'in process'.lower():

                self.in_process.insert(0, self.task_list.pop(self.task_list.index(task_name)))

            elif status != 'ready'.lower() or status != 'in process'.lower():

                print(f'The invalid status for {task_name}. It stays in unsorted TaskBoard')

        else:
            print('The task did not add to TaskBoard')

    def is_status(self, task_name):

        self.task_name = task_name

        if task_name in self.task_list:
            print(f'The {task_name} has unsorted status: in unsorted TaskBoard.')

        if task_name in self.ready_list:
            print(f'The {task_name} has ready status.')

        if task_name in self.in_process:
            print(f'The {task_name} has in process status.')

    def from_queue(self):
        return self.task_list.pop()

    def how_many_tasks(self):
        return len(self.task_list)


if __name__ == '__main__':
    task_board = TaskBoard()
    print(task_board.is_empty())  # -> True. Очередь пустая

    # помещаем объекты в очередь
    task_board.add_task('my_obj')
    task_board.add_task(4)
    task_board.add_task(True)

    print(task_board.is_empty())  # -> False. Очередь пустая

    print(task_board.how_many_tasks())  # -> 3

    print(task_board.from_queue())  # -> my_obj

    print(task_board.how_many_tasks())  # -> 2

    task_board.add_status_to_task(True, 'ready')
    task_board.add_status_to_task(4, 'in process')

    task_board.is_status(True)  # The True has ready status.
    task_board.is_status(4)  # The 4 has in process status.

    print(task_board.how_many_tasks())  # -> 0

"""Задание 7. Задание на закрепление навыков работы с деком.

В рассмотренном на уроке листинге есть один недостаток.
Приведенный код способен "обработать" только строку без пробелов, например, 'топот', но могут быть и такие палиндромы, 
как 'молоко делили ледоколом'. Вам нужно доработать программу так, чтобы она могла выполнить проверку на палиндром
и в таких строках (включающих пробелы)."""


class DequeClass:
    def __init__(self):
        self.elems = []

    def is_empty(self):
        return self.elems == []

    def add_to_front(self, elem):
        self.elems.append(elem)

    def add_to_rear(self, elem):
        self.elems.insert(0, elem)

    def remove_from_front(self):
        return self.elems.pop()

    def remove_from_rear(self):
        return self.elems.pop(0)

    def size(self):
        return len(self.elems)


if __name__ == '__main__':
    dc_obj = DequeClass()
    print(dc_obj.is_empty())  # -> True

    # добавить элементы в хвост
    dc_obj.add_to_rear(10)
    dc_obj.add_to_rear('my_str')

    # добавить элементы в голову
    dc_obj.add_to_front(None)
    dc_obj.add_to_front(True)

    # размер дека
    print(dc_obj.size())  # -> 4
    print(dc_obj.is_empty())  # -> False

    # добавить элемент в хвост
    dc_obj.add_to_rear(3.3)

    print(dc_obj.remove_from_rear())  # -> 3.3
    print(dc_obj.remove_from_front())  # -> True

# палиндром


    def pal_checker(string):

        ololo = DequeClass()

        for el in string.lower().replace(' ', '').replace('.', '').replace(',', '').replace(':', '').replace('-', ''):
            ololo.add_to_rear(el)

        still_equal = True

        if 2 > ololo.size() > 0:
            still_equal = 'The string has not necessary alphabetical letters!'
            return still_equal

        while ololo.size() > 1 and still_equal:
            first = ololo.remove_from_front()
            last = ololo.remove_from_rear()
            if first != last:
                still_equal = False

        return still_equal


    print(pal_checker('tenet'))  # → True
    print(pal_checker('tewset'))  # → False
    print(pal_checker('Sum summus mus'))  # → True
    print(pal_checker('мОлОкО Делили лЕдоКоЛоМ.'))  # → True
    print(pal_checker('мОлОкО Делили ЕоКоЛоМ.'))  # → False
    print(pal_checker('Лёша на полке клопа нашёл'))  # → True
    print(pal_checker('Лег на храм, и дивен и невидим архангел'))  # → True
    print(pal_checker(' 0.'))  # → The string has not necessary alphabetical letters!
