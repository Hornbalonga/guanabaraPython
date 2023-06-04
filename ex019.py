import math
a = int(input('digite o valor do ângulo'))
c = math.cos(math.radians(a))
s = math.sin(math.radians(a))
t = math.tan(math.radians(a))
print('o seno é {:.2f}, o cosseno é {:.2f}, e a tângente é {:.2f}'.format(s,c,t))