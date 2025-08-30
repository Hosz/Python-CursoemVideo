import random
count = 0
y = ()
while count != 5:
    num = random.randrange(0, 11)
    y += (num, )
    count += 1
print(f'Os valores sorteados foram {y}')
print(f'O maior valor foi {max(y)}')
print(f'O menor valor foi {min(y)}')
