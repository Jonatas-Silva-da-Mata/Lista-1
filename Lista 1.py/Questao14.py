tamanho = int(input('Digite o tamanho que deseja: '))
lista = []
lista_maior_10 = []

for i in range(tamanho):
    numero = int(input('Digite um valor: '))
    lista.append(numero)

    if numero > 10:
        lista_maior_10.append(numero)

print(f'Valores maiores que 10: {lista_maior_10}')