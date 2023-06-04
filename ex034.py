n1 = int(input('primerio valor'))
n2 = int(input('segundo valor'))
n3 = int(input('terceiro valor'))
if n1 > n2 and n1 >n3:
    print('o numero {} é maior'.format(n1))
if n2 > n1 and n2 >n3:
    print('o numero {} é o maior'.format(n2))
if n3 > n1 and n3> n2:
    print('o numero {} é maior'.format(n3))

if n1 < n2 and n1 < n3:
    print('o numero {} é menor'.format(n1))
if n2 < n1 and n2 < n3:
    print('o numero {} é o menor'.format(n2))
if n3 < n1 and n3 < n2:
    print('o numero {} é menor'.format(n3))