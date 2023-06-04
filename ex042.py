c = int(input('qual é a idade do participante?'))

if c <= 9:
    print('mirin')
elif c <= 14:
    print('infantil')
elif c <= 19:
    print('junior')
elif c == 20:
    print('sênior')
else:
    print('master')