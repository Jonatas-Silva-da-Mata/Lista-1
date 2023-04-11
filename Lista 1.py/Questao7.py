tamanho = int(input('Digite o tamanho do vetor: '))
palavra_longa = ''

for i in range(tamanho):
    palavra = str(input('Digite uma palavra: '))
    

    if len(palavra) > len(palavra_longa):
        palavra_longa = palavra

print(palavra_longa) 
