"""
Задание 3 *.
Сделать профилировку для скриптов с рекурсией и сделать описание,
можно ли так профилировать и есть ли 'подводные камни' в профилировании?
Придумать как это решить!
Есть очень простое решение
"""
from memory_profiler import profile, memory_usage
from random import randint

print('Использование памяти до выполнения функции', memory_usage()[0])


@profile
def m_1():
    def recursive_reverse(number, count=0):
        count += 1
        if count == 900:
            print("Использование памяти в последнем вызове рекурсии", memory_usage()[0])
            number += f'{[randint(1000000, 99999999999999) for _ in range(1000)]}'

            return number
        number += f'{[randint(1000000, 99999999999999) for _ in range(1000)]}'
        # number += [randint(1000000, 99999999999999) for _ in range(1000)]
        # Такая генерация для того чтобы питон выделял новую память на новые обьекты так как список
        # с числами до 1000000 был создан и передан в аргумент функции
        return recursive_reverse(number, count)

    a = print(len(recursive_reverse(f'{[i for i in range(1000000)]}')))

m_1()
print("Использование памяти после вызова функции", memory_usage()[0])

"""
Вроде у меня пллучилось сделать коректный подсчет выделения памяти на рекурсию 
До вызова рекурсии выделялось 19 MiB
В последнем ее вызове уже 110 MiB
После вызова 28 MiB
После последнего вызова рекурсии после возврата обратно память выделеная на работу рекурсии освобождается 
и остается только занятая память под результат 
Так же это подтвержадет таблица. И она показывает количество исполнений строк в Occurences 
Хотя инкремент показывает странные числа вроде

110.4 MiB -16886.8 MiB  899 return number.append(recursive_reverse(number, count)) и 
59.6 MiB  -2498.4 MiB     1000003       recursive_reverse([i for i in range(1000000)])

что должно нам как бы говорить что такое количество памяти освобождено и возможно я не верно решил это задание
Однако есл передовать в рекурсию строку то возростает использование памяти но покозания становатся страннее
Использование памяти в последнем вызове рекурсии 630.9 MiB
Но в таблице показывет в 16 строчке 10174.5 MiB  в 19 начинает показывать 631.2 MiB и большие минусы в инкременте
После выполнения функции вообще паммяти 5 MiB
Что-то я вообще запутался с этим выделением памяти и как оно работает при каждом вызове разные значения 
и в диспетчере задач показывает что питон заберает по мере выполнения этого скрипта до 12 Гб оперативки
"""
