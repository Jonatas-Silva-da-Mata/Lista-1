tamanho = int(input('Digite o tamanho que deseja: '))

lis_descrecente = []

for i in range(tamanho):
    valores = int(input('Digite um valor:'))
    lis_descrecente.append(valores)

print(f'Lista: {sorted(lis_descrecente, reverse=True)}')