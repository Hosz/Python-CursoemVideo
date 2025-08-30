n = list()
for q in range(0,5):
    p = int(input('Digite um número: '))
    if q == 0 or p > n[-1]:
        n.append(p)
    else:
        pos = 0
        while pos < len(n):
            if p <= n[pos]:
                n.insert(pos, p)
                break
            pos += 1
print(f'Os valores adicionados na lista foram {n}')