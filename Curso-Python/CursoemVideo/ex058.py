import random
pc = random.randint(0,10)
user = 0
count = 0
while user != pc:
    user = int(input('Advinhe o número: '))
    if user != pc:
        count += 1
        print('Tente novamente!')
print('Você acertou!!')
print('Você precisou de {} tentativas para acertar.'.format(count+1))