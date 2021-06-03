def sum_line(n, cur_sum=0, start=1):
    if start == n + 1 and cur_sum == n * (n + 1) / 2:
        print(f'1+2+...+{n} equals to {n} * ({n} + 1) / 2')
        return f'The result is {cur_sum}'
    else:
        cur_sum += start
        start += 1
        return sum_line(n, cur_sum, start)


user_num = int(input('Enter a number of terms: '))
print(sum_line(user_num))
