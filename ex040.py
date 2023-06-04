n = int(input('qual a idadedo jovem?'))

if n < 18:
    print('você terá que se alistar no futuro')
    print('você está',18 - n,'anos adiantado')
elif n == 18:
    print('você tem que se alistar')
else:
    print('já passou da hora de se alistar')
    print('você está',n - 18,'anos atrasado')