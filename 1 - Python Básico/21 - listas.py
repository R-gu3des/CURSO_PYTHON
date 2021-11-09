"""
Listas em Python:
fatiamento
append, insert, pop, del, clear, extend, +
min, max
range
"""

lista = ['a','b','c','e','f']
print(lista)
lista[4] = 'Hello, world!'
print(lista)
print(*lista[0:3])

# Adicionando elementos a uma lista com funções:

# append()
lista.append('x') # O append serve para adicionar um elemento no final da lista
print(lista)

# insert()
lista.insert(2, 'banana') # Serve para adicionar um elemento em um certo indice
print(lista)

# pop()
lista.pop() # remove o último elemento da lista
print(lista)

# del()
del(lista[2:3]) # É possível deletar elementos de uma lista escolhendo o inicio e o fim



