def fatorial(n=1, show=False):
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show:
            print(c, end='')
            if c > 1:
                print(end=' x ')
            else:
                print(end=' = ')
    return f

#r1 = format(5)
print(fatorial(5, False))