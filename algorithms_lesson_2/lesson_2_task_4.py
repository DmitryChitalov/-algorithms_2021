def div_by_two(n, start, my_list=[]):
    if len(my_list) == n:
        print(my_list)
        return sum(my_list)
    else:
        my_list.append(start)
        start = start / 2 * -1
        return div_by_two(n, start, my_list)


n = int(input('Enter number of elements in the list: '))
start = float(input('Enter start number: '))
print(div_by_two(n, start))
