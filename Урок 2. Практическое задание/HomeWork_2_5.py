def codes(n=32, step=1):
    if n == 128:
        return f'{n} - {chr(n)}'
    else:
        if step % 10 == 0:
            print(f'{n} - {chr(n)}', end='\n')
            n += 1
            step += 1
        else:
            print(f'{n} - {chr(n)}', end=' ')
            n += 1
            step += 1
            return codes(n, step)
        return codes(n, step)

print(codes())
