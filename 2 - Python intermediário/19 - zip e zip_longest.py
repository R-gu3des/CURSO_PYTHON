"""
Zip - Unindo iteráveis
Zip_longest - Itertools
"""
from itertools import count, zip_longest

# Código
cidades = ['São Paulo', 'Recife', 'Salvador', 'Rio de Janeiro']

# Código
estados = ['SP', 'PE', 'BA', 'RJ']

cidades_estados1 = zip(cidades,estados) # Um zip pega os valores de um e depis do outro na mesma posição e ele junta apenas até a quantidade de valores da menor lista
# print(next(cidades_estados))
# print(next(cidades_estados))
# print(next(cidades_estados))


# Para corrigir o que o zip faz é possivel usar o zip_longest
# Pois o zip junta apenas até o valor par



# Código
cidades2 = ['São Paulo', 'Recife', 'Salvador', 'Rio de Janeiro','Camaragibe']

# Código
estados2 = ['SP', 'PE', 'BA', 'RJ']

cidades_estados2 = zip_longest(cidades, estados, fillvalue='Estado') # Dessa forma se não houver um par será preenchido com um 'none'
# Para que não seja preenchido com none pode se usar o fillvalue para preencher






# indice = count()
# cidades_estados = zip_longest(
#     indice,
#     cidades,
#     estados,
#     fillvalue='Estado'
# )

# for indice, cidade, estados in cidades_estados:
#     print(indice, cidade, estados) 
# Com um gerador e um zip_longest dá erro porque um gerador não tem fim

# é melhor usar um zip


# Código
cidades3 = ['São Paulo', 'Recife', 'Salvador', 'Rio de Janeiro','Camaragibe']

# Código
estados3 = ['SP', 'PE', 'BA', 'RJ']

indice3 = count()
cidades_estados3 = zip(
    indice3,
    cidades2,
    estados2
)
for valores in cidades_estados2:
    print(valores) 

for indice, cidade, estados in cidades_estados3:
    print(indice, cidade, estados) 