import math


ang =  float(input('digite o angulo: '))

print('O angulo de {:.2f}, tem o SENO de {:.2f},\n O Coseno de {:.2f},\n E a tangente de {:.2f}'
      .format(ang, math.sin(math.radians(ang)), math.cos(math.radians(ang)), math.tan(math.radians(ang))))
