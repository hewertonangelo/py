from math import hypot

cat =  float(input('digite o tamanho do cateto oposto: '))
adj = float(input('digite o tamanho do cateto adjacente: '))

print('o cumprimento do cateto oposto é {}, e o cateto adjacente é '
      '{}, contudo, a hipotenusa é {:.2f}'.format(cat, adj, hypot(cat, adj)))