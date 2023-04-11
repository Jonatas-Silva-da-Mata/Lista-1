tamanho = int(input('Digite o tamanho: '))
lista = []

for i in range(tamanho):
    numero = int(input('Digite um número:'))
    lista.append(numero)

print(f'Maior valor: {max(lista)}') #max pega todos os valores da lista e mapea qual é o maior valor
