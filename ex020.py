import random
n1 = input('digite o nome prímeiro do aluno')
n2 = input('digite o nome segundo do aluno')
n3 = input('digite o nome terceiro do aluno')
n4 = input('digite o nome quarto do aluno')
no = [n1,n2, n3,n4]
es = random.choice(no)
print('o aluno sorteado foi {}'.format(es))