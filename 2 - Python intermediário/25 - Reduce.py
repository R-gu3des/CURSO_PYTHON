"""
Reduce - Um reduce serve como um acumulador
"""
from Dados import lista, pessoas, produtos
from functools import reduce

# Funcionamento de um reduce

lista_num = [1, 5, 4, 8, 43, 10, 50]

acumulando = 0

for c in lista_num:
    acumulando += c
    
print(acumulando)

# Utilizando o reduce:

soma_lista = reduce(lambda ac, val: val + ac, lista, 0) # Ac de acumulador

print(soma_lista)

soma = sum([x['idade'] for x in pessoas])
print(soma)