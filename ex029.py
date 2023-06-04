import random
n = int(input('digite um numéro'))
a = random.randint(0,5)
print('computador {} você {}'.format(a,n))
print('você ganhou! :)'if n == a else 'você perdeu! :(')