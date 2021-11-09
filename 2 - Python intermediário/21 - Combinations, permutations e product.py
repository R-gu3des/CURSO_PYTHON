"""
Combinations, Permutations e product
Combinação - Ordem não importa
Permutação - Ordem importa
Ambos não retem valores únicos
Produto - Ordem importa e repete valores únicos
"""



from itertools import combinations, permutations, product

"""Combinations / Combinações"""
# Cria uma combinação com uma lista. Ex:

pessoas = ['Ruan','Jonas','Marcela','Amanda','Melissa','Pedro']
 
print('-=' * 25)

for grupo in combinations(pessoas, 2): # Se passa o elemento e o numero de elementos para o grupo
    print(grupo) # Aqui printa todas as combinações possíveis
print('\n')

print('-=' * 25)

"""Permutations / Permutações"""

frutas = ['Pera','Uva','Maçã','Manga','Abacaxi','Limão']

for grupo in permutations(frutas, 2):
    print(grupo)

print('-=' * 25)

"""Product / Produto"""

bebidas = ['Vinho','Cerveja','Shake','Suco','Refrigerante','Gin','Licor','Água']

for p in product(bebidas, repeat=2): # No caso do product é diferente dos anteriores você precisa usar o repeat
    print(p)

