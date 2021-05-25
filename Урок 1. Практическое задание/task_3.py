"""
Задание 3.

Для этой задачи:
1) придумайте 2-3 решения (не менее двух)
2) оцените сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему

Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.

Примечание:
Без выполнения пунктов 2 и 3 задание считается нерешенным. Пункты 2 и 3 можно выполнить
через строки документации в самом коде.
Прошу вас внимательно читать ТЗ и не забыть выполнить все пункты.

Задание творческое. Здесь нет жестких требований к выполнению.
"""
brands = {"Coca-Cola": 198990,
             "Amazon": 198200,
             "Google": 190000,
             "Microsoft": 101900,
             "IBM": 135930,
             "Apple.Inc": 134343}  # O(len(...))


#  Variant_1

def top_three_1(best_world_brand):

    for el in range(len(best_world_brand)): # O(n)
        value_index = el
        for index in range(el + 1, len(best_world_brand)): #O(n)
            if best_world_brand[value_index][1] > best_world_brand[value_index][1]:
                value_index = index
        best_world_brand[el], best_world_brand[value_index] = best_world_brand[value_index], best_world_brand[el]
    return best_world_brand[:3]
  
# For Variant_1 O(n^2)-> Two loops, the rest of the lines are constant complexity

top_three_brands = list(brands.items())
for i in top_three_1(top_three_brands):
    print(f"Brand {i[0]} has profit ${i[1]} billions")

#Var2
def top_three_2(best_world_brand_two):
    top_brand ={}

    for el in range(3): #O(n)
        max_value = max(best_world_brand_two.items(), key=lambda k_v: k_v[1])
        del best_world_brand_two[max_value[0]]
        top_brand[max_value[0]] = max_value[1]
    return top_brand


print(top_three_2(brands))

# For Variant_1 O(n)-> One loop, the rest of the lines are constant complexity
