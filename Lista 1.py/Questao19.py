tamanho = int(input('Digite o tamanho que deseja: '))

lis_crescente = []

for i in range(tamanho):
    valores = int(input('Digite um valor:'))
    lis_crescente.append(valores)

print(f'Lista: {sorted(lis_crescente)}')