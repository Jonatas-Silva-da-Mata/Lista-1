tamanho = int(input('Digite o tamanho: '))
lista = []
lista_par = []

for i in range(tamanho):
    numero = int(input('Digite um numero: '))
    lista.append(numero)
  
    if numero % 2 == 0:
        lista_par.append(numero)
        soma = sum(lista_par)

print(f'Soma dos valores pares: {soma}')