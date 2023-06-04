n = float(input('infome seu salário atual'))
if n <= 1250:
    c = (n * 15) / 100
    d = c + n
    print('seu salário aumentou 15%, agora é de R${:.2f}'.format(d))
else:
    a =(n*10)/100
    b = a+n
    print('seu salário aumentou 10%, agora é de R${:.2f}'.format(b))
