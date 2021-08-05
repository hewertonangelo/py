# Fatiamento de String,
# Análise com len() - comprimento do array, count() - conta quantas vezes um caractere se repete,
# find() - informa em que momento começou um caractere,
# transformações com replace() - trocar (reposicionar), upper(), lower(), capitalize() - jogar todos os caracteres para minusculo e a primeira ele ira jogar para maiuscula
# title() - transforma todos os caracteres antes do espaço em maiuscula,
# strip() - remove todos os espaços vazios antes e depois do texto
# rstrip() - começa a tratar pela direita lstrip() - começa pela esquerda,
# split() - aonde tiver espaços, ele ira dividir a string,
# junção com join() - Junta strings.

frase = 'Curso em video'
print(frase.count('o'))
print('Curso' in frase)
print(frase.split())
print(frase.upper().count('O'))
print(len(frase))
print(frase.replace('Curso','Android'))