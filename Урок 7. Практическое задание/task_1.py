"""
1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100). Выведите на экран
исходный и отсортированный массивы.

Сортировка должна быть реализована в виде функции.

Обязательно доработайте алгоритм (сделайте его умнее).

Идея доработки: если за проход по списку не совершается ни одной сортировки,
то завершение. Обязательно сделайте замеры времени обеих реализаций
и укажите дала ли оптимизация эффективность.

Подсказка: обратите внимание, сортируем не по возрастанию, как в примере,
а по убыванию.

Сделайте выводы!!!
Опишите в чем была ваша доработка и помогла ли вам доработка??
"""
from random import randint
from timeit import timeit

lst = [randint(-100, 100) for x in range(100)]
print(lst)

def bubble_sort(lst_obj):
	n = 0
	while n < len(lst_obj):
		for i in range(len(lst_obj) - 1):
			if lst_obj[i] < lst_obj[i+1]:
				lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
		n += 1
	return lst_obj

print(bubble_sort(lst.copy()))

def bubble_sort_update(lst_obj):
	n = 0
	while n < len(lst_obj):
		end_flag = 1
		for i in range(len(lst_obj) - n - 1):
			if lst_obj[i] < lst_obj[i+1]:
				lst_obj[i], lst_obj[i+1] = lst_obj[i+1], lst_obj[i]
				end_flag = 0
		if end_flag == 1:
			break
		n += 1
	return lst_obj

print(bubble_sort_update(lst.copy()))

print(timeit('bubble_sort(lst.copy())', globals=globals(), number=10000))  # 7.779501289
print(timeit('bubble_sort_update(lst.copy())', globals=globals(), number=10000))  # 5.17235508

"""
Доработка с флагом дала незначительные плоды, разница есть, но она слаба ощутима,
из 10000 запусков, массива в 100 элементов в среднем экономия была ~10 итераций,
по времени это совсем незначительно.

После добавления в оптимизацию уменьшния итераций на каждом шаге разница во времени стала существеннее
"""