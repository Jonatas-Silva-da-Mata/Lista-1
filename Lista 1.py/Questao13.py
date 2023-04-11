tamanho = int(input('Digite o tamanho que deseja: '))
lista = []
lista_A = []

for i in range(tamanho):
    palavra = str(input('Digite uma palavra: '))
    lista.append(palavra)

    if palavra.startswith('a'):
        lista_A.append(palavra)

print(f'Palavra que começam com "a": {lista_A}')