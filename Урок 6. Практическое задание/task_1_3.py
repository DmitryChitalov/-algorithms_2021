"""
Задание 1. Скрипт № 2

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Примечание: Для анализа возьмите любые 3-5 ваших РАЗНЫХ скриптов!
(хотя бы 3 разных для получения оценки отл).
На каждый скрипт вы должны сделать как минимум по две реализации.

Можно взять задачи с курса Основ
или с текущего курса Алгоритмов

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)

ВНИМАНИЕ: ЗАДАНИЯ, В КОТОРЫХ БУДУТ ГОЛЫЕ ЦИФРЫ ЗАМЕРОВ (БЕЗ АНАЛИТИКИ)
БУДУТ ПРИНИМАТЬСЯ С ОЦЕНКОЙ УДОВЛЕТВОРИТЕЛЬНО

Попытайтесь дополнительно свой декоратор используя ф-цию memory_usage из memory_profiler
С одновременным замером времени (timeit.default_timer())!
"""

# Скрипт - 'База данных сотрудников'. Использует класс модуля task_1_2 PositionSlots.


import pickle
import task_1_2
import os
from pympler import asizeof


def show_empl(workers_db):
    """Функция вывода данных"""
    print('-' * 50)
    for i in range(len(workers_db)):
        print(i, end='. ')
        workers_db[i].get_full_name()
        print('   Доход: ', end='')
        print(workers_db[i].get_total_income())


attr_worker_list = ['имя', 'фамилию', 'должность', 'оклад', 'премию']

if not os.path.isfile('empl.pic'):
    workers_db = []
    print('Размер list: ', asizeof.asizeof(workers_db))
    with open('empl.pic', 'wb') as f:
        print('Размер list.dump: ', asizeof.asizeof(pickle.dump(workers_db, f)))
        pickle.dump(workers_db, f)

with open('empl.pic', 'rb') as f:
    workers_db = pickle.load(f)

while True:
    choice = input('Добавить сотрудника в базу => 1\n'
                   'Удалить сотрудника из базы => 2\n'
                   'Просмотр базы сотрудников  => 3\n'
                   'Выход                      => 4\n'
                   'Введите номер действия: ')
    if choice == '4':
        print(f'{"-" * 50}\nВыход')
        break

    if choice == '1':
        # Ввод данных в базу
        print('-' * 50)
        worker_list = []

        for i in range(5):
            worker_list.append(input(f'Введите {attr_worker_list[i]} сотрудника: '))
        try:
            worker_list[3] = int(worker_list[3])
            worker_list[4] = int(worker_list[4])
        except ValueError:
            print('Ошибка ввода данных!')
            worker_list = []
            continue

        print('Размер list: ', asizeof.asizeof(worker_list))  # -------------------------------------
        worker_list = tuple(worker_list)
        print('Размер tuple: ', asizeof.asizeof(worker_list))  # ------------------------------------

        worker = task_1_2.PositionSlots(worker_list[0], worker_list[1], worker_list[2], worker_list[3], worker_list[4])
        workers_db.append(worker)
        print(f'Запись проведена\n{"=" * 50}')

        with open('empl.pic', 'wb') as f:
            print('Размер базы list: ', asizeof.asizeof(workers_db))  # -----------------------------
            print('Размер базы list.dump: ', asizeof.asizeof(pickle.dump(workers_db, f)))  # ---------
            pickle.dump(workers_db, f)

    if choice == '3':
        # Просмотр базы
        with open('empl.pic', 'rb') as f:
            workers_db = pickle.load(f)

        show_empl(workers_db)
        print('=' * 50)

    if choice == '2':
        # Удаление данных из базы
        with open('empl.pic', 'rb') as f:
            workers_db = pickle.load(f)

        show_empl(workers_db)
        number = input(f'{"-" * 50}\nДля отмены нажмите "q"\nВведите номер удаляемого пользователя: ')
        if number.isalpha() or int(number) < 0 or int(number) >= len(workers_db):
            print(f'{"-" * 50}\nВ базе нет пользователя с таким номером!\n{"=" * 50}')
            continue
        else:
            del workers_db[int(number)]
            print(f'Пользователь удален\n{"=" * 50}')

        with open('empl.pic', 'wb') as f:
            pickle.dump(workers_db, f)

"""
Оптимизировано:
    1. В модуле task_1_2 в материнском классе WorkerSlots - использование __slots__.
    2. Использование в качестве базы вместо списка объектов picle-файл (сериализация).
    3. Применение кортежа вместо списка при определении объекта класса PositionSlots.
    
Результаты замеров:
==================================================================
Добавить сотрудника в ,базу => 1
Удалить сотрудника из базы => 2
Просмотр базы сотрудников  => 3
Выход                      => 4
Введите номер действия: 1
--------------------------------------------------
Введите имя сотрудника: Max
Введите фамилию сотрудника: Pain
Введите должность сотрудника: murder
Введите оклад сотрудника: 200000
Введите премию сотрудника: 200000

Размер list:  352 
Размер tuple:  312    # !!! > Использование кортежа вместо списка

Запись проведена
==================================================
Размер базы list:  2440
Размер базы list.dump:  16   # !!! > Сериализация

Добавить сотрудника в ,базу => 1
Удалить сотрудника из базы => 2
Просмотр базы сотрудников  => 3
Выход                      => 4
===================================================================

При применении сериализации объем занимаемой памяти многократно уменьшился.
Вывод очевиден. Оптимизация памяти необходима в применении.
"""
