tamanho = int(input('Digite o tamanho: '))
lista =  []

multiplicacao = 1

for i in range(tamanho):
    numero = int(input('Digite um número: '))
    lista.append(numero)

    multiplicacao *= numero

print(f'Resultado da multiplicacao: {multiplicacao}')