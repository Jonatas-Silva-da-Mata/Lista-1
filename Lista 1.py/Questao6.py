tamanho = int(input('Digite o tamanho do vetor: '))
lista = []

for i in range (tamanho):
    n = int(input('Coloque os números que desejas: '))
    lista.append(n)

    soma = sum(lista)
    print(soma)
