a = int(input('tamanho da reta 1'))
b = int(input('tamanho da reta 2'))
c = int(input('tamanho da reta 3'))
if (b-c) < a and (b+c) > a and (a-b) < c and (a+b) > c and (a-c) < b and (a+c) > b and a== b and a==c and b==c:
    print('equilátero')
    print('um triângulo, massa')

elif (b-c) < a and (b+c) > a and (a-b) < c and (a+b) > c and (a-c) < b and (a+c) > b and a==b or a==c or b==c :
    print('isóceles')
    print('um triângulo, massa')

elif (b-c) < a and (b+c) > a and (a-b) < c and (a+b) > c and (a-c) < b and (a+c) > b and a!=b and b!=c and c!=a:
    print('escaleno')
    print('um triângulo, massa')
else:
    print('poxa, não é um triângulo')