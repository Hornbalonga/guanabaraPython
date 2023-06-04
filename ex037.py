c = int(input('diga o valor da casa'))
s = int(input('diga o valor do salário'))
a = int(input('em quantos anos ela será paga?'))
r = (c/a)
p = (s*30)/100
print('R${:.2f}'.format(r))
print('R${:.2f}'.format(p))

if r > p:
    print('infelizmente,não é possivel realizar a compra')
else:
    print('a compra pode ser efetuada')

