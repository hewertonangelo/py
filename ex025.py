nome = str(input('Digite um nome: ')).strip().lower()
n = nome.split()

print('seu primeiro nome é {} e seu ultimo nome é {}'.format(n[0], n[len(n)-1]))