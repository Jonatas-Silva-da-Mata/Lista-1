tamanho = int(input('Digite o tamanho: '))
lista = []
lista_impar = []

for i in range(tamanho):
    numero = int(input('Digite um numero: '))
    lista.append(numero)

    if numero % 2 != 0:
        lista_impar.append(numero)

print(f'Valores pares: {lista_impar}')