n = int(input('qual a distância da viagem?'))
r = n*0.50
l = n*0.45
if n <= 200:
    print('será cobrado R${:.2f} '.format(r))
else:
    print('será cobrado R${}'.format(l))