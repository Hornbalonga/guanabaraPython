a = float(input('digite sua altura'))
p = float(input('digite seu peso'))
imc =p/a**2

if imc < 18.5:
    print(imc)
    print('abaixo do peso')
elif imc < 25:
    print(imc)
    print('peso ideal')
elif imc < 30:
    print(imc)
    print('sobrepeso')
elif imc > 40:
    print(imc)
    print('obesidade')
else:
    print(imc)
    print('obesidade mórbida')