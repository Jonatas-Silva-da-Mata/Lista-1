tamanho = int(input('Digite o tamanho que deseja: '))
lista = []
lista_menor_5 = []

for i in range(tamanho):
    numero = int(input('Digite um valor: '))
    lista.append(numero)

    if numero < 5:
        lista_menor_5.append(numero)

print(f'Valores maiores que 10: {lista_menor_5}')