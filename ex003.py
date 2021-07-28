import math

num = int(input('digite um numero inteiro: '))

print('o número que você digitou foi o {}!\n o dobro dele é {}\n e triplo dele é {}\n e a raiz quadrada dele é {}'.format(num, (num *2), (num * 3), math.pow(num, 1/2)))