"""
Задание 1.

Выполните профилирование памяти в скриптах
Проанализировать результат и определить программы с
наиболее эффективным использованием памяти.

Результаты профилирования добавьте в виде комментариев к коду.
Обязательно сделайте аналитику (что с памятью в ваших скриптах, в чем ваша оптимизация и т.д.)
"""
from random import randrange
import memory_profiler
from timeit import default_timer


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        start_time = default_timer()
        result = func(*args)
        m2 = memory_profiler.memory_usage()
        mem_usage = m2[0] - m1[0]
        run_time = default_timer() - start_time
        return result, mem_usage, run_time
    return wrapper


@decor
def not_repeat_check_1(test_list):
    new_list_1 = [elem for elem in test_list if test_list.count(elem) == 1]
    return new_list_1


@decor
def not_repeat_check_2(test_list):
    new_list = [elem for num, elem in enumerate(test_list) if elem not in test_list[num + 1:]
                and elem not in test_list[:num]]
    return new_list


@decor
def not_repeat_check_3(test_list):
    for num, elem in enumerate(test_list):
        if elem not in test_list[num + 1:] and elem not in test_list[:num]:
            yield elem


if __name__ == '__main__':

    original_list = [randrange(1, 9999, 2) for i in range(10000)]

    res_1, mem_diff, runtime = not_repeat_check_1(original_list)
    print(f"Выполнение заняло {mem_diff} Mib и {runtime} секунд")

    res_2, mem_diff, runtime = not_repeat_check_2(original_list)
    print(f"Выполнение заняло {mem_diff} Mib и {runtime} секунд")

    my_generator, mem_diff, runtime = not_repeat_check_3(original_list)
    print(f"Выполнение заняло {mem_diff} Mib и {runtime} секунд")

    # for element in my_generator:
    #     print(element)


"""
Представлен список чисел. Определить элементы списка, не имеющие повторений.
Сформировать итоговый массив чисел, соответствующих требованию.
Элементы вывести в порядке их следования в исходном списке.

Для решения задачи решил сделать реализацию через подсчёт количества элементов:
    - выполнение заняло 0.00390625 Mib и 1.5252192 секунд
Вторым вариантом решил использовать срезы:
    - выполнение заняло 0.47265625 Mib и 0.2567887 секунд

В первом случае мы практически не трогаем память, т.к. работаем с одним списком, но тратим время на подсчёт 
кол-ва вхождений, а во втором варианте мы очень сильно выигрываем в скорости, но проигрываем в памяти.

Т.е. я получил двоякую ситуацию - или жертвовать памятью, но выигрывать в скорости, используя срезы,
или наоборот, используя list comprehension.

Для эксперимента решил применить "ленивые вычисления". Получил интересные результаты:
Выполнение заняло 0.00390625 Mib и 0.10063320000000003 секунд

Т.е. памяти выделяется столько-же, сколько и при использовании исключений - т.е. это память на создание 
оригинального списка, а времени на данном этапе экономим ещё больше, чем в срезах, а данные всё равно потом 
извлекать. Но, данный метод, как и отмечалось ранее на лекции, имеет место быть.
"""
