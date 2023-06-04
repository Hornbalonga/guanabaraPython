a = int(input('quantos dias alugado?'))
b = int(input('quantas horas por km?'))
c = (60*a) + (0.15*b)
print('o total a pagar é R${}'.format(c))