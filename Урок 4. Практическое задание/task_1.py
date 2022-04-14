"""
Задание 1.

Приведен код, который позволяет сохранить в
массиве индексы четных элементов другого массива

Сделайте замеры времени выполнения кода с помощью модуля timeit

Оптимизируйте, чтобы снизить время выполнения
Проведите повторные замеры.

Добавьте аналитику: что вы сделали и почему!!!
Без аналитики задание не принимается

И прошу вас обратить внимание, что то, что часто ошибочно называют генераторами списков,
на самом деле к генераторам отношения не имеет. Это называется "списковое включение" - list comprehension.
"""

from timeit import timeit

# 1. Вариант с циклом - базовое условие
def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


# 2. Вариант с list comprehension
def func_lc(nums):
    new_arr = [i for i in range(len(nums)) if nums[i] % 2 == 0]
    return new_arr


# 3. Генератор в список
def func_gen_list(nums):
    gen_index = (i for i in range(len(nums)) if nums[i] % 2 == 0)
    new_arr = [i for i in gen_index]  # можно было просто extend()
    return new_arr

# 4. Только генератор (если нет необходимости в массиве)
def func_only_gen(nums):
    new_arr_gen = (i for i in range(len(nums)) if nums[i] % 2 == 0)
    return new_arr_gen


nums = list(range(1000))
n = 10000

print('Цикл:', timeit('func_1(nums)', globals=globals(), number=n))
print('LC:', timeit('func_lc(nums)', globals=globals(), number=n))
print('Генератор --> Список:', timeit('func_gen_list(nums)', globals=globals(), number=n))
print('Генератор:', timeit('func_only_gen(nums)', globals=globals(), number=n))


"""
 Выводы:
 Реализовал несколько вариантов в процессе поиска наиболее оптимального.
 
 Вариант №2 с LC (list comprehension) получился еффективнее базового условия, 
 что объясняется отсуствием необходимости загружать метод append - в случае LC 
 python может использовать встроенную команду байт-кода с именем LIST_APPEND, которая 
 используется вместо ряда команд с циклом (перевод из документации):
                Загрузить список: 40 LOAD_FAST
                Загрузить атрибут: 43 LOAD_ATTRIBUTE
                Вызов загруженной функции: 49 CALL_FUNCTION
                Выгрузить список (?): 52 POP_TOP 
 
 Вариант №3, предполагающий использование генератора и вывод в LC, 
 каждый раз работает по разному. На больших значениях n может выдать лучший результат - см. ниже.
 Но дает не очень стабильные результаты при повторнх запусках.
 
 
 Вариант №4, предполагающий использование только генератора, приводится справочно, т.к.
 сравнивать его с предыдушими вариантами будет не корректно.
    Этот способ самый быстрый, но мы не получаем в данном случае массив из функции. 
    В определенных случаях, где требуется экономия памяти и не нужен массив, это лучший вариант.  
 
 Провел ряд замеров - см.результаты ниже:
 """


# Результаты:

# При n = 100 000
# Цикл: 11.526384700000001
# LC: 9.086186000000001
# Генератор --> Список: 8.812728100000001  !!!
# Генератор: 0.06530279999999777


# При n = 50 000
# Цикл: 5.8567693
# LC: 3.8461498999999995
# Генератор --> Список: 4.6719892000000005  !!!
# Генератор: 0.04194749999999914


# При n = 10 000
# Цикл: 1.3247522
# LC: 0.9111290000000001
# Генератор --> Список: 1.0488757 !!!
# Генератор: 0.006789899999999793