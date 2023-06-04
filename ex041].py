m = float(input('digite a primeira nota'))
m2 = float(input('agora, a segunda'))
r = (m + m2)/2

if r <= 5.0:
    print('sua nota não atingiu a média, reprovado\n',r)
elif r >= 7.0:
    print('sua nota atingiu a média, aprovado\n',r)
else:
    print('precisará fazer a recuperação\n',r)