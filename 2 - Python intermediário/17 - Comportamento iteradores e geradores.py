"""
Comportamento dos iteradores
"""

nome = 'Ruan Guedes'

# Eu consigo iterar na string através de um for
for letras in nome:
    print(letras)
print('-' * 20)


#  transformando uma string em um iterador

nome = iter(nome) # Sempre que chamar um next será devolvido o próximo elemento

print(next(nome))
print(next(nome))
print(next(nome))
print('-' * 20)

# Se todos os elementos da variavel forem chamados com o next, ocorrerá um erro no próximo next,
# pois não existem mais elementos a serem chamados.


"""Se forem chamados elementos de um iterador eles deixam de fazer parte da variável"""

# Ex:

nome2 = 'Leonardo Cardoso'
nome2 = iter(nome2)

print(next(nome2)) # L
print(next(nome2)) # e
print(next(nome2)) # o
print(next(nome2)) # n
print('-' * 20)

# Com isso se formos pecorrer com um for sobre a variavel nome2, só apareceram os próximos elementos

for letra in nome2:
    print(letra)
print('-' * 20)

# Um gerador possui o mesmo comportamento que um iterador

# Ex:
nome3 = 'Fernandes Vieira'

gerador = (v for v in nome3)

print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print(next(gerador))
print('-' * 20)

for letra in gerador:
    print(letra)  