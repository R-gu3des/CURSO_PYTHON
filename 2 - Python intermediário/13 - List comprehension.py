"""
Utilizando list comprehension
"""

l1 = [1, 2, 3, 4, 5, 6, 7]

exemplo1 = [elemento for elemento in l1]
print(exemplo1)

exemplo2 = [el * 2 for el in l1] # Para cada elemento na lista multiplique por 2
print("multipicado =", exemplo2)

# Cria uma tupla com dois valores, o v para cada elemento da lista 1 e o v2 em um rnge de 3 para cada ellemento da lista 1
exemplo3 = [(v,v2) for v in l1 for v2 in range(3)]
print("tupla =", exemplo3)


######################################################

lista2 = ['Ruan', 'Roger','Amanda','Julieta','Marisvalda']

exemplo4 = [valor.replace('a','@') for valor in lista2]
print(exemplo4)

#######################################################

# Usando tupla

tupla = (
    ('Chave','Valor'),
    ('Chave2','Valor2')
)

exemplo5 = [(x,y) for y,x in tupla]
print(exemplo5)



# é possivel usar ifs
lista6 = list(range(100))
exemplo6 = [elemento for elemento in lista6 if elemento % 2 == 0]
print(exemplo6)
# se voce passar mis d eum if fica como se fosse um 'and'
exemplo7 = [v for v in lista6 if v % 3 == 0 if v % 8 == 0]
print(exemplo7)

# Quase um operador ternário
exemplo8 = [v if v  % 3 == 0 else 'Não é' for v in lista6]
print(exemplo8)

#  è possivel passar duas condições

exemplo9 = [v if v  % 3 == 0 and v % 8 == 0 else 'Não' for v in lista6]
print(exemplo9)