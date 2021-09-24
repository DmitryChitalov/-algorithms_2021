def all_sum(amount, element=1.0):
    if amount <= 1:
        return element
    else:
        return element + all_sum(amount - 1, element / -2)


if __name__ == '__main__':
    print(all_sum(3))
