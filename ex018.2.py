from math import sqrt
o = int(input('digite o valor do cateto oposto'))
a = int(input('digite o valor do cateto adjacente'))
h = o**2 + a**2
r = sqrt(h)
print('a hipotenusa é {}'.format(r))

