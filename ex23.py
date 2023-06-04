no = str(input('Insira seu nome:'))
no = no.title()
m = no.upper()
mi = no.lower()
q = len(no) - no.count(' ')
l = no.split()
print('nome: {}\nmaiusculo: {}\nminusculo: {}\ntotal de letras: {}\nprimeiro nome: {}'.format(no,m,mi,q,l[0]))
#laura wanessa da cruz correa