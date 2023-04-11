tamanho = int(input('Digite o tamanho: '))
lista = []

for i in range(tamanho):
    numero = int(input('Digite um numero: '))
    lista.append(numero)

media = sum(lista) / len(lista)

print(f'Resultado da media: {media:.2f}')