def summ_numbers(n, step=1, sum=0):
    if n == 1:
        return sum + 1
    else:
        step = (step / 2) * -1
        sum += step
        n -= 1
        return summ_numbers(n, step, sum)

print(summ_numbers(8))