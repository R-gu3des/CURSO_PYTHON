"""
For in em python
Iterando strings com for
Função range(começo, fim, passo a passo)

"""

frase = 'One piece'

for letra in frase:
    print(letra)

   
# Se você também quiser o index, só usar a funcão 'enumerate'

for index, letra in enumerate(frase):
    print(f'{index} - {letra}')

#  Usando a função 'range'

for c in range(1,10):
    print(c)
for c in range(20, 10, -1):
    print(c)
