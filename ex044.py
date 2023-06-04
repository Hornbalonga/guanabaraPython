v = float(input('qual é o preço do produto?'))
d = int(input('qual vai ser a forma de pagamento?\n1. dinehro ou cheque\n2. cartao\n3. 2x\n4. 3x ou mais'))

if d == 1:
    s = (v*10)/100
    print('com 10% de desconto, ficara R${}'.format(s))
    print(d)

elif d == 2:
    a2 = (v*5)/100
    print('com 5% de desconto, ficara R${}'.format(a2))

elif d == 3:
    print('preço normal')

elif d == 4:
    a3 = (v*5)/100
    a4 = v + a3
    print('com 20% de juros, ficara R${}'.format(a4))
else:
    print('tente novamnete')
