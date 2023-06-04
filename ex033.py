import calendar
n = calendar.isleap(int(input('digite um ano')))
if n == True:
    print('esse ano é bisexto')
else:
    print('esse ano não é bisexto')
