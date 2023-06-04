n = int(input('digite a quilometragem do carro'))
if n >= 60:
    print('você foi multado!')
    m = (n-59)*7
    print('pague pela multa de R${:.2f}'.format(m))
print('dirija com segurança.')