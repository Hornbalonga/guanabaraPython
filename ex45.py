import random
pc =('pedra','papel','tesoura')
pc2 = random.randint(0,2)
j = int(input('escolha...\n0. pedra\n1. papel \n2. tesoura'))
print('pc escolheu {}'.format(pc[pc2]))
print('jogador escolheu {}'.format(pc[j]))

if pc2 == 0:
    if j == 0:
        print('empate')
    if j == 1:
        print('o jogador ganhou')
    if j == 2:
        print('o pc ganhou')
elif pc2 == 1:
    if j == 0:
        print('o pc ganhou')
    if j == 1:
        print('empate')
    if j == 2:
        print('o jogador ganhou')
elif pc2 == 2:
    if j == 0:
        print('o jogador ganhou')
    if j == 1:
        print('o pc ganhou')
    if j == 2:
        print('empate')
else:
    print('invalido')